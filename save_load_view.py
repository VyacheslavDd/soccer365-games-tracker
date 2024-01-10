import flet

class SaveLoadView:
    def __init__(self):
        self.save_button = flet.ElevatedButton("Сохранить сет матчей", style=flet.ButtonStyle(
                                                       color={
                                                           flet.MaterialState.DEFAULT: flet.colors.BLACK,
                                                           
                                                       },
                                                       bgcolor= {
                                                           flet.MaterialState.DEFAULT: flet.colors.GREEN_400,
                                                           flet.MaterialState.HOVERED: flet.colors.GREEN_700
                                                       },
                                                       padding={
                                                           flet.MaterialState.DEFAULT: 20
                                                       }
                                                   ), on_click=None)
        self.load_button = flet.ElevatedButton("Загрузить сет матчей", style=flet.ButtonStyle(
                                                       color={
                                                           flet.MaterialState.DEFAULT: flet.colors.BLACK,
                                                           
                                                       },
                                                       bgcolor= {
                                                           flet.MaterialState.DEFAULT: flet.colors.ORANGE_600,
                                                           flet.MaterialState.HOVERED: flet.colors.ORANGE_800
                                                       },
                                                       padding={
                                                           flet.MaterialState.DEFAULT: 20
                                                       }
                                                   ), on_click=None)
        self.buttons_row = flet.Row(alignment=flet.MainAxisAlignment.CENTER, spacing=200, controls=[self.save_button, self.load_button])