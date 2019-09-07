"""

13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.

"""

user_input = input("Type some text here: ")

user_input_lower = user_input.lower()
user_input_upper = user_input.upper()

print(f"\nYour text in lower case: {user_input_lower}")
print(f"Your text in upper case: {user_input_upper}")