import global_helper
import re_helper
import game_parser
import common_functions

class AddGameService:
    def __init__(self):
        pass

    @classmethod
    def check_game_existence(cls, url):
        for game in global_helper.GlobalHelper.table_container.service.games:
            if game.url == url or game.url[:-1] == url:
                raise Exception("Данная игра уже добавлена в таблицу!")
            
    def append_match(self, input):
        url = input.value
        input.value = ""
        re_helper.RegularExpressionHelper.check_game_url(url)
        self.check_game_existence(url)
        game = game_parser.GameParser.parse_game(url)
        game.row_index = len(global_helper.GlobalHelper.table_container.service.games)
        global_helper.GlobalHelper.table_container.service.games.append(game)
        common_functions.show_snack_bar(f"Игра {game.title}, {game.date} добавлена!")
        global_helper.GlobalHelper.table_container.service.update_page(
            global_helper.GlobalHelper.table_container.main_container,
            global_helper.GlobalHelper.table_container.previous_button,
            global_helper.GlobalHelper.table_container.next_button,
        )