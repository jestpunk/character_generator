from typing import Optional, Dict

from lib.core import character
from lib.items import Inventory
from lib.characteristics import AbilityChart


class Character(character.BaseCharacter):

    def __init__(
        self,
        *,
        char_class: character.Classes,
        race: character.Races,
        gender: character.Gender,
        abilities: AbilityChart,
        name: Optional[str] = None,
        inventory: Optional[Inventory] = None,
        image: Optional[str] = None,
    ):
        self.char_class = char_class
        self.race = race
        self.gender = gender
        self.abilities = abilities
        self.name = name
        self.inventory = inventory
        self.image = image

    def __str__(self):
        return (
            f"Character\n"
            f"Name: {self.name}\n"
            f"Gender: {self.gender.value}\n"
            f"Class: {self.char_class.value}\n"
            f"Race: {self.race.value}\n\n"
            f"Abilities: {self.abilities}\n"
            f"Portrait: {self.image}\n"
        )
