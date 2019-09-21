import unittest


class Team:
    def __init__(self, match, team):
        self.team = team
        self.match = match
        self.match_team1 = match[1]
        self.match_team2 = match[2]
        self.goal1 = int(match[3])
        self.goal2 = int(match[4])

    def counter(self):
        # see who's the winner and returns the winning team, or None if no one won.
        if self.goal1 > self.goal2:
            return self.match_team1
        elif self.goal1 < self.goal2:
            return self.match_team2
        else:
            return None

    def goal_difference(self):
        if self.goal1 > self.goal2:
            return self.goal1 - self.goal2
        elif self.goal1 < self.goal2:

            return self.goal2 - self.goal1
        else:
            return 0

    def printer(self):
        pass
        # return print(self.match_team1, self.match_match_team2, self.goal1, self.goal2)


if __name__ == "__main__":
    x = Team(["datum", "lag1", "lag2", "4", "6"])
    print(x.goal_difference())
    print(x.counter())
