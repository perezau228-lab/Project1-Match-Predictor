import requests
import time


class FotMobClient():
    def __init__(self):
        self.base_url = "https://www.fotmob.com/api"
        # Browser User_Agent(avoids being flagged as a bot
        self.search_url = "https://apigw.fotmob.com/searchapi/suggest"
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

    def search_team(self, name):
        response = self.session.get(
            self.search_url,
            params={"term": name, "lang": "en"}
        )
        response.raise_for_status()
        data = response.json()

        team_matches = data.get("teamSuggest", [])
        if not team_matches:
            return None

        options = team_matches[0].get("options", [])
        if not options:
            return None

        best_match = options[0].get("payload", {})
        team_id = best_match.get("id")
        team_name = best_match.get("name")

        if team_id is None:
            return None

        return team_id, team_name

    def get_next_fixture(self, team_id):
        team_data = self.get_team(team_id)

        fixtures = team_data.get("fixtures", {})
        all_fixtures = fixtures.get("allFixtures", {}) if isinstance(fixtures, dict) else {}
        next_match_list = all_fixtures.get("nextMatch") or all_fixtures.get("fixtures")

        if not next_match_list:
            return None

        next_match = next_match_list[0] if isinstance(next_match_list, list) else next_match_list

        try:
            return {
                "match_id": next_match["id"],
                "home_id": next_match["home"]["id"],
                "home_name": next_match["home"]["name"],
                "away_id": next_match["away"]["id"],
                "away_name": next_match["away"]["name"],
                "date": next_match.get("status", {}).get("utcTime"),
            }
        except (KeyError, TypeError):
            return None

    def poll_match(self, match_id, interval=None):
        while True:
            yield self.get_match(match_id)
            time.sleep(interval or 30)
