INTEGER = 97
x = True

while x:
    user_input = int(input("Enter an integer: "))
    if user_input != INTEGER:
        continue
    else:
        print("Congratulations, you’re correct​!")
        x = False
