"""

13. Write a Python program to copy the contents of a file to another file .

"""

list_12 = "str(list_12)"

x = ""

with open("text1.txt", "r") as file_12:
    x += file_12.read()


with open("test13.txt", "w") as file_13:
    file_13.write(x)

