"""
a. Initieras med en lista med lagnamn. Utifrån vart och ett av dessa lagnamn 
   ska en Team-instans skapas och läggas i en lista.
b. Ha en metod för att ta emot data från en match och uppdatera de lag som 
   matchen gäller.
c. Kunna skriva ut hela tabellställningen sorterad på poäng i fallande skala i
   formatet Lagnamn, Poäng, Målskillnad.
"""

import csv
import pandas as pd
import numpy as np


class ScoreTable:
    def __init__(self, file):
        self.file = file
        with open(f"{file}", "r") as table:
            reader = csv.reader(table)
            data = list(reader)

            column_types = [data[0]]
            del data[0]

            chaos = []

            for element in data:
                # print(element)
                for attr in element:
                    chaos.append(attr)

        list_idx = []

        for i in range(len(data)):
            list_idx.append(i + 1)

        pd_df = pd.DataFrame(np.array([chaos]).reshape(len(data), len(element)), index=list_idx, columns=column_types)
        print(pd_df)


    def score_sum(self):
        pass


ScoreTable("PL_1819.csv")



