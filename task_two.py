import json
from utils import metric2imperial
from classes import Film

if __name__ == "__main__":
    film = Film(1)

    film.get_all_cross_refs()
    for char in film.characters:
        char["mass"] = metric2imperial(char["mass"], "kg", "lb")
        char["height"] = metric2imperial(char["height"], "cm", "ft")
    with open("task_two.json", "w") as f:
        f.write(json.dumps(film.write_contents(), indent=2))
