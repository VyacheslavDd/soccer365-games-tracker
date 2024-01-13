import flet
import global_helper
import constants
import sorter
from threading import Timer
import common_functions

class TableService:
    def __init__(self, games):
        self.page = 1
        self.games = games
    
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

    def show_details(self, e, index, auto_update=False):
        try:
            global_helper.GlobalHelper.details_component.details_list.controls.clear()
            global_helper.GlobalHelper.details_component.details_list.controls.append(flet.Text(f"События матча {self.games[index].title} ({self.games[index].date}):", weight=flet.FontWeight.BOLD))
            global_helper.GlobalHelper.details_component.cur_index = index
            for record in self.games[index].details:
                global_helper.GlobalHelper.details_component.details_list.controls.append(flet.Text(record))
            if not auto_update:
                 self.update_page(
            global_helper.GlobalHelper.table_container.main_container,
            global_helper.GlobalHelper.table_container.previous_button,
            global_helper.GlobalHelper.table_container.next_button,
        )
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
        self.update_page(
            global_helper.GlobalHelper.table_container.main_container,
            global_helper.GlobalHelper.table_container.previous_button,
            global_helper.GlobalHelper.table_container.next_button,
        )

    def cannot_decrease_page(self):
        return True if self.page == 1 else False

    def cannot_increase_page(self):
        return True if self.page * constants.ENTITIES_PER_PAGE >= len(self.games) else False

    def fill_table(self):
        start = (self.page - 1) * constants.ENTITIES_PER_PAGE
        self.table = self.create_table(sorted(self.games[start:start + constants.ENTITIES_PER_PAGE], key=sorter.GameSorter.sort_by_date))
        if global_helper.GlobalHelper.save_load_component is not None:
            global_helper.GlobalHelper.save_load_component.service.check_save_button_availability(global_helper.GlobalHelper.save_load_component.save_button)

    def update_page(self, container, prev_button, next_button, start_new_timer=False):
        self.fill_table()
        container.content = self.table
        prev_button.disabled = self.cannot_decrease_page()
        next_button.disabled = self.cannot_increase_page()
        if global_helper.GlobalHelper.details_component.cur_index != -1:
            self.show_details(None, global_helper.GlobalHelper.details_component.cur_index, auto_update=True)
        global_helper.GlobalHelper.page.update()
        if start_new_timer:
            Timer(constants.TABLE_UPDATE_TIME, self.update_page, [container, prev_button, next_button, True]).start()

    def change_page(self, increase_by):
        self.page += increase_by
        self.update_page(
            global_helper.GlobalHelper.table_container.main_container,
            global_helper.GlobalHelper.table_container.previous_button,
            global_helper.GlobalHelper.table_container.next_button,
        )
        

    