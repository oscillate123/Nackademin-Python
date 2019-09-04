"""

Skriv ett program som loopar över en lista innehållandes olika tal. Om programmet stöterpå ett ojämnt tal skrivs orden

“Not allowed!” ut och loopen avbryts.

"""

numbers = list(range(1, 15))

numbers = [number for number in numbers if (number % 2) == 0]

numbers.append(3)
numbers.append(20)

for number in numbers:
    if (number % 2) == 0:
        print(number)
    else:
        print("Not allowed!")
        break

# [print(x) for x in numbers if (x % 2) != 0]
