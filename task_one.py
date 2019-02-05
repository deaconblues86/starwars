import db
import json
import argparse
from utils import rand_id
from classes import Character
from functools import reduce


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pull some characters from swapi and load them to MySQL')
    parser.add_argument("-u", "--user", required=True, help="MySQL username")
    parser.add_argument("-p", "--password", required=True, help="MySQL password")
    parser.add_argument("-d", "--db_url", required=True, help="MySQL host")
    args = parser.parse_args()

    characters = {}
    while len(characters) != 15:
        # Ensuring always unique character
        while True:
            char_id = rand_id()
            if char_id not in characters:
                break

        # Seems 17 is currently broken -- skipping it
        if char_id == 17:
            continue

        char = Character(char_id)
        char.get_cross_ref("films")
        char.prep_for_db()
        characters[char_id] = char

    try:
        # Set up DB connection, table, and load data
        engine = db.db_connect(args.user, args.password, args.db_url)
        char_table = db.create_char_table(engine)
        for char in characters:
            db.insert_character(engine, char_table, characters[char])

        # Pull names and films from DB
        characters = engine.execute("SELECT name, films from characters").fetchall()
        print(len(characters))

        # Prep and print to console
        films = set(reduce(lambda x, y: x + y, [c.films.split("|") for c in characters]))
        characters_by_film = [{"film": f,  "character": [c.name for c in characters if f in c.films]} for f in films]
        print(json.dumps(characters_by_film, indent=2))
        db.db_close(engine)

    finally:
        # Clean up DB afterwards
        db.drop_table(engine, char_table)
        db.db_close(engine)