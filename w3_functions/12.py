"""

12. Write a Python function that checks whether a
passed string is palindrome or not.

Note: A palindrome is a word, phrase, or sequence that reads
the same backward as forward, e.g., madam or nurses run.

"""


def palindrome_check():
    user_input = input("Type a word or phrase:\n ")

    user_input = user_input.strip()
    check = list(user_input)
    check_r = list(reversed(check))

    if check_r == check:
        return print(f"{user_input} is a palindrome!")
    else:
        return print(f"{user_input} isn't a palindrome.")


palindrome_check()
