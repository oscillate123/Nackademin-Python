"""

6. Write a Python program to read a file line by line store it into a variable.

"""


lines = ""

with open("text1.txt", "r") as file:
    for line in file:
        lines += line

print(lines)
