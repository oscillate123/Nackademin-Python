"""

Upprepa uppgiften ovan, men använd denna gång list comprehension för att lösaproblemet.

"""

answer = [(2, 3), (3, 0), (6, 4), (7, 1), (9, 2)]

first_list = [3, 7, 9, 2, 6]

second_list = [2, 3, 6, 7, 9]

output_list = [tuple([x, first_list.index(x)]) for x in second_list]

if output_list == answer:
    print(output_list)
    print("Grattis du klarade uppgiften")
else:
    print(output_list)
    print("Try again")
