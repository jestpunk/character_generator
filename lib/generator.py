from lib.core import character
from lib import characteristics


def generate():
    char_class = character.classes.pop()
    race = character.races.pop()
    abilities = characteristics.Abilities(char_class, race)
    char = character.Character(
        char_class, race, abilities, "blank name", "blank inventory", "blank image"
    )
    print(char)


if __name__ == "__main__":
    generate()
