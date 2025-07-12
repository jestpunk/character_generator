import pytest

from lib.core import character
from lib.name import name_generator
from random import choice

@pytest.mark.parametrize("race", list(character.Races))
@pytest.mark.parametrize("gender", list(character.Gender))
def test_name_generation(race, gender):
    for n in range(2, 10):
        char_class = choice(list(character.Classes))
        abilities = "..."
        char = character.Character(
            char_class, race, abilities, "blank name", "blank inventory", "blank image"
        )
        char.gender = gender
        ng = name_generator.NameGenerator(char, n)
        assert isinstance(ng.generate(), str)
