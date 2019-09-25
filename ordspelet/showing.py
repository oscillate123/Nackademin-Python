import ordspelet.read_file as r_file

words_db = r_file.get_words()
words_list = words_db.copy()
hints_list = []
matches = []

print("Vilka 3 bokstäver får ordet innehålla?")

while len(hints_list) < 3:
    hints_list.append(input(f"Bokstav {len(hints_list) + 1}:"))

    for word in words_list:
        hits = [0 for _ in word]
        for idx, char in enumerate(word):
            for hint in hints_list:
                if char == hint:
                    hits[idx] = 1

        if len(hints_list) <= sum(hits):
            matches.append(word)
        elif len(hints_list) >= sum(hits):
            words_list.remove(word)

    print(len(matches))
    print(len(words_list))
