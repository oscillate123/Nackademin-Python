def function_sum(term1, term2):
    sum = term1 + term2
    print(f"Sum is {sum}")


function_sum(3, 4)


def function_name(argument1, argument2, argument3):
    return_value = argument1 + argument2 + argument3

    global argument4
    argument4 = 4

    return return_value, argument1, argument2, argument3


print(function_name(1, 2, 3))
print(argument4)


plus = lambda var1, var2, var3: var1 + var2 + var3

minus = lambda x, y, z: x - y - z

print(f"Lambda plus resultat: {plus(2,2,3)}")

print(f"Lambda minus resultat: {minus(6, 3, 1)}")

