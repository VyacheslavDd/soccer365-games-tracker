import flet
from global_helper import GlobalHelper


def define_page_settings(page):
    page.title = "Soccer365 games tracker"
    page.scroll = flet.ScrollMode.ADAPTIVE

def app(page: flet.Page):
    define_page_settings(page)
    GlobalHelper.page = page
    GlobalHelper.add_table_container()
    GlobalHelper.add_add_view()
    GlobalHelper.add_save_load_component()
    GlobalHelper.add_details_component()
    GlobalHelper.add_file_pickers()
    page.update()

flet.app(target=app)
