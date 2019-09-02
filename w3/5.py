"""

5. Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.

Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'

"""

string_1 = 'abc'
string_2 = 'xyz'

list_1 = list(string_1)
list_2 = list(string_2)

list_added = list_1 + list_2
print(list_added)

list_added[0], list_added[-1] = list_added[-1], list_added[0]
list_added[1], list_added[-2] = list_added[-2], list_added[1]
print(list_added)

list_len = len(list_added)
list_middle = list_len/2
print(list_middle)

list_added.insert(int(list_middle), " ")
list_merged = "".join(list_added)
print(list_merged)

