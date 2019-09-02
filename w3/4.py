"""
4. Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$',
 except the first char itself. Go to the editor
Sample String : 'restart'
Expected Result : 'resta$t'
Click me to see the sample solution
"""

# simple quotation marks are 'variables' and double quotation marks are hardcoded strings "some text"

string = "titanium tank trunk"
# string

first_char = string[0]
# take the first character and store it

def change(word):
    return ''.join(c if c != word[0] else '$' for c in word)
# function with one liner to change all characters that are the same as 'first_char' to "$"

y = change(string)
# using the function on the string and then store it in a variable

z = y.replace("$", first_char, 1)
# replace the first character in the modified string to the original first character

print(z)
# print result of 'z'


# MOST EFFECTIVE:


def change_word(word):
    a = word[0]
    word = word.replace(a, "$")
    word = a + word[1:]
    return word


print(change_word("restart"))
# doing the same operation as before, but a bit more effective
