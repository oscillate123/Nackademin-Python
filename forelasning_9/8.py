"""

8. Write a python program to find the longest words

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

print(words[0])
