
class Match:
    def __init__(self, row_index, url, date, title, status, score):
        self.url = url
        self.date = date
        self.title = title
        self.status = status
        self.score = score
        self.row_index = row_index