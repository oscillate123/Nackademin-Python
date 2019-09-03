names = {}

age = {}

shoe_size = {}


# person_1_name = input("Please enter name for person 1:\n").lower()
person_1_name = "Oscar".lower()
names[1] = person_1_name

# person_1_age = int(input("Please enter age for person 1:\n"))
person_1_age = 22
age[1] = person_1_age

# person_1_shoe_size = int(input("Please enter shoe size for person 1:\n"))
person_1_shoe_size = 44
shoe_size[1] = person_1_shoe_size


# person_2_name = input("Please enter name for person 2:\n").lower()
person_2_name = "David".lower()
names[2] = person_2_name

# person_2_age = int(input("Please enter age for person 2:\n"))
person_2_age = 45
age[2] = person_2_age

# person_2_shoe_size = int(input("Please enter shoe size for person 2:\n"))
person_2_shoe_size = 48
shoe_size[2] = person_2_shoe_size


# person_3_name = input("Please enter name for person 3:\n").lower()
person_3_name = "Bente".lower()
names[3] = person_3_name

# person_3_age = int(input("Please enter age for person 3:\n"))
person_3_age = 43
age[3] = person_3_age

# person_3_shoe_size = int(input("Please enter shoe size for person 3:\n"))
person_3_shoe_size = 40
shoe_size[3] = person_3_shoe_size


age_twist = {v: k for k, v in age.items()}
age_keys = sorted(age_twist, reverse=True)
highest_age_key = age_twist[age_keys[0]]
temp_key_1 = highest_age_key

print(f"The oldest person is {names[temp_key_1].title()} who has shoe size {shoe_size[temp_key_1]}")


shoe_size_twist = {v: k for k, v in shoe_size.items()}
shoe_size_keys = sorted(shoe_size_twist)
ssk_len = len(shoe_size_keys)
ssk_median = int(ssk_len / 2)
shoe_size_median = shoe_size_twist[shoe_size_keys[ssk_median]]
temp_key_2 = shoe_size_median

print(f"The person with median shoe size is {names[temp_key_2].title()} who is {age[temp_key_2]} years old")

# print(f"Please enter search value, name, age or size followed by value. i.e. 'age david'' - and remove quation
# marks.")

# print(f"Found person")

print(f"")