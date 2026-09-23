class Team():
  def __init__(self, team_id, name):
    self.team = team_id
    self.name = name
    
    self.wins = 0
    self.draw = 0
    self.losses = 0
    
    self.goals_for = 0
    self.goals_against = 0
    self.recent_results = []
  
  def win_rate(self):
    matches_played = self.wins + self.draw + self.losses
    if matches_played == 0:
        return 0
    else:
        return self.wins / matches_played
  
  def goal_difference(self):
    return self.goals_for - self.goals_against

  def record_result(self, goals_for, goals_against, game_result):
    if game_result == "W":
      self.wins += 1
    elif game_result == "D":
      self.draw += 1
    elif game_result == "L":
      self.losses += 1
    
class Match():
  def __init__(self, match_id, home_team, away_team):
    self.match_id = match_id
    self.home_team = home_team
    self.away_team = away_team
    
    self.home_score = 0
    self.away_score = 0
    
    self.minute = 0
    self.status = "Not Started"
    
class Prediction():
  def __init__(self, home_probability, draw_probability, away_probability):
    self.home_probability = home_probability
    self.draw_probability = draw_probability
    self.away_probability = away_probability
    
