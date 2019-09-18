import csv
import pandas as pd
import numpy as np


# file = "PL_1819.csv"


def read_csv(file):

    with open(f"{file}", "r") as table:
        reader = csv.reader(table)
        data = list(reader)

        column_types = [data[0]]
        del data[0]

        # chaos = []

        winner_n_score = []

        for element in data:
            # print(element)
            # for attr in element:
            #     chaos.append(attr)
            if element[3] > element[4]:
                winner_n_score.append([element[1], 3])
            elif element[3] < element[4]:
                winner_n_score.append([element[2], 3])
            elif element[3] == element[4]:
                winner_n_score.append([element[1], 1])
                winner_n_score.append([element[2], 1])

        # for item in winner_n_score:
        #     list(item)

    # list_idx = []
    #
    # for i in range(len(data)):
    #     list_idx.append(i + 1)

    # pd_df = pd.DataFrame(np.array([chaos]).reshape(len(data), len(element)), index=list_idx, columns=column_types)
    # print(pd_df)


    # my_dict = {v: k for k, v in addresses.items()}

    # print(winner_n_score)
    return winner_n_score
