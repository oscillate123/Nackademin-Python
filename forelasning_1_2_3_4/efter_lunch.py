n = "\n"


a = 2
b = 4

print_msg_1 = n + str(a) + n + str(b)


print(str(print_msg_1))

a, b = b, a


print_msg_2 = n + str(a) + n + str(b)


print(str(print_msg_2))
