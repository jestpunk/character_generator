from lib.core import character
from lib import characteristics
from lib.name import name_generator
import random


def generate() -> character.Character:
    gender = random.choice(list(character.Gender))
    char_class = random.choice(list(character.Classes))
    race = random.choice(list(character.Races))
    abilities = characteristics.AbilityChart(char_class, race)
    char = character.Character(
        char_class=char_class,
        race=race,
        gender=gender,
        abilities=abilities,
        name=None,
        inventory=None,
        image=None,
    )
    ng = name_generator.NameGenerator(char)
    char.name = ng.generate()
    return char


if __name__ == "__main__":
    generate()
