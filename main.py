import flet
import table_view, add_game_view, save_load_view


def define_page_settings(page):
    page.title = "Soccer365 games tracker"
    page.scroll = flet.ScrollMode.ADAPTIVE

def app(page: flet.Page):
    define_page_settings(page)
    table_container = table_view.TableContainer(page, list())
    add_game_component = add_game_view.AddView()
    save_load_component = save_load_view.SaveLoadView(page, table_container)
    table_container.save_load_view_ref = save_load_component
    page.add(table_container.main_container)
    page.add(table_container.button_container)
    page.add(add_game_component.input_container)
    page.add(add_game_component.add_button_container)
    page.add(save_load_component.buttons_row)
    page.update()

flet.app(target=app, view=flet.AppView.WEB_BROWSER)
