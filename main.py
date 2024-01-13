import flet
import table_view, add_game_view, save_load_view, global_helper, game_details_view


def define_page_settings(page):
    page.title = "Soccer365 games tracker"
    page.scroll = flet.ScrollMode.ADAPTIVE

def app(page: flet.Page):
    define_page_settings(page)
    global_helper.GlobalHelper.page = page
    table_container = table_view.TableContainer(list())
    global_helper.GlobalHelper.table_container = table_container
    add_game_component = add_game_view.AddView()
    save_load_component = save_load_view.SaveLoadView()
    global_helper.GlobalHelper.save_load_component = save_load_component
    details_view_component = game_details_view.DetailsView()
    global_helper.GlobalHelper.details_component = details_view_component
    page.add(table_container.main_container)
    page.add(table_container.button_container)
    page.add(add_game_component.input_container)
    page.add(add_game_component.add_button_container)
    page.add(save_load_component.buttons_row)
    page.add(details_view_component.list_container)
    page.update()

flet.app(target=app, view=flet.AppView.WEB_BROWSER)
