import os

TABLE_COLS = 5
ENTITIES_PER_PAGE = 5
GAME_NEW_PARSE_TIME = 60
STOP_WORD = "Завер"
TABLE_UPDATE_TIME = GAME_NEW_PARSE_TIME / 2
DATE_FORMAT_STRING = "%d.%m.%Y %H:%M"
ALTERNATIVE_DATE_FORMAT_STRING = "%d.%m.%Y"
NOTIFICATION_TIMEOUT_TIME = 3
RUNNING_MATCH_WORD = "Ид"
MAIN_PAGE_URL = "https://soccer365.ru/"
GAME_PAGE_TEMPLATE = "https://soccer365.ru/games/{}/"

ACTION_DICTIONARY = {
    "live_yellowcard": "Жёлтая карточка",
    "live_redcard": "Красная карточка",
    "live_pengoal": "Гол с пенальти",
    "live_psg": "Гол с пенальти (серия пенальти)",
    "live_var": "Отмена гола (VAR)",
    "live_goal": "Гол",
    "live_yellowred": "Вторая жёлтая карточка",
    "live_mispen": "Промах с пенальти",
    "live_psm": "Промах с пенальти (серия пенальти)",
    "live_owngoal": "Автогол"
}