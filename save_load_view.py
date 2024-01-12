import flet
import set_loader, set_saver, common_functions

class SaveLoadView:

    def load(self, e):
        try:
            for game in self.table_container.games:
                game.timer.cancel()
            data = set_loader.Loader.load_set()
            self.table_container.games = data
            self.table_container.page = 1
            common_functions.show_snack_bar(self.page_ref, "Данные загружены!")
            self.table_container.update_page()
        except Exception as exc:
            common_functions.show_snack_bar(self.page_ref, exc)

    def save(self, e):
        try:
            set_saver.Saver.save_set(self.table_container.games)
            common_functions.show_snack_bar(self.page_ref, "Данные сохранены!")
        except Exception as exc:
            common_functions.show_snack_bar(self.page_ref, exc)

    def check_save_button_availability(self):
        if len(self.table_container.games) > 0:
            self.save_button.disabled = False
        else:
            self.save_button.disabled = True
        self.page_ref.update()

    def __init__(self, page, table_container):
        self.page_ref = page
        self.table_container = table_container
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
                                                   ), on_click=self.save)
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
                                                   ), on_click=self.load)
        self.buttons_row = flet.Row(alignment=flet.MainAxisAlignment.CENTER, spacing=200, controls=[self.save_button, self.load_button])
        self.check_save_button_availability()