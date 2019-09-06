"""

6. Öppna en ny l
7. Skriv, i den nya len, en funktion för att generera en slumpmässig list.
Funktionen ska ta ett argument för hur många tal du ska ha, och en för
hur högt de ska gå.
8. Skriv en funktion som frågar efter input och repeterar tills det är en sira
för att sedan returnera en int.
9. Skriv en till funktion som tar en lista och ett tal som argument, och
returnerar en lista på tal över det angivna talet
10. Skriv ytterliggare en funktion som tar en lista med tal som argument och
returnerar en lista med uddatal
11. Skriv ett program som använder funktionerna för att göra samma sak som
i den förra len.
12. Läs igenom lerna och fundera över vilken du skulle förstå lättast om du
inte visste på förhand vad de gjorde.

"""
import random


def list_randoms(max_len, max_val):
    random_ints = []

    while len(random_ints) < max_len:
        x = random.randrange(1, max_val, 1)
        random_ints.append(x)

    random_ints.sort()
    return random_ints


def list_odds(number_list):
    odd_numbers = []

    for number in number_list:
        if (number % 2) != 0:
            odd_numbers.append(number)

    return odd_numbers


def input_user():
    user_number = ""

    while user_number.isdecimal() is not True:
        user_number = input("Provide an integer: ")

    return int(user_number)


def compare(some_list, u_input):
    compared_list = []

    for number in some_list:
        if number > u_input:
            compared_list.append(number)

    return compared_list


print(compare(list_odds(list_randoms(30, 1000)), input_user()))
