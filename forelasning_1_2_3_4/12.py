# Skapa ett program som frågar om två strängar och sedan skriver ut dem
# på varsin rad, omgivna av citationstecken med ett och samma printkommando

input_string_1 = input("Vänligen skriv valfri text.")
input_string_2 = input("Vänligen skriv valfri text igen.")

print(f"Det du skrev var: \"{input_string_1}\" och \"{input_string_2}\".")

"""

\ f
\ N {namn} - Unicode
\ r - början av raden
\ t - horisontell tab
\ v - vertikal tab
\ x {kod} - hexadecimal
\ u {16-bit} unicode
\ U {32-bit} unicode // inom {ska det skrivas kod}

Sekvens Betyder
\ ' '
\ 
\ \ \
\ a Varningsljud i vissa terminaler
\ b Baksteg
\ f Form-feed (ny rad)
\ n Ny rad och gå till början
Sekvens Betyder
\ N{namn} Unicode efter namn
\ r Gå till början av raden
\ t Horisontell tab
\ v Vertikal tab
\ u{unicode} 16-bit unicode
\ U{unicode} 32-bit unicode
\ 0  {kod} Oktalt teckenkod
\ x{kod} Hexadecimal teckenkod


"""

print("text \a asdf")
print("text \\ asdf")
print("text \' asdf")
print("text \f asdf")
print("text \f asdf")
print("text \n asdf")
print("text \n asdf")
# print("text \u{U+00C4} asdf")
print("text \r asdf")
print("text \r asdf")
print("text \t asdf")
print("text \t asdf")
print("text \v asdf")
print("text \v asdf")
# print("text \x{} asdf")


