task_string_1 = "Jag tYcker om äGg!"
task_string_2 = "jAG tYCKER iNTE oM SPAM!"
task_string_3 = "SPAM!"
task_string_4 = "inte"
task_string_5 = "äGg!"

task_string_6 = task_string_3.lower()


x = task_string_1.rsplit(" ")
y = task_string_2.rsplit(" ")

z = x + y

# print(z)

z = " ".join(z)

# print(z)

z = z.lower()

z = z.replace("jag", " ", 1)

z = z.replace("tycker", " ", 1)

z = z.replace("om", " ", 1)

z = z.replace("ägg", " ", 1)

z = z.replace("!", " ", 1)


# print(z)

z = z.replace("jag", "jAG")

z = z.replace("tycker", "tYCKER")

z = z.replace("inte", "iNTE")

z = z.replace("om", "oM")

z = z.replace(task_string_6, task_string_3)

print(z)

