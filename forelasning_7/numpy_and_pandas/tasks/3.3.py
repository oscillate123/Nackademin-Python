import pandas as pd
import numpy as np

year_list = [2017, 2018, 2019]
quarter_list = ["Q1", "Q2", "Q3", "Q4"]

num_list = []

for year in year_list:
    for quarter in quarter_list:
        num_list.append(int(input(f"What was the result of {quarter} {year}? : ")))

pd_df = pd.DataFrame(np.array([num_list]).reshape(3, 4), columns=quarter_list, index=year_list)

print(pd_df)
