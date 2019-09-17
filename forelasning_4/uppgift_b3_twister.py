name = {}

age = {}

shoe_size = {}

person_info = {"name": name, "age": age, "size": shoe_size}


person_1_name = input("Please enter name for person 1:\n").lower()
# person_1_name = "Oscar".lower()
name[1] = person_1_name

person_1_age = int(input("Please enter age for person 1:\n"))
# person_1_age = "22"
age[1] = person_1_age

person_1_shoe_size = int(input("Please enter shoe size for person 1:\n"))
# person_1_shoe_size = "44"
shoe_size[1] = person_1_shoe_size


person_2_name = input("Please enter name for person 2:\n").lower()
# person_2_name = "Karl".lower()
name[2] = person_2_name

person_2_age = int(input("Please enter age for person 2:\n"))
# person_2_age = "45"
age[2] = person_2_age

person_2_shoe_size = int(input("Please enter shoe size for person 2:\n"))
# person_2_shoe_size = "48"
shoe_size[2] = person_2_shoe_size


person_3_name = input("Please enter name for person 3:\n").lower()
# person_3_name = "Annika".lower()
name[3] = person_3_name

person_3_age = int(input("Please enter age for person 3:\n"))
# person_3_age = "43"
age[3] = person_3_age

person_3_shoe_size = int(input("Please enter shoe size for person 3:\n"))
# person_3_shoe_size = "40"
shoe_size[3] = person_3_shoe_size


age_twist = {v: k for k, v in age.items()}
age_keys = sorted(age_twist, reverse=True)
highest_age_key = age_twist[age_keys[0]]
temp_key_1 = highest_age_key
print(f"\nThe oldest person is {name[temp_key_1].title()} who has shoe size {shoe_size[temp_key_1]}")


shoe_size_twist = {v: k for k, v in shoe_size.items()}
shoe_size_keys = sorted(shoe_size_twist)
ssk_len = len(shoe_size_keys)
ssk_median = int(ssk_len / 2)
shoe_size_median = shoe_size_twist[shoe_size_keys[ssk_median]]
temp_key_2 = shoe_size_median
print(f"\nThe person with median shoe size is {name[temp_key_2].title()} who is {age[temp_key_2]} years old")


search_input = input("\n\nPlease enter search value, name, age or size followed by value.\n")
search_list = search_input.split(" ")
cmd1 = search_list[0]
cmd2 = search_list[1]
string_twist = {v: k for k, v in person_info[cmd1].items()}
string_find_person = int(string_twist[cmd2])
print_msg1 = "Found person"
found_person_name = person_info["name"][string_find_person].title()
found_person_age = person_info["age"][string_find_person]
found_person_shoe_size = person_info["size"][string_find_person]
print(f"\n Name: {found_person_name}\n  Age: {found_person_age}\n Size: {found_person_shoe_size}")
