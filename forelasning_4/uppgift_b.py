"""

Projektledaren för ditt utvecklingsteam kommer till dig och vill att du ska skriva ett program.

Programmet har en kravspecifikation enligt punkterna 1-4 nedan.
Projektledaren kan inteprogrammera så för att hen ska kunna läsa din kod ber hen dig att undvika:
 att användaloopar och if-satser, om du kan.

 1.Programmet ska vara icke-case-sensitive. Det ska alltså inte spela någon roll om användaren använder stora eller
 små bokstäver. Namn som skrivs ut ska dock alltid börja med stor bokstav.

 2.Programmet ska låta användaren mata in tre personers namn, ålder och skostorlek. Dessa uppgifter måste sparas
 under programmets körning.

 3.Programmet ska sedan skriva ut namn och skostorlek på den person som är äldst samt namn
 och ålder på den som har medianskostorlek.

 4.Efter det ska användaren kunna söka efter personer genom att mata in en av de tre datatyperna. Om programmet
 hittar någon som matchar ska denneskompletta uppgifter skrivas ut.


Please enter name for person1>
ahmed
Please enter age for person 1
>25
Please enter shoe size for person 1
>42

Please enter name for person 2
>DIANA
Please enter age for person 2
>40
Please enter shoe size for person 2
>38

Please enter name for person 3
>Casper
Please enter age for person 3
>30
Please enter shoe size for person 3
>45


The oldest person is Diana who has shoe size 38
The person with median shoe size is Ahmed who is 25 years old

 Please enter search value, name, age or size followed by value
 >age 30
 Found person
    Name: Casper
    Age: 30
    Size: 45

"""

persons_dict = {
    "name1": "",
    "age1": "",
    "shoe_size1": "",

    # dictionary for storing information regarding person 1


    "name2": "",
    "age2": "",
    "shoe_size2": "",

    # dictionary for storing information regarding person 2


    "name3": "",
    "age3": "",
    "shoe_size3": "",

    # dictionary for storing information regarding person 3
}


person_1_name = input("Please enter name for person 1:\n").lower()
persons_dict["name1"] = person_1_name

person_1_age = int(input("Please enter age for person 1:\n"))
persons_dict["age1"] = person_1_age

person_1_shoe_size = int(input("Please enter shoe size for person 1:\n"))
persons_dict["shoe_size1"] = person_1_shoe_size
# collecting information from user input and assigning it to each dictionary key, for person 1

print(persons_dict)


person_2_name = input("Please enter name for person 2:\n").lower()
persons_dict["name2"] = person_2_name

person_2_age = int(input("Please enter age for person 2:\n"))
persons_dict["age2"] = person_2_age

person_2_shoe_size = int(input("Please enter shoe size for person 2:\n"))
persons_dict["shoe_size2"] = person_2_shoe_size
# collecting information from user input and assigning it to each dictionary key, for person 2


print(persons_dict)


person_3_name = input("Please enter name for person 3:\n").lower()
persons_dict["name3"] = person_3_name

person_3_age = int(input("Please enter age for person 3:\n"))
persons_dict["age3"] = person_3_age

person_3_shoe_size = int(input("Please enter shoe size for person 3:\n"))
persons_dict["shoe_size3"] = person_3_shoe_size
# collecting information from user input and assigning it to each dictionary key, for person 3


print(persons_dict)


if persons_dict["age1"] > persons_dict["age2"] & persons_dict["age1"] > persons_dict["age3"]:
    name1 = persons_dict["name1"].title()
    shoe_size1 = persons_dict["shoe_size1"]
    print(f"The oldest person is {name1} who has shoe size {shoe_size1}")
elif persons_dict["age2"] > persons_dict["age1"] & persons_dict["age2"] > persons_dict["age3"]:
    name2 = persons_dict["name2"].title()
    shoe_size2 = persons_dict["shoe_size2"]
    print(f"The oldest person is {name2} who has shoe size {shoe_size2}")
else:
    name3 = persons_dict["name3"].title()
    shoe_size3 = persons_dict["shoe_size3"]
    print(f"The oldest person is {name3} who has shoe size {shoe_size3}")

