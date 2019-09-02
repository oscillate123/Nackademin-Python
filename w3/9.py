"""

9. Write a Python program to remove the 'n'th index character from a nonempty string.

9. Ta bort en bokstav genom att berätta vilken position bokstaven har i ordet.

"""

def word(string, i):
    letter = string[i]
    string = list(string)
    string.remove(letter)
    string = "".join(string)
    print(string)

word("Python", 2)
word("Oscar", 1)
word("nackademin", 5)
