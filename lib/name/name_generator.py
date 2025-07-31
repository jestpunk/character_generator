import json
import random
from lib.core.character import Races, Gender


RELATIVE_PATH_TO_DATA_FOLDER = "data/"


class NameGenerator:
    def __init__(self, race: Races, gender: Gender, n: int = 3):
        self.race = race
        self.gender = gender
        self.n = n

    def _gather_data(self, txt_filename: str) -> None:
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

    @staticmethod
    def _get_txt_filename(race, gender) -> str:
        txt_filename = (
            str(race.value).lower() + "_" + str(gender.value).lower() + ".txt"
        )
        txt_filename = RELATIVE_PATH_TO_DATA_FOLDER + txt_filename
        return txt_filename

    @staticmethod
    def _get_json_filename(race, gender, n: int) -> str:
        json_filename = (
            str(race.value).lower()
            + "_"
            + str(gender.value).lower()
            + "_"
            + str(n)
            + ".json"
        )
        json_filename = RELATIVE_PATH_TO_DATA_FOLDER + json_filename
        return json_filename

    def _save_to_json(self, json_filename: str) -> None:
        file_out = open(json_filename, "w")
        json_dump = json.dumps(self.names_data, indent=4)
        file_out.write(json_dump)
        file_out.close()

    def generate(self) -> str:
        json_filename = NameGenerator._get_json_filename(self.race, self.gender, self.n)
        try:
            file_in = open(json_filename)
        except FileNotFoundError:
            txt_filename = NameGenerator._get_txt_filename(self.race, self.gender)
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
