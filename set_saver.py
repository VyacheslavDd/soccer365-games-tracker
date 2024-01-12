import constants
import os

class Saver:
    @classmethod
    def save_set(cls, games_list):
        if not os.path.exists(constants.SAVE_PATH):
            os.mkdir(constants.SAVE_PATH)
        with open(os.path.join(constants.SAVE_PATH, constants.SAVE_FILE_TITLE), 'w', encoding='utf-8') as save:
            for game in games_list:
                data_row = f'"{game.row_index + 1}" "{game.date}" "{game.title}" "{game.status}" "{game.score}" "{game.url}"\n'
                save.write(data_row)
        