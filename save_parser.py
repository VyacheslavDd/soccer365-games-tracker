import flet
import constants
import match

class Parser:
    @classmethod
    def parse_save(cls, path):
        with open(path, 'r', encoding="utf-8") as file:
            data = file.readlines()
        game_objects = []
        for line in data:
            cells_data = line.strip().split('"')
            cells_data = cells_data[0].split() + cells_data[1:]
            cells_data[3:] = cells_data[3].split()
            if len(cells_data) != constants.TABLE_COLS + 1:
                return Exception("Некорректные данные.")
            game_class = match.Match(int(cells_data[0]) - 1, cells_data[-1], cells_data[1], cells_data[2], cells_data[3], cells_data[4])
            game_objects.append(game_class)
        return game_objects
