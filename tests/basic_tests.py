import pytest

from lib import generator
from lib.core import character


def test_generation():
    assert isinstance(generator.generate(), character.Character)
