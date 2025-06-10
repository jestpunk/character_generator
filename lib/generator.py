import core.character, characteristics

char_class = core.character.classes.pop()
race = core.character.races.pop()
abilities = characteristics.Abilities(char_class, race)
char = core.character.Character(char_class, race, abilities, 'blank name', 'blank inventory', 'blank image')
print(char)