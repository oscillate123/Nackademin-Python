def user_input():

    response = input("Skriv in ett personnummer du vill testa, eller ett ofullständigt som du vill generera:")

    if len(response) < 8:
        print("Input är för kort!")
        user_input()

    if len(response) > 14:
        print("Input är för långt!")
        user_input()

    return response


def stripCentury(number):
    """Strips the number of the century

    Sometimes, personnummer is written including century.
    This is not included in the algorithm for calculating the
    final digit, and thus is removed by this function."""

    if len(number) < 11:
        return number
    else:
        return number[2:]


def fixFormat(original_number):
    """Format the number in a predictable way.

    Fixes the problem with different ways of formatting the number.
    The resulting format is always yymmddnnn or yymmddnnnn depending on the
    input."""

    dashless_number = original_number.replace("-", "")
    century_stripped_number = stripCentury(dashless_number)

    if not century_stripped_number.isdigit():
        print("Input innehåller något annat än siffror och bindestreck!")
        user_input()

    return century_stripped_number


def indexValueMod(number, index):
    """Doubles a number and adds the digits in it to the list numbers, which we return

    Takes an integer and doubles it, and then adds the numbers together. """

    numbers = []

    if index < 9:
        if (index % 2) == 0:  # if index 'X' value of personnummer is even, we multiply that index by 2

            number *= 2

            if number >= 10:
                # number = (number // 10) + (number % 10)
                number1 = (number // 10)  # first number in the double digit number
                number2 = (number % 10)  # second number in the double digit number
                numbers.append(number1)  # return them as i.e. str 1 and str 8, instead of int 18.
                numbers.append(number2)
            else:
                numbers.append(number)

        else:  # else, we multiply with 1
            numbers.append(number)

        return numbers

    else:

        return numbers


def calculateControlDigit(number):
    """Calculate the control digit for a personnummer

    The control digit is calculated by multiplying every other number by two, (Starting with the first) then adding the separate digits. The control digit is then the difference
    between that sum and the closest higher multiple of ten. E.g. if the sum is 44, the control digit will be 50-44=6"""

    # Make it easier to handle individual digits
    number_as_string = str(number)

    cumulative_sum_numbers = []

    # Enumerate makes a tuple of index and element
    for index, digit in enumerate(number_as_string):
        # Make calculations possible
        current_digit = int(digit)

        # using indexValueMod function, if index is even, the digit is multiplied
        current_digit_multiplied = indexValueMod(current_digit, index)

        # list comprehension for appending each number generated in indexValueMod function
        [cumulative_sum_numbers.append(num) for num in current_digit_multiplied]

    cumulative_sum = sum(cumulative_sum_numbers)

    # This is equivalent to taking the following multiple of ten minus the number
    control_digit_last_digit = 10 - (cumulative_sum % 10)

    return control_digit_last_digit


def printControlDigitMatch(personnummer, control_digit):
    last_digit = (int(personnummer) % 10)
    if last_digit == control_digit:
        print("Personnumrets kontrollsiffra stämmer!")
    else:
        print(f"Personnumrets kontrollsiffra stämmer INTE!\nDen ska vara {control_digit}, men är {last_digit}")


# This statement means that the code below will not run if imported.
# This is good when running automated tests, which we will cover later
if __name__ == "__main__":

    personnummer = user_input()
    personnummer = fixFormat(personnummer)
    control_digit = calculateControlDigit(personnummer)

    if len(personnummer) == 10:
        printControlDigitMatch(personnummer, control_digit)
    elif len(personnummer) == 9:
        print(f"Det fullständiga personnumret är: {personnummer}{control_digit}")
