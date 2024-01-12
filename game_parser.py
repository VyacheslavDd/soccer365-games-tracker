import requests
from bs4 import BeautifulSoup as bs
import datetime
import re_helper
import match

class GameParser:
    @classmethod
    def get_game_details(cls, page):
        return []

    @classmethod
    def _map_data(cls, url, date, home_team, away_team, score, status, details):
        match_obj = match.Match(0, url, date, f"{home_team} - {away_team}", status, score, details)
        return match_obj

    @classmethod
    def parse_game(cls, url, new_game_parse=True):
        page_text = requests.get(url).text
        parsed_data = bs(page_text, 'lxml')
        if parsed_data.select_one("#game_events") is None:
            raise Exception("Передана некорректная страница!")
        info_line = parsed_data.select_one("#game_events .bkcenter h2").text
        date = re_helper.RegularExpressionHelper.find_date(info_line)
        home_team = parsed_data.select_one(".live_game_ht a").text.strip()
        away_team = parsed_data.select_one(".live_game_at a").text.strip()
        score = ":".join([x.text.strip() for x in parsed_data.select(".live_game_goal span")])
        status = parsed_data.select_one(".live_game_status b")
        status = "Не начат" if status is None else (status.text if not re_helper.RegularExpressionHelper.contains_minute(status.text) else f"Идёт: {status.text}")
        details = cls.get_game_details(parsed_data)
        if new_game_parse:
            return cls._map_data(url, date, home_team, away_team, score, status, details)
        return [score, status, details]