"""

8.Skriv ett program som använder sig av nästlade while-loopar för att
skriva ut alla primtal som är mindre än 100.
Vägledning: Primtal är ett tal som är större än 1 och som inte går att dela
jämnt med något tal annat än sig själv och 1.

"""

i = 1

while i < 100:
    # print i if i is prime

    isPrime = True  # flag
    x = 2

    while (i / 2) >= x:
        # print(f" i -> {i}")
        # print(f" x -> {x}")

        if i % x == 0:
            isPrime = False  # raise flag
            break
        x += 1

    if isPrime:  # flag check
        print(i)

    # print("\n" + "_________")
    i += 1
