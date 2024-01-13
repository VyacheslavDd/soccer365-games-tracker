import flet
import constants
import game_parser, re_helper
import common_functions
import global_helper

class AddView:
    def __init__(self):
        self.input_container = flet.Container(margin=flet.margin.only(bottom=25))
        self.url_input_field = flet.TextField(label="Url игры", hint_text="https://soccer365.ru/games/2020343/", width=500)
        self.input_row = flet.Row(alignment=flet.MainAxisAlignment.CENTER, controls=[self.url_input_field])
        self.input_container.content = self.input_row
        self.add_button_container = flet.Container(margin=flet.margin.only(bottom=55), alignment=flet.alignment.center,
                                                   content=flet.ElevatedButton("Добавить матч", style=flet.ButtonStyle(
                                                       color={
                                                           flet.MaterialState.DEFAULT: flet.colors.BLACK,
                                                           
                                                       },
                                                       bgcolor= {
                                                           flet.MaterialState.DEFAULT: flet.colors.YELLOW,
                                                           flet.MaterialState.HOVERED: flet.colors.YELLOW_400
                                                       },
                                                       padding={
                                                           flet.MaterialState.DEFAULT: 25
                                                       }
                                                   ), on_click=self.append_match),
                                                   )

    def check_game_existence(self, url):
        for game in global_helper.GlobalHelper.table_container.games:
            if game.url == url or game.url[:-1] == url:
                raise Exception("Данная игра уже добавлена в таблицу!")

    def append_match(self, e):
        try:
            url = self.url_input_field.value
            self.url_input_field.value = ""
            re_helper.RegularExpressionHelper.check_game_url(url)
            self.check_game_existence(url)
            game = game_parser.GameParser.parse_game(url)
            game.row_index = len(global_helper.GlobalHelper.table_container.games)
            global_helper.GlobalHelper.table_container.games.append(game)
            common_functions.show_snack_bar(f"Игра {game.title}, {game.date} добавлена!")
            global_helper.GlobalHelper.table_container.update_page()
        except Exception as exc:
            common_functions.show_snack_bar(exc)
