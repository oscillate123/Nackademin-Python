import csv
from Lauras.forelasning10.uppgift2.team import Team
from operator import itemgetter
import pandas as pd
import numpy as np
from Lauras.forelasning10.uppgift2.table import Table

table_list = []


def file_read_csv(file):
    # read csv file
    with open(f"{file}", "r") as file:
        reader = csv.reader(file)
        data = list(reader)
        file.close()
    return data

x = file_read_csv("PL_1819.csv")
del x[0]

y = Team(x[0])

#print(y.goal_difference())
#print(y.win_counter())
#print(y.goal_difference())

alist = []
blist = []
for i in x:
    object = Team(i)
    #print(object.counter())
    #print(object.win_counter())
    #print(object.goal_difference())
    object.update_data(object,alist)
    #print(något)
alist = y.make_lists_of_list(alist)
b = (sorted(alist, key=itemgetter(1)))[::-1]
# print(b)


pd_list = []


for item in b:
    for element in item:
        pd_list.append(element)


titles = ["Team", "Score", "Goal difference"]

print(pd.DataFrame(np.array(pd_list).reshape(20, 3), columns=titles, index=(range(1, 21))))


#
# # z = file_read("teams.csv")
# # table.Table(z, y)


# def loop_list(data):
#     for item in x:
#         stats = team.Team(item)
#         print(stats.counter())
#         print(type(stats.counter()))
#         print(stats.goal_difference())

