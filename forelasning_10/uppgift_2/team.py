import unittest


class Team:
    def __init__(self, match):
        self.match = match
        self.team1 = match[1]
        self.team2 = match[2]
        self.goal1 = int(match[3])
        self.goal2 = int(match[4])

    def counter(self):
        if self.goal1 > self.goal2:
            return self.team1
        elif self.goal1 < self.goal2:
            return self.team2
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
        # return print(self.team1, self.team2, self.goal1, self.goal2)


if __name__ == "__main__":
    x = Team(["datum", "lag1", "lag2", "4", "6"])
    print(x.goal_difference())
    print(x.counter())
