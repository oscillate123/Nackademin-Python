import forelasning_10.uppgift_2.oscar_version as U2


class CreateTeam:
    def __init__(self, match_scores):
        self.match_scores = match_scores
        # print(match_scores)

    def team_score(self):

        global match
        count = []

        for i in self.match_scores:
            for match in i:
                if match in count:
                    count[i] += i[1]
                    count.append("z")  # remove z
                    print(match)
                else:
                    count.append([match[0], match[1]])

        return print(match)

    def goal_diff(self):
        pass


CreateTeam(U2.read_csv("PL_1819.csv")).team_score()
