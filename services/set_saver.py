import common.constants as constants
import os

class Saver:
    @classmethod
    def save_set(cls, path, games_list):
        with open(path, 'w', encoding='utf-8') as save:
            for game in games_list:
                data_row = f'"{game.row_index + 1}" "{game.date}" "{game.title}" "{game.status}" "{game.score}" "{game.url}"\n'
                save.write(data_row)
        