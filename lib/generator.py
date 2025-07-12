from lib.core import character
from lib import characteristics
from lib.name import name_generator
import random


def generate():
    char_class = random.choice(list(character.Classes))
    race = random.choice(list(character.Races))
    abilities = characteristics.AbilityChart(char_class, race)
    char = character.Character(
        char_class, race, abilities, "blank name", "blank inventory", "blank image"
    )
    ng = name_generator.NameGenerator(char)
    char.name = ng.generate()
    return char


if __name__ == "__main__":
    generate()
