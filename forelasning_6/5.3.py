# val1 = int(input("Please type an integer: "))
# val2 = int(input("Please type another integer: "))
#
# +-/*%**
#
# print(f"Resultatet av:\n{val1} + {val2} = {val1 + val2}")
# print(f"Resultatet av:\n{val1} - {val2} = {val1 - val2}")
# print(f"Resultatet av:\n{val1} / {val2} = {val1 / val2}")
# print(f"Resultatet av:\n{val1} * {val2} = {val1 * val2}")
# print(f"Resultatet av:\n{val1} % {val2} = {val1 % val2}")
# print(f"Resultatet av:\n{val1} ** {val2} = {val1 ** val2}")

arithmetics = ["+", "minus", "divide", "multiply", "mod", "potency"]

u_var1 = int(input("Please type an integer: "))
u_arithmetic = input(f"Which arithmetic do you want to use?\nYou can use these:\n{arithmetics}\n")
u_arithmetic_type = u_arithmetic
u_var2 = int(input("Please type another integer: "))

if u_arithmetic == "+":
    u_arithmetic = lambda var1, var2: var1 + var2
elif u_arithmetic == "minus":
    u_arithmetic = lambda var1, var2: var1 - var2
elif u_arithmetic == "divide":
    u_arithmetic = lambda var1, var2: var1 / var2
elif u_arithmetic == "multiply":
    u_arithmetic = lambda var1, var2: var1 * var2
elif u_arithmetic == "mod":
    u_arithmetic = lambda var1, var2: var1 % var2
elif u_arithmetic == "potency":
    u_arithmetic = lambda var1, var2: var1 ** var2


def math_op(lambda_f, v1, v2):
    print(f"{v1} {u_arithmetic_type} {v2} gives: {lambda_f(v1, v2)}")


math_op(u_arithmetic, u_var1, u_var2)
