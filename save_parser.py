import flet
import constants
import match

class Parser:
    @classmethod
    def parse_save(cls, path):
        with open(path, 'r', encoding="utf-8") as file:
            data = file.readlines()
        rows = []
        game_objects = []
        for line in data:
            cells_data = line.strip().split('"')
            cells_data[2:] = cells_data[2].split()
            if len(cells_data) != constants.TABLE_COLS + 1:
                return [list(), list()]
            cells = []
            for cell in cells_data[:-1]:
                cells.append(flet.DataCell(flet.Text(cell.strip())))
            row = flet.DataRow(cells=cells)
            rows.append(row)
            game_class = match.Match(cells_data[-1], cells_data[0], cells_data[1], cells_data[2], cells_data[3])
            game_objects.append(game_class)
        return rows, game_objects
