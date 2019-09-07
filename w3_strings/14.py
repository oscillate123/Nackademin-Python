"""

14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words
 in sorted form (alphanumerically).

Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
# they've made a typo, for logical reasons, I assume they mean:
Expected Result : black, green, red, white

Re-using code from exercise 2 and 12, since its once again - counting items.

"""

sample_words = ["red", "white", "black", "red", "green", "black"]
sample_words.sort()

count = []

for item in sample_words:
    if item in count:
        continue
    else:
        count.append(item)

count = ", ".join(count)

print(count)
