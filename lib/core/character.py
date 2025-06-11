# Character, Abilities, Class, Race, Name, Items, Image

classes = {
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    "Warlock",
    "Wizard",
}
races = {
    "Dwarf",
    "Elf",
    "Halfling",
    "Human",
    "Dragonborn",
    "Half-Elf",
    "Half-Orc",
    "Tiefling",
}


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
            f"Class: {self.char_class}\n"
            f"Race: {self.race}\n"
            f"Abilities: {self.abilities}"
        )
