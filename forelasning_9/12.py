"""

12. Write a Python program to write a list to a file.

"""

list_12 = [1, 2, 3, 4, 5, "\n6"]
list_12 = str(list_12)

with open("test12.txt", "w") as file:
    file.write(list_12)
