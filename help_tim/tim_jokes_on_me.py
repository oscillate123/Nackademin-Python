import csv


with open("PL_1819.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)

    print(data)

    # for object in data:
    #     print(object)