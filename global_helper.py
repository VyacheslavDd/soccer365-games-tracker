import table_view, add_game_view, save_load_view, game_details_view
import flet

class GlobalHelper:
    page = None
    table_container = None
    save_load_component = None
    details_component = None
    file_picker_load = None
    file_picker_save = None

    @classmethod
    def clear_details(cls):
        cls.details_component.details_list.controls.clear()
        cls.details_component.cur_index = -1
    
    @classmethod
    def add_table_container(cls):
        cls.table_container = table_view.TableContainer(list())
        cls.page.add(cls.table_container.main_container)
        cls.page.add(cls.table_container.button_container)
    
    @classmethod
    def add_add_view(cls):
        add_game_component = add_game_view.AddView()
        cls.page.add(add_game_component.input_container)
        cls.page.add(add_game_component.add_button_container)

    @classmethod
    def add_save_load_component(cls):
        cls.save_load_component = save_load_view.SaveLoadView()
        cls.page.add(cls.save_load_component.buttons_row)

    @classmethod
    def add_details_component(cls):
        cls.details_component = game_details_view.DetailsView()
        cls.page.add(cls.details_component.list_container)

    @classmethod
    def add_file_pickers(cls):
        cls.file_picker_load = flet.FilePicker(on_result=cls.save_load_component.service.load)
        cls.page.overlay.append(cls.file_picker_load)
        cls.file_picker_save = flet.FilePicker(on_result=cls.save_load_component.service.save)
        cls.page.overlay.append(cls.file_picker_save)
