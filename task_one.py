import json
import time
from utils import rand_id
from classes import Character

if __name__ == "__main__":
    characters = {}
    while len(characters) != 15:
        # Ensuring always unique character
        while True:
            char_id = rand_id()
            if char_id not in characters:
                break

        char = Character(char_id)
        time.sleep(1)
        characters[char_id] = char

    characters[char_id].get_cross_ref("films")
    print(characters[char_id].films)
    characters = [v.dump() for k, v in characters.items()]
    print(json.dumps(characters, indent=2))
