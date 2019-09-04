"""

5.Genom att använda en for-loop, skriv ett program som för varje tal i second_list, hämtar talet och dess
position i first_list och skriver resultatet som en lista av tupler.

 Exempel:

 first_list = [3, 7, 9, 2, 6]

 second_list = [2, 3, 6, 7, 9]

 Output: [(2, 3), (3, 0), (6, 4), (7, 1), (9, 2)]

"""

answer = [(2, 3), (3, 0), (6, 4), (7, 1), (9, 2)]

first_list = [3, 7, 9, 2, 6]

second_list = [2, 3, 6, 7, 9]

output_list = []

for second in second_list:

    idx_idx = first_list.index(second)
    idx_val = first_list[idx_idx]
    temp_set = (idx_val, idx_idx)
    output_list.append(temp_set)

if output_list == answer:
    print(output_list)
    print("Grattis du klarade uppgiften")
else:
    print(output_list)
    print("Try again")
