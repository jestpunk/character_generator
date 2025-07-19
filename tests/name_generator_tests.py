import pytest
import os

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
            char_class=char_class,
            race=race,
            gender=gender,
            abilities=abilities,
            name="blank name",
            inventory="blank inventory",
            image="blank image",
        )
        char.gender = gender
        ng = name_generator.NameGenerator(char, n)
        assert isinstance(ng.generate(), str)


def test_txt_files():
    files_list = os.listdir(name_generator.RELATIVE_PATH_TO_DATA_FOLDER)
    for file in files_list:
        if file.endswith(".txt"):
            race, gender = file[:-4].split("_")
            assert race.capitalize() in [
                r.value for r in character.Races
            ] and gender.capitalize() in [g.value for g in character.Gender]
