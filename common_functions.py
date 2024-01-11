import flet

def show_snack_bar(page, text):
    if page.snack_bar is None:
        page.snack_bar = flet.SnackBar(flet.Text(f"{text}"))
    else:
        page.snack_bar.content = flet.Text(f"{text}")
    page.snack_bar.open = True
    page.update()