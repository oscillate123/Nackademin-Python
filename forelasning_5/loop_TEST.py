my_numbers = [1, 2, 3, 4, 5, 6, 7]

for i in my_numbers:
    print(i)


print("\n")

y = True
x = 0

while y:
    x += 1
    print(x)
    if x == 8:
        y = False


print("\n")

x_list = [1,2,3]
y_list = ["a", "b", "c"]


for x in x_list:
    print(x)
    for y in y_list:
        print(str(x) + y)


print("\n")

for val in "string":
    if val != "n":
        print(val)
        continue
    else:
        break

print(" value == n , therefor we break the loop")


print("\n")

numbers = [1, 2, 3, 4, 5, 6, 7]

squares = [number**2 for number in numbers if (number % 2) != 0]

print(squares)
