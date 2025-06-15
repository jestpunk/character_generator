"""
import pytest
import init_path
import random
import numpy as np

from lib.core import BaseItem, BaseCharacter, BasePortrait, BaseCharacteristic
from lib import generator
from lib.portrait import drawer

def test_character() -> None:
    character : BaseCharacter = generator.generate()

    assert isinstance(character.name, str)
    assert len(character.name) > 0
    assert isinstance(character.item, BaseItem)

    for characteristic in character.characteristics:
        assert isinstance(characteristic, BaseCharacteristic)

    assert isinstance(character.portrait, np.array)
"""

import pytest

from lib import generator
from lib.core import character


def test_generation():
    assert isinstance(generator.generate(), character.Character)
