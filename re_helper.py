import re
import datetime

class RegularExpressionHelper:
    _game_url_pattern = r"https://soccer365.ru/games/\d{4,10}/?"
    _date_pattern = r"\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}|\d{2}\.\d{2}\.\d{4}"
    _number_pattern = r"\d{1,}"
    _row_split_pattern = r'"([^"]*)"'
    @classmethod
    def check_game_url(cls, url):
        if re.fullmatch(cls._game_url_pattern, url):
            return
        raise Exception("Некорректная ссылка!")
    
    @classmethod
    def find_date(cls, info_line):
        result = re.findall(cls._date_pattern, info_line)
        if len(result):
            return result[0]
        date = datetime.date.today()
        day = date.day if date.day > 9 else "0" + str(date.day)
        month = date.month if date.month > 9 else "0" + str(date.month)
        return f"{day}.{month}.{date.year}"
    
    @classmethod
    def contains_minute(cls, status_line):
        if len(re.findall(cls._number_pattern, status_line)) > 0:
            return True
        return False
    
    @classmethod
    def split_data_row(cls, row):
        return re.findall(cls._row_split_pattern, row)