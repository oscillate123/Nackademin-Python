val1 = int(input("Please type an integer: "))
val2 = int(input("Please type another integer: "))

# +-/*%**

operation_plus = val1 + val2
operation_minus = val1 - val2
operation_divide = val1 / val2
operation_multiply = val1 * val2
operation_sqaure = val1 ** val2


def foo(op, res):
    print(f"Räknesätt {op}, Resultat: {res}")


foo("+", operation_plus)
foo("-", operation_minus)
foo("/", operation_divide)
foo("*", operation_multiply)
foo("^2", operation_sqaure)