"""

10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

"""

string_1 = "This is a test"
string_2 = "Rabbits are running"

print(f"{string_1} \n{string_2}")
# print string_1 and string_2, for comparing later on

list_1 = list(string_1)
list_2 = list(string_2)
# make strings to values objects, easier to work with index

list_1[0], list_1[-1], list_2[0], list_2[-1] = list_2[0], list_2[-1], list_1[0], list_1[-1]
# switching letters with each other, using multiple assignment
# https://www.iteanz.com/tutorials/python/multiple-assignment/

string_1 = "".join(list_1)
string_2 = "".join(list_2)
# joining the lists again, so it becomes strings again

print(f"{string_1} \n{string_2}")
# printing strings for comparing with initial strings
