import flet
import common.constants as constants
import entities.match as match
import services.helpers.re_helper as re_helper

class Parser:
    @classmethod
    def parse_save(cls, path):
        with open(path, 'r', encoding="utf-8") as file:
            data = file.readlines()
        game_objects = []
        for line in data:
            cells_data = re_helper.RegularExpressionHelper.split_data_row(line)
            if len(cells_data) != constants.TABLE_COLS + 1:
                raise Exception("Некорректные данные.")
            game_class = match.Match(int(cells_data[0]) - 1, cells_data[-1], cells_data[1], cells_data[2], cells_data[3], cells_data[4])
            game_class.update_data(manual_update=True)
            game_objects.append(game_class)
        return game_objects
