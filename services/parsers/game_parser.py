import requests
from bs4 import BeautifulSoup as bs
import datetime
import services.helpers.re_helper as re_helper
import entities.match as match
import common.constants as constants

class GameParser:
    @classmethod
    def get_game_details(cls, home_team, away_team, page):
        details = []
        details_list = page.select(".mrgt15 ~ div")
        for detail in details_list:
            try:
                minute = detail.select_one(".event_min").text.strip()
                team = detail.select_one(".event_ht") if len(detail.select(".event_ht div")) > 0 else detail.select_one(".event_at")
                team_name = home_team if "ht" in team['class'][0] else away_team
                player = team.select_one(".img16 span a").text.strip()
                assistance = team.select_one(".assist")
                assistance = f"({assistance.text.strip()})" if assistance is not None else ""
                action = team.select_one(f".{team['class'][0]}_icon")
                action = constants.ACTION_DICTIONARY[action['class'][1].strip()]
                detail_string = f"{minute}: {player}, {action} {assistance} ({team_name})"
                details.append(detail_string)
            except Exception as e:
                continue
        return details

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
        details = cls.get_game_details(home_team, away_team, parsed_data)
        if new_game_parse:
            return cls._map_data(url, date, home_team, away_team, score, status, details)
        return [score, status, details]