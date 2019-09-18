import re


def is_number_valid(number):
    input_number = number

    if input_number.isdigit():
        return int(input_number)
    else:
        error_msg = "\nMobilnumret behöver bestå av siffror. "
        raise ValueError(error_msg)


def is_age_valid(age):
    input_age = age

    if input_age.isdigit():
        return int(input_age)
    else:
        error_msg = "\nÅldern behöver bestå av siffror. "
        raise ValueError(error_msg)


def is_email_valid(email):  # checking if email is valid with counting @'s and look for dot's
    input_mail = email

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
