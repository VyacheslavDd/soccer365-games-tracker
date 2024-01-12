import flet
import constants
from threading import Timer

class TableContainer:
    def create_table(self, data):
        table = flet.DataTable(
            border=flet.border.all(2, flet.colors.BLACK),
            horizontal_lines=flet.border.BorderSide(2, flet.colors.BLACK),
            vertical_lines=flet.border.BorderSide(2, flet.colors.BLACK),
            columns=[
                flet.DataColumn(flet.Text("Номер", weight=flet.FontWeight.BOLD)),
                flet.DataColumn(flet.Text("Дата", weight=flet.FontWeight.BOLD)),
                flet.DataColumn(flet.Text("Афиша", weight=flet.FontWeight.BOLD)),
                flet.DataColumn(flet.Text("Статус", weight=flet.FontWeight.BOLD)),
                flet.DataColumn(flet.Text("Счёт", weight=flet.FontWeight.BOLD)),
                flet.DataColumn(flet.Text("Действия", weight=flet.FontWeight.BOLD))
            ],
        )
        rows = []
        for game in data:
            row = flet.DataRow()
            cells = []
            cells.append(flet.DataCell(flet.Text(game.row_index + 1)))
            cells.append(flet.DataCell(flet.Text(game.date)))
            cells.append(flet.DataCell(flet.Text(game.title)))
            cells.append(flet.DataCell(flet.Text(game.status)))
            cells.append(flet.DataCell(flet.Text(game.score)))
            cells.append(flet.DataCell(content=flet.TextButton("Удалить", on_click=lambda e, i=game.row_index: self.remove_entry(e, i))))
            row.cells = cells
            rows.append(row)
        table.rows = rows
        return table
    
    def cannot_decrease_page(self):
        return True if self.page == 1 else False

    def cannot_increase_page(self):
        return True if self.page * constants.ENTITIES_PER_PAGE >= len(self.games) else False

    def remove_entry(self, e, index):
        self.games[index].timer.cancel()
        del self.games[index]
        for game in self.games[index:]:
            game.row_index -= 1
        self.update_page()

    def update_page(self, start_new_timer=False):
        self.fill_table()
        self.main_container.content = self.table
        self.previous_button.disabled = self.cannot_decrease_page()
        self.next_button.disabled = self.cannot_increase_page()
        self.page_ref.update()
        if start_new_timer:
            Timer(constants.TABLE_UPDATE_TIME, self.update_page, [True]).start()

    def change_page(self, increase_by):
        self.page += increase_by
        self.update_page()

    def create_pagination_buttons(self):
        self.previous_button = flet.ElevatedButton("<< Назад", disabled=self.cannot_decrease_page(),
                                              on_click=lambda x: self.change_page(increase_by=-1))
        self.next_button = flet.ElevatedButton("Вперёд >>",
                                           disabled=self.cannot_increase_page(),
                                           on_click=lambda x: self.change_page(increase_by=1))

    def fill_table(self):
        start = (self.page - 1) * constants.ENTITIES_PER_PAGE
        self.table = self.create_table(self.games[start:start + constants.ENTITIES_PER_PAGE])
        if self.save_load_view_ref is not None:
            self.save_load_view_ref.check_save_button_availability()

    def __init__(self, page, data):
        self.page_ref = page
        self.save_load_view_ref = None
        self.main_container = flet.Container(margin=flet.margin.only(bottom=15))
        self.main_container.alignment = flet.alignment.center
        self.games = data
        self.page = 1
        self.fill_table()
        self.main_container.content = self.table
        self.button_container = flet.Container(margin=flet.margin.only(bottom=50), alignment=flet.alignment.center)
        self.create_pagination_buttons()
        self.pagination_row = flet.Row(spacing=50, alignment=flet.MainAxisAlignment.CENTER, controls=[self.previous_button, self.next_button])
        self.button_container.content = self.pagination_row
        Timer(constants.TABLE_UPDATE_TIME, self.update_page, [True]).start()