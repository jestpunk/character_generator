# Character, Abilities, Class, Race, Name, Items, Image
from enum import Enum
import random
from typing import Optional, Dict

from lib.items import Inventory


class Classes(Enum):
    BARBARIAN = "Barbarian"
    BARD = "Bard"
    CLERIC = "Cleric"
    DRUID = "Druid"
    FIGHTER = "Fighter"
    MONK = "Monk"
    PALADIN = "Paladin"
    RANGER = "Ranger"
    ROGUE = "Rogue"
    SORCERER = "Sorcerer"
    WARLOCK = "Warlock"
    WIZARD = "Wizard"


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"


class Races(Enum):
    DWARF = "Dwarf"
    ELF = "Elf"
    HALFLING = "Halfling"
    HUMAN = "Human"
    DRAGONBORN = "Dragonborn"
    HALF_ELF = "Half-elf"
    HALF_ORC = "Half-orc"
    TIEFLING = "Tiefling"


class Character:

    def __init__(
        self,
        *,
        char_class: Classes,
        race: Races,
        gender: Gender,
        abilities,
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
