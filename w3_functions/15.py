"""

15. Write a Python program that accepts a hyphen-separated
sequence of words as input and prints the words in a
hyphen-separated sequence after sorting them alphabetically.

Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow

"""


def hype():
    user_input = input("some text please: ")

    listing = user_input.split("-")
    listing.sort()
    print("-".join(listing))


hype()
