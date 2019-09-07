add = lambda var1, var2: var1 + var2
sub = lambda var1, var2: var1 - var2
div = lambda var1, var2: var1 / var2
mult = lambda var1, var2: var1 * var2
mod = lambda var1, var2: var1 % var2

arithmetic = {"+": add,
               "-": sub,
               "/": div,
               "*": mult,
               "%": mod}

while True:
    u_var1 = int(input("Please type an integer: "))

    u_arithmetic = input(f"Which arithmetic do you want to use?\n"
                        f"You can use these:\n"
                        f"{arithmetic.keys()}\n")

    u_var2 = int(input("Please type another integer: "))

    print(f"Is this correct? {u_var1} {u_arithmetic} {u_var2}")
    u_confirm = input(f"Yes/No \n ").lower()

    arithmetic_value = arithmetic[u_arithmetic]

    if u_confirm == "yes":
        break


def math_op(lambda_f, v1, v2):
    print(f"{v1} {u_arithmetic} {v2} = {lambda_f(v1, v2)}")


math_op(arithmetic_value, u_var1, u_var2)
