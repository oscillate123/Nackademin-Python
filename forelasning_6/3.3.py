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
        my_randoms.append(x)

print(len(my_randoms))
print(my_randoms)


userInput = input("Please type an integer: ")


