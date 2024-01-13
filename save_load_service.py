import set_loader, set_saver, common_functions
import global_helper



class SaveLoadService:
    def __init__(self):
        pass

    def load(self, e):
        if e.files is None:
            return
        try:
            data = set_loader.Loader.load_set(e.files[0].path)
            for game in global_helper.GlobalHelper.table_container.games:
                if game.timer is not None:
                    game.timer.cancel()
            global_helper.GlobalHelper.table_container.games = data
            global_helper.GlobalHelper.table_container.page = 1
            global_helper.GlobalHelper.clear_details()
            common_functions.show_snack_bar("Данные загружены!")
            global_helper.GlobalHelper.table_container.update_page()
        except Exception as exc:
            common_functions.show_snack_bar(exc)

    def save(self, e):
        if e.path is None:
            return
        try:
            set_saver.Saver.save_set(e.path, global_helper.GlobalHelper.table_container.games)
            common_functions.show_snack_bar("Данные сохранены!")
        except Exception as exc:
            common_functions.show_snack_bar(exc)

    @classmethod
    def check_save_button_availability(cls, button):
        if len(global_helper.GlobalHelper.table_container.games) > 0:
            button.disabled = False
        else:
            button.disabled = True
        global_helper.GlobalHelper.page.update()