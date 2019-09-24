words_list = ["test", "katt", "hund", "hud", "hem", "hustak", "cykel", "propp", "skärm"]
hints_list = ["h", "t", "u"]
matches = []

for word in words_list:  # loopa genom ordlistan
    hits = [0 for _ in word]  # skapa en temporär "hits lista", t.ex. [0,0,0,0]
    for idx, char in enumerate(word):  # kolla varje bokstav och plats i ordet
        for hint in hints_list:  # jämföra bokstaven med varje "hint"
            if char == hint:  # om bokstaven finns med i hints
                hits[idx] = 1  # ändra bokstavens plats i "hits listan" till 1
                # t.ex. söker efter bokstäver htu, test innehåller t, då blir
                # hits list  = [1,0,0,1], då t matchar in på första och sista
    if len(hints_list) == sum(hits):  # om antal sökta bokstäver är samma som
        # antal träffar, så kommer ordet att läggas till i matches
        matches.append(word)
        # lägger till ordet i matches

print(matches)
