"""
a. Läsa in de två datafilerna.
b. Initiera en Table-instans med en lista med de lagnamn givna av teams.csv 
   som argument.
c. Iterera igenom alla matcher i PL_1819.csv och lägga till dem en och en i 
   Table-instansen så att denna kan uppdatera sina Team-instanser.
d. Efter var tionde match och efter den sista matchen för säsongen ska Table-
   instansen ombeds att skriva ut hela tabellställningen.
"""

import forelasning_10.uppgift_2.team as t
import csv


def read_file(file, type):
    with open(f"{file}", "r") as table:
        reader = csv.reader(table)
        data = list(reader)
        if type == "team":
            x = t.Team_Table(data)
            print(x)
        elif type == "score":
            print(data)


# read_file("teams.csv", "team")

t.TeamTable("teams.csv")
