"""

Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged.

Sample String : 'abc'
Expected Result : 'abcing'

Sample String : 'string'
Expected Result : 'stringly'

"""

string_1 = 'baking'
list_1 = list(string_1)

ing = ["i", "n", "g"]
ly = ["l", "y"]

if len(list_1) >= 3:
    if list_1[-3:] != ing:
        list_1.extend(ing)
        string_1 = "".join(list_1)
        print(string_1)
    else:
        list_1.extend(ly)
        string_1 = "".join(list_1)
        print(string_1)
