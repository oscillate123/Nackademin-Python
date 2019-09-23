"""
3.2 Uppgifter
1. Skriv ett program som börjar med strängen Jag tYcker om äGg! och i
slutändan skriver ut strängen jAG tYCKER iNTE oM SPAM!

3.2.1 Specikationer
1. Endast startsträngen, strängen inte och strängen SPAM ska vara hårdkodade.
2. Programmet ska inte ta någon användarinput
3. Följande strängmetoder får användas:
(a) capitalize()
(b) join()
(c) lower()
(d) upper()
(e) swapcase()
(f) replace()
(g) split()
(h) rsplit()
(i) title()
(j) format()
4. Programmet ska skriva ut vad som gjorts samt hur strängen ser ut efter
varje genomförd rad.


txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


 txt = "I like bananas"
x = txt.replace("bananas", "apples")


 myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)

"""

task_string_1 = "Jag tYcker om äGg!".rsplit(" ")
task_string_2 = "jAG tYCKER iNTE oM SPAM!".rsplit(" ")

variables = (task_string_1[0].capitalize().swapcase(),
            task_string_1[1].capitalize().swapcase(),
             task_string_2[2].capitalize().swapcase(),
             task_string_1[2].capitalize().swapcase(),
             task_string_2[4],)

final_answer = (f"{variables[0]} {variables[1]} {variables[2]} {variables[3]} {variables[4]} ")

print(final_answer)

t_1 = "Jag tYcker om äGg!"
t_2 = "jAG tYCKER iNTE oM SPAM!"
t_3 = "SPAM!"
t_4 = "äGg!"

