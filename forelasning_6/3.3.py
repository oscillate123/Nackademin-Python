"""

1. Skapa en ny fil
2. Gör en lista med slumpmässiga heltal (Förslagsvis 20 tal mellan 0 och
hundra)
3. Låt användaren ange ett heltal
4. Lägg till en if-sats med strängmetoden .isdecimal() för att säkerställa att
det är en sira och inget annat som användaren matat in.
5. Skriv kod, utan funktioner, som skriver ut en lista på alla udda tal under
användarens angivna värde

"""
import random

my_randoms=[]

while len(my_randoms) < 20:
    x = random.randrange(1, 100, 1)
    if (x % 2) != 0:
        if x not in my_randoms:
            my_randoms.append(x)
    my_randoms.sort()


user_number = input("Provide an integer: ")

while user_number.isdecimal() is not True:
    user_number = input("Provide an integer: ")

user_number = int(user_number)

for number in my_randoms:
    if number < user_number:
        print(number)

