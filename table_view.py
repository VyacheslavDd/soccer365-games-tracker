import flet
import constants
from threading import Timer
import global_helper
import common_functions
import sorter
import table_service

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
                flet.DataColumn(flet.Text("", weight=flet.FontWeight.BOLD)),
                flet.DataColumn(flet.Text("", weight=flet.FontWeight.BOLD))
            ],
        )
        rows = []
        counter = 1
        for game in data:
            row = flet.DataRow()
            cells = []
            cells.append(flet.DataCell(flet.Text(counter)))
            cells.append(flet.DataCell(flet.Text(game.date)))
            cells.append(flet.DataCell(flet.Text(game.title)))
            cells.append(flet.DataCell(flet.Text(game.status)))
            cells.append(flet.DataCell(flet.Text(game.score)))
            cells.append(flet.DataCell(content=flet.TextButton("Детали матча", on_click=lambda e, i=game.row_index: self.show_details(e, i))))
            cells.append(flet.DataCell(content=flet.TextButton("Удалить", on_click=lambda e, i=game.row_index: self.remove_entry(e, i))))
            row.cells = cells
            rows.append(row)
            counter += 1
        table.rows = rows
        return table
    
    def cannot_decrease_page(self):
        return True if self.page == 1 else False

    def cannot_increase_page(self):
        return True if self.page * constants.ENTITIES_PER_PAGE >= len(self.games) else False

    def show_details(self, e, index, auto_update=False):
        try:
            global_helper.GlobalHelper.details_component.details_list.controls.clear()
            global_helper.GlobalHelper.details_component.details_list.controls.append(flet.Text(f"События матча {self.games[index].title} ({self.games[index].date}):", weight=flet.FontWeight.BOLD))
            global_helper.GlobalHelper.details_component.cur_index = index
            for record in self.games[index].details:
                global_helper.GlobalHelper.details_component.details_list.controls.append(flet.Text(record))
            if not auto_update:
                self.update_page()
        except:
            common_functions.show_snack_bar("Ошибка в обновлении событий матча!")

    def remove_entry(self, e, index):
        if global_helper.GlobalHelper.details_component.cur_index == index:
            global_helper.GlobalHelper.clear_details()
        if self.games[index].timer is not None:
            self.games[index].timer.cancel()
        del self.games[index]
        for game in self.games[index:]:
            game.row_index -= 1
        if global_helper.GlobalHelper.details_component.cur_index >= index:
            global_helper.GlobalHelper.details_component.cur_index -= 1
        self.update_page()

    def update_page(self, start_new_timer=False):
        self.fill_table()
        self.main_container.content = self.table
        self.previous_button.disabled = self.cannot_decrease_page()
        self.next_button.disabled = self.cannot_increase_page()
        if global_helper.GlobalHelper.details_component.cur_index != -1:
            self.show_details(None, global_helper.GlobalHelper.details_component.cur_index, auto_update=True)
        global_helper.GlobalHelper.page.update()
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
        self.table = self.create_table(sorted(self.games[start:start + constants.ENTITIES_PER_PAGE], key=sorter.GameSorter.sort_by_date))
        if global_helper.GlobalHelper.save_load_component is not None:
            global_helper.GlobalHelper.save_load_component.service.check_save_button_availability(global_helper.GlobalHelper.save_load_component.save_button)

    def __init__(self, data):
        self.service = table_service.TableService()
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