class Player:
    def __init__(self, attr):
        self.name = attr["name"]
        self.nationality = attr["nationality"]
        self.assists = attr["assists"]
        self.goals = attr["goals"]
        self.penalties = attr["penalties"]
        self.team = attr["team"]
        self.games = attr["games"]
    
    def __str__(self):
        return f"{self.name} team {self.team} goals {self.goals} assists {self.assists}"
