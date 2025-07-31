from lib.core.character import BaseCharacter, Classes, Gender, Races
from lib.character import Character
from lib import characteristics
from lib.name import name_generator
import random


def generate() -> BaseCharacter:
    gender = random.choice(list(Gender))
    char_class = random.choice(list(Classes))
    race = random.choice(list(Races))
    abilities = characteristics.AbilityChart(char_class, race)
    char = Character(
        char_class=char_class,
        race=race,
        gender=gender,
        abilities=abilities,
        name=None,
        inventory=None,
        image=None,
    )
    ng = name_generator.NameGenerator(race, gender)
    char.name = ng.generate()
    return char


if __name__ == "__main__":
    generate()
