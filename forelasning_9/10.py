"""

10. Write a Python program to count the frequency of words in a file.

"""

lines = []

words = []

with open("text1.txt", "r") as file:
    for line in file:
        lines.append(line)

for i in lines:
    if " " in i:
        x = i.split(" ")
        for item in x:
            words.append(item.replace("\n", ""))
    else:
        words.append(i.replace("\n", ""))

words.sort(key=len, reverse=True)

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print("\n")
print(" Word count:" + "\n" + str(count).replace(",", "\n").replace("{", " ").replace("}", " "))
