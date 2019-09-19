import csv
import forelasning_10.uppgift_2.team as team
import forelasning_10.uppgift_2.table as table


def file_read(file):
    with open(f"{file}", "r") as file:
        reader = csv.reader(file)
        data = list(reader)
        file.close()
    return data


x = file_read("PL_1819.csv")
del x[0]

y = team.Team(x[0])

print(y.counter())
print(y.goal_difference())

z = file_read("teams.csv")
table.Table(z, y)

