import flet

class DetailsView:
    def __init__(self):
        self.cur_index = -1
        self.list_container = flet.Container(margin=flet.margin.only(top=50), alignment=flet.alignment.center)
        self.details_list = flet.ListView(spacing=10, padding=20, auto_scroll=False, width=500, height=150)
        self.list_container.content = self.details_list