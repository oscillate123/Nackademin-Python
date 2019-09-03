names = {}

age = {}

shoe_size = {}


# person_1_name = input("Please enter name for person 1:\n").lower()
person_1_name = "Oscar"
names[1] = person_1_name

# person_1_age = int(input("Please enter age for person 1:\n"))
person_1_age = 22
age[1] = person_1_age

# person_1_shoe_size = int(input("Please enter shoe size for person 1:\n"))
person_1_shoe_size = 44
shoe_size[1] = person_1_shoe_size


# person_2_name = input("Please enter name for person 2:\n").lower()
person_2_name = "David"
names[2] = person_2_name

# person_2_age = int(input("Please enter age for person 2:\n"))
person_2_age = 45
age[2] = person_2_age

# person_2_shoe_size = int(input("Please enter shoe size for person 2:\n"))
person_2_shoe_size = 48
shoe_size[2] = person_2_shoe_size


# person_3_name = input("Please enter name for person 3:\n").lower()
person_3_name = "Bente"
names[3] = person_3_name

# person_3_age = int(input("Please enter age for person 3:\n"))
person_3_age = 43
age[3] = person_3_age

# person_3_shoe_size = int(input("Please enter shoe size for person 3:\n"))
person_3_shoe_size = 40
shoe_size[3] = person_3_shoe_size


# age_sorted = sorted(age.values(), reverse=True)


# print(name[1])
# print(age[1])
# print(shoe_size[1])


print(age)

age_twist = {v: k for k, v in age.items()}
print(age_twist)

age_keys = sorted(age_twist, reverse=True)

print(age_twist[age_keys[0]])

highest_age_key = age_twist[age_keys[0]]

print(highest_age_key)

print(f"{names[2]} {age[2]} {shoe_size[2]}")

# age = {v: k for k, v in age.items()}

# print(f"{name}\n{age}\n{shoe_size}")
