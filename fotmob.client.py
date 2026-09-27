import requests
import time


class FotMobClient():
    def __init__(self):
        self.base_url = "https://www.fotmob.com/api"
        # Browser User_Agent(avoids being flagged as a bot)
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/120.0 Safari/537.36",
            "Accept": "application/json",
        })

    def get_match(self, match_id):
        response = self.session.get(
            f"{self.base_url}/matchDetails",
            params={"matchId": match_id}
        )
        response.raise_for_status()
        return response.json()

    def get_team(self, team_id):
        response = self.session.get(
            f"{self.base_url}/teams",
            params={"id": team_id}
        )
        response.raise_for_status()
        return response.json()

    def get_fixtures(self, league_id):
        response = self.session.get(
            f"{self.base_url}/leagues",
            params={"id": league_id}
        )
        response.raise_for_status()
        data = response.json()
        return data.get("matches", {}).get("allMatches", [])

    def poll_match(self, match_id, interval=None):
        """
        Repeatedly fetches a match, sleeping `interval` seconds between calls,
        so you always have the latest live data as the match updates.
        Use this in your main loop instead of calling get_match() once.
        """
        while True:
            yield self.get_match(match_id)
            time.sleep(interval or 30)
