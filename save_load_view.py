import flet
import global_helper
import save_load_service

class SaveLoadView:
    def __init__(self):
        self.service = save_load_service.SaveLoadService()
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
                                                   ), on_click=lambda _: global_helper.GlobalHelper.file_picker_save.save_file(
                                                       dialog_title="Сохранение сета", file_name="save.txt", allowed_extensions=['txt']
                                                   ))
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
                                                   ), on_click=lambda _: 
                                                   global_helper.GlobalHelper.file_picker_load.pick_files(allowed_extensions=['txt']))
        self.buttons_row = flet.Row(alignment=flet.MainAxisAlignment.CENTER, spacing=200, controls=[self.save_button, self.load_button])
        self.service.check_save_button_availability(self.save_button)