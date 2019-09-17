import csv

with open("PL_1819.csv", "r") as table:
    reader = csv.reader(table)
    data = list(reader)

    team_list = []

    for item in data:
        # print(item)
        [team_list.append(team) for team in item if not team.isdigit()]

# print(team_list)

team_list_2 = []

for index, team in enumerate(team_list):
    if (index % 3) == 0:
        pass
    else:
        team_list_2.append(team)

print(team_list_2)
