import random
base_ability_scores = [15, 14, 13, 12, 10, 8]

classes_ability_scores = {
    'Barbarian': {'Strength': 2},
    'Bard': {'Charisma': 2},
    'Cleric': {'Wisdom': 2},
    'Druid': {'Wisdom': 2},
    'Fighter': {'Strength': 1, 'Dexterity': 1},
    'Monk': {'Dexterity': 1, 'Wisdom': 1},
    'Paladin': {'Strength': 1, 'Charisma': 1},
    'Ranger': {'Dexterity': 1, 'Wisdom': 1},
    'Rogue': {'Dexterity': 2},
    'Sorcerer': {'Charisma': 2},
    'Warlock': {'Charisma': 2},
    'Wizard': {'Intelligence': 2},
}

races_ability_scores = {
    #Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma
    'Dwarf': {'Strength': 1, 'Constitution': 2},
    'Elf': {'Dexterity': 2, 'Wisdom': 1},
    'Halfling': {'Dexterity': 2, 'Charisma': 1},
    'Human': {'Strength': 1, 'Constitution': 1, 'Intelligence': 1},
    'Dragonborn': {'Strength': 2, 'Intelligence': 1},
    'Half-Elf': {'Wisdom': 1, 'Charisma': 2},
    'Half-Orc': {'Strength': 2, 'Constitution': 1},
    'Tiefling': {'Intelligence': 1, 'Charisma': 2},
}

class Abilities:
    def __init__(self, char_class, race):
        self.abilities = {
            'Strength':0,
            'Dexterity':0,
            'Constitution':0,
            'Intelligence':0,
            'Wisdom':0,
            'Charisma':0,
        }
        self.char_class = char_class
        self.race = race
        self.assign()

    def __str__(self):
        return f"Strength: {self.abilities['Strength']}\n" \
            f"Dexterity: {self.abilities['Dexterity']}\n" \
            f"Constitution: {self.abilities['Constitution']}\n" \
            f"Intelligence: {self.abilities['Intelligence']}\n" \
            f"Wisdom: {self.abilities['Wisdom']}\n" \
            f"Charisma: {self.abilities['Charisma']}\n"
    
    def assign(self, scores=base_ability_scores):
        for ability in self.abilities:
            score = random.choice(scores)
            self.abilities[ability] += score
            scores.remove(score)
        self.adjust(races_ability_scores[self.race])
        self.adjust(classes_ability_scores[self.char_class])

    def adjust(self, scores):
        for ability in scores:
            if ability in self.abilities:
                self.abilities[ability] += scores[ability]

    


#test_abs = Abilities('Cleric', 'Dwarf')
#print(test_abs)
#test_abs.assign(base_ability_scores)
#print(test_abs)
#test_abs.adjust(races_ability_scores['Half-Orc'])
#print(test_abs)
#test_abs.adjust(classes_ability_scores['Druid'])
#print(test_abs)

