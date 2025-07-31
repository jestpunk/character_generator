import random
from enum import Enum
from collections import defaultdict
from lib.core.character import Classes, Races

BASE_ABILITY_SCORE = 6
BASE_DISTR_SCORE = 36


class Abilities(Enum):
    STRENGTH = "Strength"
    DEXTERITY = "Dexterity"
    CONSTITUTION = "Constitution"
    INTELLIGENCE = "Intelligence"
    WISDOM = "Wisdom"
    CHARISMA = "Charisma"


classes_ability_scores = {
    Classes.BARBARIAN: {Abilities.STRENGTH: 2},
    Classes.BARD: {Abilities.CHARISMA: 2},
    Classes.CLERIC: {Abilities.WISDOM: 2},
    Classes.DRUID: {Abilities.WISDOM: 2},
    Classes.FIGHTER: {Abilities.STRENGTH: 1, Abilities.DEXTERITY: 1},
    Classes.MONK: {Abilities.DEXTERITY: 1, Abilities.WISDOM: 1},
    Classes.PALADIN: {Abilities.STRENGTH: 1, Abilities.CHARISMA: 1},
    Classes.RANGER: {Abilities.DEXTERITY: 1, Abilities.WISDOM: 1},
    Classes.ROGUE: {Abilities.DEXTERITY: 2},
    Classes.SORCERER: {Abilities.CHARISMA: 2},
    Classes.WARLOCK: {Abilities.CHARISMA: 2},
    Classes.WIZARD: {Abilities.INTELLIGENCE: 2},
}

races_ability_scores = {
    # Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma
    Races.DWARF: {Abilities.STRENGTH: 1, Abilities.CONSTITUTION: 2},
    Races.ELF: {Abilities.DEXTERITY: 2, Abilities.WISDOM: 1},
    Races.HALFLING: {Abilities.DEXTERITY: 2, Abilities.CHARISMA: 1},
    Races.HUMAN: {
        Abilities.STRENGTH: 1,
        Abilities.CONSTITUTION: 1,
        Abilities.INTELLIGENCE: 1,
    },
    Races.DRAGONBORN: {Abilities.STRENGTH: 2, Abilities.INTELLIGENCE: 1},
    Races.HALF_ELF: {Abilities.WISDOM: 1, Abilities.CHARISMA: 2},
    Races.HALF_ORC: {Abilities.STRENGTH: 2, Abilities.CONSTITUTION: 1},
    Races.TIEFLING: {Abilities.INTELLIGENCE: 1, Abilities.CHARISMA: 2},
}


class AbilityChart:
    def __init__(self, char_class: Classes, race: Races):
        self.abilities: dict = defaultdict(int)
        self.char_class = char_class
        self.race = race
        self.assign()

    def __str__(self):
        output = "\n"
        for ability in Abilities:
            output += ability.value + ": " + str(self.abilities[ability]) + "\n"
        return output

    def assign(self, score: int = BASE_DISTR_SCORE) -> None:
        for ability in Abilities:
            self.abilities[ability] += BASE_ABILITY_SCORE
        for i in range(score):
            ability = random.choice(list(Abilities))
            self.abilities[ability] += 1
        self.adjust(races_ability_scores[self.race])
        self.adjust(classes_ability_scores[self.char_class])

    def adjust(self, scores: dict) -> None:
        for ability in scores:
            if ability in self.abilities.keys():
                self.abilities[ability] += scores[ability]
