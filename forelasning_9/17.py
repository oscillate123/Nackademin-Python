"""

17. Write a Python program to remove newline characters from a file.

"""

lines = []

words = []

with open("text1.txt", "r") as file:
    for line in file:
        lines.append(line)

for i in lines:
    if " " in i:
        for item in i:
            words.append(item.replace("\n", ""))
    else:
        words.append(i.replace("\n", ""))


with open("text17.txt", "w") as file_17:
    for word in words:
        file_17.write(word)
