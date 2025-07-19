import init_path
import os

from lib.name.name_generator import NameGenerator
from lib.core.character import Character, Classes, Races, Gender
from random import choice


def gen(n: int) -> None:
    for _ in range(10):
        char_class = choice(list(Classes))
        race = choice(list(Races))
        gender = choice(list(Gender))
        abilities = None
        char = Character(
            char_class=char_class,
            race=race,
            gender=gender,
            abilities=abilities,
            name=None,
            inventory=None,
            image=None,
        )
        ng = NameGenerator(char, n)
        print(race.value, char.gender.value, ng.generate())


if __name__ == "__main__":
    gen(4)
