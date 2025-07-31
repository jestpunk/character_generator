import pytest
import os

from lib.core import character
from lib.name import name_generator


@pytest.mark.parametrize("race", list(character.Races))
@pytest.mark.parametrize("gender", list(character.Gender))
def test_name_generation(race, gender):
    for n in range(2, 10):
        ng = name_generator.NameGenerator(race, gender, n)
        assert isinstance(ng.generate(), str)


def test_txt_files():
    files_list = os.listdir(name_generator.RELATIVE_PATH_TO_DATA_FOLDER)
    for file in files_list:
        if file.endswith(".txt"):
            race, gender = file[:-4].split("_")
            assert race.capitalize() in [
                r.value for r in character.Races
            ] and gender.capitalize() in [g.value for g in character.Gender]
