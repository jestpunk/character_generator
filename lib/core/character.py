# Character, Abilities, Class, Race, Name, Items, Image
from enum import Enum


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


class Races(Enum):
    DWARF = "Dwarf"
    ELF = "Elf"
    HALFLING = "Halfling"
    HUMAN = "Human"
    DRAGONBORN = "Dragonborn"
    HALF_ELF = "Half-Elf"
    HALF_ORC = "Half-Orc"
    TIEFLING = "Tiefling"


class Character:

    def __init__(self, char_class, race, abilities, name, inventory, image):
        self.char_class = char_class
        self.race = race
        self.abilities = abilities
        self.name = name
        self.inventory = inventory
        self.image = image

    def __str__(self):
        return (
            f"Character\n"
            f"Name: {self.name}\n"
            f"Class: {self.char_class.value}\n"
            f"Race: {self.race.value}\n\n"
            f"Abilities: {self.abilities}\n"
            f"Portrait: {self.image}\n"
        )
