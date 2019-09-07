
# definerar funktionen xxx, funktionen kräver 2 variabler
# för att fungera
def xxx(n, k):
    return sum([num % k for num in range(n+1)])
    # i en funktion behöver vi returnera något, därav "return"
    # sum, används för att summera ihop något
    # sum(här kan vi skriva t.ex. en lista och summera den)
    # istället för att skapa en lista manuellt så kan vi skapa en
    # med "list comprehension"
    # list comprehension funkar såhär:
    # [gör detta - för varje sak i den här listan - om detta krav är mött]
    # delen "om detta krav är mött" MÅSTE INTE vara med, men "gör detta" och "för varje sak i
    # den här listan" måste vara med i en "list comprehension" för att den ska fungera.
    # lite som att, list comprehension är en funktion, som kräver två saker, och tredje är "optional"
    # ex. på list comprehension [each_item/2 for each_item in example_list]
    # i vårt fall: [num modulus k, för varje num i range 0 till, inmatningssiffran n + 1 ]
    # och varför vi vill göra range 0 till inmatningssiffran n + 1, är för att om man
    # använder "range funktionen" så tar den 1 eller två variabler.
    # range(2, 5) ger oss siffrorna 2, 3 och 4. Av någon skev anledning så ger den inte oss
    # siffran som är i slutet. Se det som: range(start, slut - 1)
    # men om du skriver: range(5), så kommer den ge oss 0, 1, 2, 3 och 4
    # varför - idk... :P
    # men så varför vi skriver range(n+1) är för att om n = 6
    # då vill vi testa köra modulus på nummer 6 också såklart!
    # därav, måste vi skriva n + 1, annars kommer range(n) (om n = 6) ge:
    # range(n) = 0, 1, 2, 3, 4 och 5. Eftersom att det är 6 st värden!
    # och skillnaden på 6 st värden och värdet 6 kommer ta ännu mer tid att förklara
    # för att summera:

    # funktion xxx behöver två inmatningsvärden, och inmatningsvärdena kommer kallas "n" & "k":
        # funktionen ska göra följande:
        # returnera summan av:
        # för varje nummer i spannet mellan 0 och funktionens inmatningsvärde "n" + 1
        # ta det nummret vi har fått ut av föregående spann (när vi loopar igenom det),
        # och kör modulus på det.
        # modulus siffran, deffineras av funktionens inmatningsvärde "k"

    # kommentar, det är inte exakt i den ordningen det sker, men det är vad som händer.


print(xxx(6, 2))
