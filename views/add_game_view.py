import flet
import services.view_services.add_game_service as add_game_service

class AddView:
    def __init__(self):
        self.service = add_game_service.AddGameService()
        self.input_container = flet.Container(margin=flet.margin.only(bottom=25))
        self.url_input_field = flet.TextField(label="Url игры", hint_text="https://soccer365.ru/games/2020343/", width=500)
        self.input_row = flet.Row(alignment=flet.MainAxisAlignment.CENTER, controls=[self.url_input_field])
        self.input_container.content = self.input_row
        self.btn_row = flet.Row(alignment=flet.MainAxisAlignment.CENTER, spacing=180)
        add_game_button = flet.ElevatedButton("Добавить матч", style=flet.ButtonStyle(
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
                                                   ), on_click=lambda e, input=self.url_input_field: self.service.append_match(e, input))
        add_games_button = flet.ElevatedButton("Добавить матчи за сегодня", style=flet.ButtonStyle(
                                                       color={
                                                           flet.MaterialState.DEFAULT: flet.colors.BLACK,
                                                           
                                                       },
                                                       bgcolor= {
                                                           flet.MaterialState.DEFAULT: flet.colors.GREEN_200,
                                                           flet.MaterialState.HOVERED: flet.colors.GREEN_400
                                                       },
                                                       padding={
                                                           flet.MaterialState.DEFAULT: 25
                                                       }
                                                   ), on_click=self.service.append_today_top_matches)
        self.btn_row.controls = [add_game_button, add_games_button]
        self.add_button_container = flet.Container(margin=flet.margin.only(bottom=85), alignment=flet.alignment.center,
                                                   content=self.btn_row)
