# import random
# for i in range(0, 12):
#     x = random.randint(1,10)
#     num_list.append(x)

import pandas as pd
import numpy as np

num_list = []

QX = 1

for i in range(1, 13):

    if i < 5:
        year = 2017
        # QX = quarter(i)
        num_list.append(int(input(f"Vad var resultatet för Q{QX} {year}?")))
        QX += 1

    elif 4 < i < 9:
        year = 2018
        # QX = quarter(i)
        num_list.append(int(input(f"Vad var resultatet för Q{QX} {year}?")))
        QX += 1

    elif 8 < i:
        year = 2019
        # QX = quarter(i)
        num_list.append(int(input(f"Vad är resultatet för Q{QX} {year}?")))
        QX += 1

pd_df = pd.DataFrame(np.array([num_list]).reshape(3, 4), columns=["Q1", "Q2", "Q3", "Q4"], index=[2017, 2018, 2019])

print(pd_df)
