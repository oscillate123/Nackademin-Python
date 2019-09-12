"""

3. Write a Python program to append text to a file and display the text.

"""

fh = open("text1.txt", "a")
fh.write("\ntest task 4")
fh.close()

fh1 = open("text1.txt", "r")
print(fh1.read())
fh1.close()
