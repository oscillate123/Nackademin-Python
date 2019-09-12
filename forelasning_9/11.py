"""

11. Write a Python program to get the file size of a plain file.

"""

import os

file = "text1.txt"

file_size = os.stat(file).st_size

print(file_size)
