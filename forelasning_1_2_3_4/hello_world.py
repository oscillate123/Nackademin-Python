n = "\n"

input_val_a = int(input("Skriv tal A: " + n))
input_val_b = int(input("Skriv tal B: " + n))

print_sum = input_val_a + input_val_b
msg_sum = "Addition:" + n + "Tal A (" + str(input_val_a) + ") + Tal B (" + str(input_val_b) + ") = "
print(n + msg_sum + str(print_sum) + n)

print_sub = input_val_a - input_val_b
msg_sub = "Subtraktion:" + n + "Tal A (" + str(input_val_a) + ") - Tal B (" + str(input_val_b) + ") = "
print(n + msg_sub + str(print_sub) + n)

print_div = input_val_a * input_val_b
msg_sub = "Multiplikation:" + n + "Tal A (" + str(input_val_a) + ") * Tal B (" + str(input_val_b) + ") = "
print(n + msg_sub + str(print_div))

print_div = input_val_a / input_val_b
msg_sub = "Divison:" + n + "Tal A (" + str(input_val_a) + ") / Tal B (" + str(input_val_b) + ") = "
print(n + msg_sub + str(print_div))

print_div = input_val_a // input_val_b
msg_sub = "Heltalsdivision:" + n + "Tal A (" + str(input_val_a) + ") // Tal B (" + str(input_val_b) + ") = "
print(n + msg_sub + str(print_div))

