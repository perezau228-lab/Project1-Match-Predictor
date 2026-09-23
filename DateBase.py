import sqlite3

class DataBase:
  def __init__(self):
    self.connection = sqlite3.connect("soccer.db")
  def sav_match(self, match):
    pass
  def get_team_history(self, team_id):
    pass
