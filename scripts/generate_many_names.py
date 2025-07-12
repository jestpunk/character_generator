import init_path

from lib.name.name_generator import NameGenerator
from lib.core.character import Character, Classes, Races, Gender
from random import choice


def gen(n):
    for _ in range(10):
        char_class = choice(list(Classes))
        race = choice(list(Races))
        abilities = "..."
        char = Character(
            char_class, race, abilities, "blank name", "blank inventory", "blank image"
        )
        ng = NameGenerator(char, n)
        print(race.value, char.gender.value, ng.generate())


if __name__ == "__main__":
    gen(4)
