import flet
import constants
from threading import Timer
import table_service

class TableContainer:
    def __init__(self, data):
        self.service = table_service.TableService(data)
        self.main_container = flet.Container(margin=flet.margin.only(bottom=15))
        self.main_container.alignment = flet.alignment.center
        self.service.fill_table()
        self.main_container.content = self.service.table
        self.button_container = flet.Container(margin=flet.margin.only(bottom=50), alignment=flet.alignment.center)
        self.previous_button = flet.ElevatedButton("<< Назад", disabled=self.service.cannot_decrease_page(),
                                              on_click=lambda x: self.service.change_page(increase_by=-1))
        self.next_button = flet.ElevatedButton("Вперёд >>",
                                           disabled=self.service.cannot_increase_page(),
                                           on_click=lambda x: self.service.change_page(increase_by=1))
        self.pagination_row = flet.Row(spacing=50, alignment=flet.MainAxisAlignment.CENTER, controls=[self.previous_button, self.next_button])
        self.button_container.content = self.pagination_row
        Timer(constants.TABLE_UPDATE_TIME, self.service.update_page, [self.main_container, self.previous_button, self.next_button, True]).start()