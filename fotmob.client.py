import os
import requests

class FotMobClient():
  def __init__(self):
    self.base_url = "https://www.fotmob.com"
  def get_match(self, match_id):
    response = requests.get(f"{self.base_url}/api/MatchDetails", params={'match_id'})
    response.raise_for_status()
    return response.json()
  def get_team(self, team_id):
    pass
  def get_fixtures(self, league_id):
    pass
