import services.helpers.global_helper as global_helper
import services.helpers.re_helper as re_helper
import services.parsers.site_parser as site_parser
import common.common_functions as common_functions

class AddGameService:
    def __init__(self):
        pass

    @classmethod
    def check_game_existence(cls, url):
        for game in global_helper.GlobalHelper.table_container.service.games:
            if game.url == url or game.url[:-1] == url:
                raise Exception("Данная игра уже добавлена в таблицу!")
            
    def append_today_top_matches(self, e):
        game_links = site_parser.SiteParser.parse_main_page_top_games()
        if game_links is None or not len(game_links):
            return
        for link in game_links:
            try:
                self.__proceed_url(link)
            except Exception as exc:
                pass

    def __proceed_url(self, url):
        re_helper.RegularExpressionHelper.check_game_url(url)
        self.check_game_existence(url)
        game = site_parser.SiteParser.parse_game(url)
        game.row_index = len(global_helper.GlobalHelper.table_container.service.games)
        global_helper.GlobalHelper.table_container.service.games.append(game)
        common_functions.show_snack_bar(f"Игра {game.title}, {game.date} добавлена!")
        global_helper.GlobalHelper.table_container.service.update_page(
            global_helper.GlobalHelper.table_container.main_container,
            global_helper.GlobalHelper.table_container.previous_button,
            global_helper.GlobalHelper.table_container.next_button,
        )

    def append_match(self, e, input):
        try:
            url = input.value
            input.value = ""
            self.__proceed_url(url)
        except Exception as exc:
            common_functions.show_snack_bar(exc)