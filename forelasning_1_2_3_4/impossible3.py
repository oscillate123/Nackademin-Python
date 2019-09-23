# (a) capitalize()
# (b) join()
# (c) lower()
# (d) upper()
# (e) swapcase()
# (f) replace()
# (g) split()
# (h) rsplit()
# (i) title()
# (j) format()

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

"hårdkodade variabler":
"Jag tYcker om äGg!"
"SPAM!"
"äGg!"
"inte"
" "

"""


"""   --- ###   jAG tYCKER iNTE oM SPAM!  ### --- """


t_org = "Jag tYcker om äGg!"
t_spam = "SPAM!"
t_egg = "äGg!"
t_not = "inte"
space = " "
# hard coded variables

t_org = t_org.lower().title().swapcase()
t_not = t_not.lower().title().swapcase()
# make lowercase of all variables so we can more easy search later on


t1, t2, t3, t4 = t_org.rsplit(space)

t_org_m = t1 + space + t2 + space + t_not + space + t3 + space + t_spam

t_org_m = "".join(t_org_m)

print(t_org_m)
