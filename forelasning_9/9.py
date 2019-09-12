"""

9. Write a Python program to count the number of lines in a text file.

"""

lines = []

with open("text1.txt", "r") as file:
    for line in file:
        lines.append(line)

print(len(lines))