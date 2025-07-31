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


class BaseCharacter:

    def __init__(self): ...
