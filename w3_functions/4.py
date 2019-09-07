"""

Rekommenderade uppgifter: 4, 6, 7, 10, 12, 13, 15, 18
(Lärarnas kommentar)

4. Write a Python program to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"

"""


def reverse():
    user_input = list(input("Type some characters: "))
    user_input.reverse()
    user_input = "".join(user_input)
    print(user_input)
    return


reverse()
