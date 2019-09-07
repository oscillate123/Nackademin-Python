"""

7. Write a Python function that accepts a string and calculate
the number of upper case letters and lower case letters.

Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12

"""


def counting():

    is_upper = 0
    is_lower = 0

    user_input = input("Type something: ")

    for char in user_input:
        if char.isupper():
            is_upper += 1
        elif char.islower():
            is_lower += 1

    print(f"No. of Upper case character : {is_upper}")
    print(f"No. of lower case character : {is_lower}")
    return


counting()
