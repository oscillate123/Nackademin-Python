import csv
import forelasning_10.uppgift_2.team as team
import forelasning_10.uppgift_2.table as tabell

with open("PL_1819.csv", "r") as statistik:
    reader = csv.reader(statistik)
    data = list(reader)

del data[0]

x = team.Team(data[0])
print(x.counter())
print(x.goal_diff)


# for row in data:
#     x = match.Team.printer(row)
#     print(x)

