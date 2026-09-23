class Precictor():
  def predict(self, home_team, away_team):

    home_strength = self.calculate_strength(home_team)
    away_strength = self.calculate_strength(away_team)

    total = home_strength + away_strength

    home_probability = home_strength / total
    away_probability = away_strength / total

    draw_probability = 1 - home_probability - away_probability
    
    return{"home": home_probability,"draw": draw_probability,"away": away_probability}
    
  def calculate_strength(self, team):
    pass
