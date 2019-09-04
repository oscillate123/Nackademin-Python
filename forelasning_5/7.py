"""

7.Du har följande lista på frukter:
fruits = ['apple', 'orange', 'pear', 'banana', 'grapes']

Skriv ett program som frågar användaren efter hur många platser för frukt hen har i sin korg,
och sedan fyller du denna korg (en lista) med frukter genom att loopa igenom frukt-listan
tills dess att korg-listan är full.

Output-exempel:

My_basket = ['apple', 'orange', 'pear', 'banana', 'grapes', 'apple','orange', 'pear']


"""


size = int(input("How many fruits can your basket store?"))

# size = 7

fruits = ['apple', 'orange', 'pear', 'banana', 'grapes']
my_basket = []
i = 0

while i < size:
    for fruit in fruits:
        if i <= size:
            my_basket.append(fruit)
            i += 1
        elif size % len(fruits) != 0 & size == i-1:
            my_basket.append(fruit)
            i += 1

print(my_basket)
print(len(my_basket))
