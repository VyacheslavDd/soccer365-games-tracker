import datetime
import common.constants as constants

class GameSorter:
    @classmethod
    def sort_by_date(cls, game):
        try:
            return datetime.datetime.timestamp(datetime.datetime.strptime(game.date, constants.DATE_FORMAT_STRING))
        except:
            try:
                return datetime.datetime.timestamp(datetime.datetime.strptime(game.date, constants.ALTERNATIVE_DATE_FORMAT_STRING))
            except:
                return 0