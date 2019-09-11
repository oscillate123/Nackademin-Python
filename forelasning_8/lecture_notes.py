import re

#
# string = "01234567891"
#
# print(string[1:])

x = "oscar.jacobsson@yh.nackademin.se"

find_dot = re.match("[.]", x)

if bool(re.search("[.]", x)):
    print(True)
else:
    print(False)