import flet
import global_helper

def show_snack_bar(text):
    if global_helper.GlobalHelper.page.snack_bar is None:
        global_helper.GlobalHelper.page.snack_bar = flet.SnackBar(flet.Text(f"{text}"))
    else:
        global_helper.GlobalHelper.page.snack_bar.content = flet.Text(f"{text}")
    global_helper.GlobalHelper.page.snack_bar.open = True
    global_helper.GlobalHelper.page.update()