import init_path
import os

from lib.name.name_generator import NameGenerator
from lib.core.character import Races, Gender
from random import choice


def gen(n: int) -> None:
    for _ in range(10):
        race = choice(list(Races))
        gender = choice(list(Gender))
        ng = NameGenerator(race, gender, n)
        print(race.value, gender.value, ng.generate())


if __name__ == "__main__":
    gen(4)
