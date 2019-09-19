class Team:
    def __init__(self, match):
        self.match = match
        self.team1 = match[1]
        self.team2 = match[2]
        self.goal1 = match[3]
        self.goal2 = match[4]
        self.goal_diff = 0

    def counter(self):
        if self.goal1 > self.goal2:
            return self.team1
        elif self.goal1 < self.goal2:
            return self.team2
        else:
            return None

    def goal_difference(self):
        if self.goal1 > self.goal2:
            self.goal_diff = self.goal1 - self.goal2
            return self.goal_diff
        elif self.goal1 < self.goal2:
            self.goal_diff = self.goal2 - self.goal1
            return self.goal_diff
        else:
            return self.goal_diff

    def printer(self):
        return print(self.team1, self.team2, self.goal1, self.goal2)
