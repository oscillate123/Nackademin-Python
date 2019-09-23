

class Team:
    def __init__(self, match):
        self.match = match
        self.match_team1 = match[1]
        self.match_team2 = match[2]
        self.goal1 = int(match[3])
        self.goal2 = int(match[4])

    def counter(self):
        # returns the teams and their points
        return self.match_team1, self.goal1, self.match_team2, self.goal2

    def win_counter(self):
        # see who's the winner and returns the winning team, or None if no one won.
        if self.goal1 > self.goal2:
            return self.match_team1
        elif self.goal1 < self.goal2:
            return self.match_team2
        else:
            return None

    def loosing_counter(self):
        # see who's the looser and returns the loosing team, or None if no one lost.
        if self.goal1 < self.goal2:
            return self.match_team1
        elif self.goal1 > self.goal2:
            return self.match_team2
        else:
            return None

    def goal_difference(self):
        if max(self.goal1, self.goal2) > min(self.goal1, self.goal2):
            return max(self.goal1, self.goal2) - min(self.goal1, self.goal2), min(self.goal1, self.goal2) - max(self.goal1, self.goal2)
        else:
            return 0

    def update_data(self, object, a_list):
        # Om lagen inte redan finns i listan läggs de in med två nollor där poäng och måldiff
        # ska samlas
        if self.match_team1 not in a_list:
            a_list.append(self.match_team1)
            a_list.append(0)
            a_list.append(0)
        if self.match_team2 not in a_list:
            a_list.append(self.match_team2)
            a_list.append(0)
            a_list.append(0)

        # Här används metoden win_counter för att se vilket lag som vunnit eller om det blivit oavgjort
        # Blir det oavgjort returneras None och resulterar i att båda lagen får 1 poäng var
        # Vinner något lag så får endast det laget 3 poäng. Detta visas i else-satsen
        if object.win_counter() == None:
            a = a_list.index(self.match_team1) + 1
            b = a_list.index(self.match_team2) + 1
            a_list[a] = int(a_list[a]) + 1
            a_list[b] = int(a_list[b]) + 1
            return a_list
        else:
            c = a_list.index(object.win_counter()) + 1
            d = a_list.index(object.win_counter()) + 2
            e = a_list.index(object.loosing_counter()) + 2
            a_list[c] = int(a_list[c]) + 3
            a_list[d] = int(a_list[d]) + object.goal_difference()[0]
            a_list[e] = int(a_list[e]) + object.goal_difference()[1]
            return a_list



    def make_lists_of_list(self, a_list):
        #Skapar en lista med listor för att inte tappa bort värden vid senare sortering
        b_list = []
        while len(a_list) != 0:
            c_list = []
            c_list.append(a_list[0])
            c_list.append(a_list[1])
            c_list.append(a_list[2])
            b_list.append(c_list)
            a_list.remove(a_list[0])
            a_list.remove(a_list[0])
            a_list.remove(a_list[0])
        return b_list





        #if object.win_counter() == self.match_team1:



