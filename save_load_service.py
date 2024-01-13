import set_loader, set_saver, common_functions
import global_helper
import re_helper



class SaveLoadService:
    def __init__(self):
        pass

    def load(self, e):
        if e.files is None:
            return
        try:
            data = set_loader.Loader.load_set(e.files[0].path)
            for game in global_helper.GlobalHelper.table_container.service.games:
                if game.timer is not None:
                    game.timer.cancel()
            global_helper.GlobalHelper.table_container.service.games = [game for game in data if re_helper.RegularExpressionHelper.check_game_url(game.url, raise_exception=False)]
            global_helper.GlobalHelper.table_container.service.page = 1
            global_helper.GlobalHelper.clear_details()
            common_functions.show_snack_bar("Данные загружены!")
            global_helper.GlobalHelper.table_container.service.update_page(
            global_helper.GlobalHelper.table_container.main_container,
            global_helper.GlobalHelper.table_container.previous_button,
            global_helper.GlobalHelper.table_container.next_button,
        )
        except Exception as exc:
            common_functions.show_snack_bar(exc)

    def save(self, e):
        if e.path is None:
            return
        try:
            set_saver.Saver.save_set(e.path, global_helper.GlobalHelper.table_container.service.games)
            common_functions.show_snack_bar("Данные сохранены!")
        except Exception as exc:
            common_functions.show_snack_bar(exc)

    @classmethod
    def check_save_button_availability(cls, button):
        if len(global_helper.GlobalHelper.table_container.service.games) > 0:
            button.disabled = False
        else:
            button.disabled = True
        global_helper.GlobalHelper.page.update()