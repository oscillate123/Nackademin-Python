"""

12. Write a Python program to count the occurrences of each word in a given sentence.

Re-used the code from exercise 2, and adjusted it for this exercise.

string = "google.com"
count = {}

for i in string:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(" Character count:" + "\n" + str(count))

"""

sentence = "ding pling sing king ding bing ding"
values = sentence.split(" ")

count = {}

for item in values:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1

print(count)
