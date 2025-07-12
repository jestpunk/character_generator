import json
import random

# filename_in = "elf_names.txt"
# filename_out = "elf_male_names_data.json"

RELATIVE_PATH_TO_DATA_FOLDER = "data/"


class NameGenerator:
    def __init__(self, character, n=3):
        self.race = character.race
        self.gender = character.gender
        self.n = n

    def _gather_data(self, txt_filename):
        names_data = {}
        try:
            file_in = open(txt_filename)
        except FileNotFoundError:
            print(f"Source file {txt_filename} not found")
            exit()

        for line in file_in:
            line = "_" * (self.n - 1) + line
            for i in range(self.n - 1, len(line)):
                window = line[i - self.n + 1 : i].lower()
                letter = line[i].lower()
                if window not in names_data:
                    names_data[window] = {letter: 1}
                elif letter not in names_data[window]:
                    names_data[window][letter] = 1
                else:
                    names_data[window][letter] += 1

        file_in.close
        self.names_data = names_data

    def _get_txt_filename(self):  # Логично здесь использовать match
        txt_filename = (
            str(self.race.value).lower() + "_" + str(self.gender.value).lower() + ".txt"
        )
        txt_filename = RELATIVE_PATH_TO_DATA_FOLDER + txt_filename
        return txt_filename

    def _get_json_filename(self):
        json_filename = (
            str(self.race.value).lower()
            + "_"
            + str(self.gender.value).lower()
            + "_"
            + str(self.n)
            + ".json"
        )
        json_filename = RELATIVE_PATH_TO_DATA_FOLDER + json_filename
        return json_filename

    def _save_to_json(
        self, json_filename
    ):  # Класть в папку data (относительным путём, чтобы можно было запустить на другом компьютере)
        file_out = open(json_filename, "w")
        json_dump = json.dumps(self.names_data, indent=4)
        file_out.write(json_dump)
        file_out.close()

    def generate(self) -> str:  # Дропаем ошибку если не нашли файл
        json_filename = self._get_json_filename()
        try:
            file_in = open(json_filename)
        except FileNotFoundError:
            txt_filename = self._get_txt_filename()
            self._gather_data(txt_filename)
            self._save_to_json(json_filename)
            file_in = open(json_filename, "r")
        self.names_data = json.load(file_in)
        name = ""
        window = "_" * (self.n - 1)
        symb = random.sample(
            list(self.names_data[window].keys()),
            k=1,
            counts=list(self.names_data[window].values()),
        )
        while symb[0] != "\n":
            name += symb[0]
            window = window[1::] + symb[0]
            symb = random.sample(
                list(self.names_data[window].keys()),
                k=1,
                counts=list(self.names_data[window].values()),
            )
        file_in.close()
        return name.capitalize()
