from forelasning_10.uppgift_2.team import Team


class Table:
    def __init__(self, team_names, match):
        self.team_names = team_names
        self.team = Team(match)

    def update_score(self):
        pass