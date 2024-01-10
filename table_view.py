import flet
import constants

class TableContainer:
    @classmethod
    def __create_table(cls, data):
        table = flet.DataTable(
            border=flet.border.all(2, flet.colors.BLACK),
            horizontal_lines=flet.border.BorderSide(2, flet.colors.BLACK),
            vertical_lines=flet.border.BorderSide(2, flet.colors.BLACK),
            columns=[
                flet.DataColumn(flet.Text("Дата", weight=flet.FontWeight.BOLD)),
                flet.DataColumn(flet.Text("Афиша", weight=flet.FontWeight.BOLD)),
                flet.DataColumn(flet.Text("Статус", weight=flet.FontWeight.BOLD)),
                flet.DataColumn(flet.Text("Счёт", weight=flet.FontWeight.BOLD))
            ],
            rows=data
        )
        return table
    
    def cannot_decrease_page(self):
        return True if self.page == 1 else False

    def cannot_increase_page(self):
        return True if self.page * constants.ENTITIES_PER_PAGE > len(self.data[0]) else False

    def change_page(self, increase_by):
        self.page += increase_by
        self.fill_table()
        self.main_container.content = self.table
        self.previous_button.disabled = self.cannot_decrease_page()
        self.next_button.disabled = self.cannot_increase_page()
        self.page_ref.update()

    def create_pagination_buttons(self):
        self.previous_button = flet.ElevatedButton("<< Назад", disabled=self.cannot_decrease_page(),
                                              on_click=lambda x: self.change_page(increase_by=-1))
        self.next_button = flet.ElevatedButton("Вперёд >>",
                                           disabled=self.cannot_increase_page(),
                                           on_click=lambda x: self.change_page(increase_by=1))

    def fill_table(self):
        start = (self.page - 1) * constants.ENTITIES_PER_PAGE
        self.table = self.__create_table(self.data[0][start:start + constants.ENTITIES_PER_PAGE])

    def __init__(self, page, data):
        self.page_ref = page
        self.main_container = flet.Container(margin=flet.margin.only(bottom=15))
        self.main_container.alignment = flet.alignment.center
        self.data = data
        self.page = 1
        self.fill_table()
        self.main_container.content = self.table
        self.button_container = flet.Container(margin=flet.margin.only(bottom=50), alignment=flet.alignment.center)
        self.create_pagination_buttons()
        self.pagination_row = flet.Row(spacing=50, alignment=flet.MainAxisAlignment.CENTER, controls=[self.previous_button, self.next_button])
        self.button_container.content = self.pagination_row