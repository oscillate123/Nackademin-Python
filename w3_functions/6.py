"""

6. Write a Python function to check whether a number is in a given range.

"""


def this_makes_me_numb():
    val1 = int(input("Input number: "))
    val2 = int(input("Provide top value of range: "))
    if val1 in range(val2+1):
        print(f"{val1} is in the range from 0 to {val2}")
    else:
        this_makes_me_numb()
    return


this_makes_me_numb()
