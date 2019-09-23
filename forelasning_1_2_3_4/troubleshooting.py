print("Detta är mitt bästa program") # Här skriver jag ut en liten välkomsthälsning till användaren av detta program

A = int(input())

Ålder = int(A) # Skriv till fönster

#minInputVariabel = float(A)

print("Ålder", A)



"""
Comments on the written code:

1. Some "IDE":s doesn't support "non-ascii character", like å, ä, and ö.
1.a. If the IDE doesn't support non-ascii character, your code won't
run. Because the compiler can't read the Å,Ä,Ö etc, character.
2. Never name variables with non-ascii characters.
3. If you want someone to understand what the code does, make the documentation
and/or comments in English, since it is a universal language.
4. Define the variables in the start of your code (if possible), it is easier 
later on to understand what happens row by row, when you use your variable.
5. If you want the "user" to understand the console more, then you should ask
for input in the row containing: A = int(input("PUT TEXT HERE")).
Otherwise, there is a higher possibility that the user doesn't understand it 
is an input field/box.
6. Maybe a bit more explaining in the console output.
7. Use pep8 standard in the style of the code, then it will be more readable
later on for yourself and for other people.
8. Use better variables, variables with self explaining names.
9. Remove "Ålder = int(A) # Skriv till fönster" because it doesn't help us at all,
it only takes space. See suggestion below.
10. Remove "#minInputVariabel = float(A)" because it doesn't help us at all,
it only takes space. See suggestion below. Also, someone's age is almost never
measured with decimals. Not that I've heard of.


###  Suggestion on how to write the code instead: ###

print("This is my best application")
# This is a welcome phrase for the user

input_age = int(input("Please type your age and press enter: "))
# Here I ask the user to input their age.

print("Your age is: " + str(input_age))
# Here I print the users age, using the variable from where the input was stored.

"""