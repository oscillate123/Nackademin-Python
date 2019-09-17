X = 1
Y = 4

addresses = {"Adam": "Ormvägen 5",
             "Bella": "Klockgatan 1",
             "Cornelia": "Vikingagatan 3"}

cars = ["Volvo", "Opel", "BMW"]

numbers1 = {1, 2, 3, X, 6}

numbers2 = {Y, 2, 3, 4, 7}

# 1. X & Y har datatyp: Integer

# 2. addresses har datatypen: dictonary

# 3.

print(addresses["Bella"])

# 4. Vad händer om man skriver: addresses[“Daniel”] = “Prinsgränd 2”​
# Värdet tillhörande nyckeln "Daniel" till "Prinsgränd 2" läggs till i dic addressess

# 5.
print(len(addresses.keys()))

# 5.1

print(sorted(list(addresses.keys()))[-1])

# 5.2 - Utöka programmet så att namnet skrivs ut på den personen som bor på adressen som kommer först i bokstavsordning.

my_dict = {v: k for k, v in addresses.items()}

print(sorted(my_dict.keys()))

# 6. Cars är datatypen lista

# 7. Open blir resultatet, då X = 1, och vi kallar på item med index 1 i listan cars

print(cars[X])

# 8. print(cars[Y]) kommer inte gå att skriva eftersom att Y = 4 och listan cars innehåller bara 3 items
# dvs 0,1,2 i index. Vi kan därför inte söka på index 4 i listan cars

# 9. BMW hamnar på första plats i listan cars

cars.sort()
print(cars[0])

# 10.

cars_2 = cars
cars.append("Saab")

print(f"{cars}\n{cars_2}")

# 10.1

cars_3 = cars.copy()
cars.append("Honda")

print(f"{cars_3}\n{cars}")

# 10.2

cars = cars + cars
cars.sort()
cars.reverse()
print(cars)

# 10.3

unique_cars = set(cars)
print(unique_cars)

# 11 numbers1 & numbers2 är datatypen set

# 12

print(f"{numbers1}\n{numbers2}")

numbers3 = numbers1 & numbers2

# 13

print(numbers3)

# 14

unionen = numbers1 | numbers2

print(unionen)

# 15 fråga läraren om skillnad mellan symmetrisk differens och differens

korsning = numbers1 & numbers2

symmetrisk_differens = unionen - korsning

print(symmetrisk_differens)

# eller i en "oneliner"

symmetrisk_differens2 = (numbers1 | numbers2) - (numbers1 & numbers2)

print(symmetrisk_differens2)

# variant på 15, som är effektivare

sym_dif_func_in_pyth = numbers1.symmetric_difference(numbers2)

print(sym_dif_func_in_pyth)