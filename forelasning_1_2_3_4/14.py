"""

2.2 Uppgifter
1. Skapa ett program som frågar efter två tal och skriver ut summan, diferensen,
produkten och kvoten av talen.
2.2.1 Specikationer
1. Det ska vara tydligt för användaren vilken input som förväntas, samt vilket
svar som är vilket
2. Presentationen av resultaten för de olika räknesätten ska använda sig av
olika metoder för stränginterpolation, det vill säga:
(a) Strängkonkatenering
(b) %-operatorn
(c) .format-sträng
(d) f-sträng
3. Koden ska vara lättläst och begriplig även för någon som inte på förhand
känner till vad koden ska göra.


"""

n = "\n "
# linebreak as a variable

print("Vi ska utföra matematiska operationer med två tal.")
input_string_1 = int(input("Vänligen skriv tal ett här -> "))
input_string_2 = int(input("Vänligen skriv tal två här -> "))
# user input

math_add = input_string_1 + input_string_2
math_sub = input_string_1 - input_string_2
math_multi = input_string_1 * input_string_2
math_divide = input_string_1 / input_string_2
# math operations

output_strings_a = "Strängkonkatenering: \n "
output_strings_a += str(math_add) + n +  str(math_sub) + n + str(math_multi) + n + str(math_divide)
# storing variables as strings in the variable output_strings_a
# appending variables, for easier readability in the output.

output_strings_b = ("Med %%-formatering: \n %s" %(math_sub))
output_strings_c = (
      "Om vi använder .format{{}} istället: \n {int1}".format(int1=math_multi))
output_strings_d = f"Enklast är att använda sig av f\"\n {math_divide}"


print(output_strings_a)
print(output_strings_b)
print(output_strings_c)
print(output_strings_d)

