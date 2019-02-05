import json
import time
from utils import rand_id
from classes import Film

if __name__ == "__main__":
    film = Film(1)

    film.get_all_cross_refs()
    print(film.write_contents())
    with open("task_two.json", "w") as f:
        f.write(json.dumps(film.write_contents(), indent=2))
