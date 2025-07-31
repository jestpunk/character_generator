import pytest

from lib import generator
from lib import character


def test_generation():
    assert isinstance(generator.generate(), character.Character)
