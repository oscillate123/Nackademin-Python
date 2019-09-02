"""

11. Write a Python program to remove the characters which have odd index values of a given string.

"""

string = "nackademin"
list = []
list2 = []

for index, item in enumerate(string):
    # print(f"{index} -> {item}")
    if (index % 2) == 0:
        print(f"{index} -> even index -> value: {item}")
        list.extend(item)
    else:
        print(f"{index} -> odd index --> value: {item}")
        list2.extend(item)

list = "".join(list)
list2 = "".join(list2)
list3 = list + " " + list2

print(f"\nSaved chars: {list}")
print(f"Removed chars: {list2}")
print(f"Added lists: {list3}")
print(f"Original string: {string}")