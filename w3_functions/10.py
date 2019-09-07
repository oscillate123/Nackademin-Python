"""

10. Write a Python program to print the even numbers from a given list.

Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]

"""


def print_even():
    nums = []
    numbers = int(input("Give me a number: "))
    [nums.append(i) for i in list(range(1, numbers + 1)) if (i % 2) == 0]
    print(nums)


print_even()
