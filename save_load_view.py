import flet
import set_loader, set_saver, common_functions
import global_helper

class SaveLoadView:

    def load(self, e):
        try:
            for game in global_helper.GlobalHelper.table_container.games:
                game.timer.cancel()
            data = set_loader.Loader.load_set()
            global_helper.GlobalHelper.table_container.games = data
            global_helper.GlobalHelper.table_container.page = 1
            global_helper.GlobalHelper.clear_details()
            common_functions.show_snack_bar("Данные загружены!")
            global_helper.GlobalHelper.table_container.update_page()
        except Exception as exc:
            common_functions.show_snack_bar(exc)

    def save(self, e):
        try:
            set_saver.Saver.save_set(global_helper.GlobalHelper.table_container.games)
            common_functions.show_snack_bar("Данные сохранены!")
        except Exception as exc:
            common_functions.show_snack_bar(exc)

    def check_save_button_availability(self):
        if len(global_helper.GlobalHelper.table_container.games) > 0:
            self.save_button.disabled = False
        else:
            self.save_button.disabled = True
        global_helper.GlobalHelper.page.update()

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