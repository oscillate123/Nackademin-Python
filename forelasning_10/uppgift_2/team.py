"""
a. Initieras med en lista med ett lagnamn som ska sparas som ett klassattribut.
b. Klassen ska även innehålla data om lagets poäng och målskillnad.
c. Klassen ska ha en metod som kan användas till att uppdatera lagets data 
   efter att en match har spelats. Om laget har vunnit ska poängen öka med 3, 
   om matchen har slutat oavgjort ska poängen öka med 1 och vid förlust ska 
   poängen förbli oförändrad.
"""
import csv
import pandas as pd
import numpy as np


class TeamTable:
    def __init__(self, file):
        self.file = file
        with open(f"{file}", "r") as table:
            reader = csv.reader(table)
            data = list(reader)

        data = data[0]

        column_types = ["Teams"]
        list_idx = []

        for i in range(len(data)):
            list_idx.append(i + 1)

        pd_df = pd.DataFrame(np.array([data]).reshape(len(data), 1), index=list_idx, columns=column_types)
        print(pd_df)


