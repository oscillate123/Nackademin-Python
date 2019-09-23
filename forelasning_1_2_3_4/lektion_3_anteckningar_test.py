"""

\ f
\ N {namn} - Unicode
\ r - början av raden
\ t - horisontell tab
\ v - vertikal tab
\ x {kod} - hexadecimal
\ u {16-bit} unicode
\ U {32-bit} unicode // inom {ska det skrivas kod}

Informationen på presentationen stämmer inte:
http://python-ds.com/python-3-escape-sequences

"""


string_1 = "test test1 test"

print(string_1.capitalize())
print(string_1.title())
print(string_1.upper())
print(string_1.lower())
print(string_1.find("test1"))
print(string_1)

string_2 = "abcdefghijklmnopqrstuvwxyz"
string_3 = "a b c d e f g h i j k l m n o p q r s t u v w x y z"

filtered = string_3.split(" ")
str1 = ''.join(str(e) for e in filtered)

range_of_letters = string_2[3:8]
print(range_of_letters)
print(filtered)
print(str1)
