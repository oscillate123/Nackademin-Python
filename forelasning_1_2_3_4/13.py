"""

1. Öppna en ny l enligt tidigare övningar.
2. Skriv ett program som tar emot två strängar från användaren
3. Skapa en ny sträng med enkla citationstecken runt den första strängen,
dubbla runt den andra samt en ny rad mellan dem. Så här:
'Första strängen'
"Andra strängen"
4. Skriv ut den nya strängen som svar.
5. Provkör och se hur resultatet blir.
6. Testa dig igenom alla escape-sekvenser nämnda i presentationen genom en
serie print-kommandon. (Teckenkoder

"""



input_string_1 = input("Vänligen skriv valfri text.")
input_string_2 = input("Vänligen skriv valfri text igen.")

output_strings = (f"\n '{input_string_1}'\n \"{input_string_2}\"")

print(output_strings)
