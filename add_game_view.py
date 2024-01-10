import flet
import constants

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
                                                   ), on_click=None),
                                                   )