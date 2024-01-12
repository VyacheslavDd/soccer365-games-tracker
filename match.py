from threading import Timer
import game_parser
import constants

class Match:
    def __init__(self, row_index, url, date, title, status, score, details=list()):
        self.url = url
        self.date = date
        self.title = title
        self.status = status
        self.score = score
        self.details = details
        self.row_index = row_index
        self.timer = None
        if not self.status.startswith(constants.STOP_WORD):
            self.timer = Timer(constants.GAME_NEW_PARSE_TIME, self.update_data)
            self.timer.start()

    def update_data(self, manual_update=False):
        new_data = game_parser.GameParser.parse_game(self.url, new_game_parse=False)
        self.score = new_data[0]
        self.status = new_data[1]
        self.details = new_data[2]
        if not new_data[1].startswith(constants.STOP_WORD) and not manual_update:
            self.timer = Timer(constants.GAME_NEW_PARSE_TIME, self.update_data)
            self.timer.start()