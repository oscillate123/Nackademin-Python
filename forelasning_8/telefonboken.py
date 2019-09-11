import re


def get_name():
    person_name = input("\nVad heter personen? ")

    if person_name == "":
        print("Du har valt att avsluta koden. Välkommen åter.")
        exit()

    return person_name.lower()


def control_name(input_name):

    if input_name in PhoneBook.phone_book:
        return print(PhoneBook.phone_book[input_name])
    elif input_name not in PhoneBook.phone_book:
        print("Vi kan inte hitta personen. Vi ska lägga till personen. ")
        add_person(input_name)


def add_person(input_name):
    person_name = input_name
    person_number = is_number_valid()
    person_email = is_email_valid()
    person_age = is_age_valid()

    make_person = Person(person_name, person_number, person_email, person_age)
    person_info = {"Name": make_person.person_name.title(),
                   "Number": make_person.person_number,
                   "Email": make_person.person_email,
                   "Age": make_person.person_age}

    PhoneBook(person_name, person_info)

    return


def is_number_valid():
    input_number = input("Vad är personens mobilnummer? ")

    if input_number.isdigit():
        return int(input_number)
    else:
        error_msg = "\nMobilnumret behöver bestå av siffror. "
        raise ValueError(error_msg)


def is_age_valid():
    input_age = input("Vad är personens mobilnummer? ")

    if input_age.isdigit():
        return int(input_age)
    else:
        error_msg = "\nÅldern behöver bestå av siffror. "
        raise ValueError(error_msg)


def is_email_valid():  # checking if email is valid with counting @'s and look for dot's
    input_mail = input("Vad är personens mailadress? ")

    find_dot = bool(re.search("[.]", input_mail))
    find_at = input_mail.count("@")
    # gets True if there is a dot in the mailadress

    if not find_dot and not find_at == 1:
        error_msg = "\nMailadressen behöver bestå av minst en punkt och ett @-tecken, för att vara giltigt. "
        raise ValueError(error_msg)
    elif not find_dot:
        error_msg = "\nMailadressen behöver bestå av minst en punkt, för att vara giltig. "
        raise ValueError(error_msg)
    elif not find_at == 1:
        error_msg = "\nMailadressen behöver bestå av ett @-tecken, för att vara giltig. "
        raise ValueError(error_msg)
    else:
        return input_mail


class PhoneBook:

    phone_book = {}
    # phone_book = {"Oscar": person_info}

    def __init__(self, person_name, person_info):
        self.person_name = person_name
        self.person_info = person_info
        PhoneBook.phone_book[person_name] = person_info


class Person:

    def __init__(self, person_name, person_number, person_email, person_age):
        self.person_name = person_name
        self.person_number = person_number
        self.person_email = person_email
        self.person_age = person_age


while len(PhoneBook.phone_book):

    try:
        control_name(get_name())
    except ValueError as error:
        print(error)
