
class GlobalHelper:
    page = None
    table_container = None
    save_load_component = None
    details_component = None

    @classmethod
    def clear_details(cls):
        cls.details_component.details_list.controls.clear()
        cls.details_component.cur_index = -1
