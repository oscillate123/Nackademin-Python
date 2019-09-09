import pandas as pd
import numpy as np

num1 = int(input("Ange ett tal: "))
num2 = int(input("Ange ett tal: "))
num3 = int(input("Ange ett tal: "))
num4 = int(input("Ange ett tal: "))
num5 = int(input("Ange ett tal: "))
num6 = int(input("Ange ett tal: "))
num7 = int(input("Ange ett tal: "))
num8 = int(input("Ange ett tal: "))
num9 = int(input("Ange ett tal: "))
num10 = int(input("Ange ett tal: "))
num11 = int(input("Ange ett tal: "))
num12 = int(input("Ange ett tal: "))

list1 = [num1, num2, num3, num4]
list2 = [num5, num6, num7, num8]
list3 = [num9, num10, num11, num12]

array1 = np.array(list1)
array2 = np.array(list2)
array3 = np.array(list3)

dataframe = pd.DataFrame(np.concatenate((array1, array2, array3), axis=0))

print(dataframe)

