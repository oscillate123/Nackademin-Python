"""

16. Write a Python program to assess if a file is closed or not

"""

fh = open("test13.txt", "r")

if fh.closed:
    print("File is closed.")
else:
    print("File is open.")
