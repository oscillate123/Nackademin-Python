

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

    dash_less_number = original_number.replace("-", "")
    century_stripped_number = stripCentury(dash_less_number)
    return century_stripped_number


def doubleAndSum(number):
    """Doubles a number and adds the digits in it

    Takes an integer and doubles it, and then adds the numbers together. Will not work for numbers larger than 49"""

    number *= 2
    if number >= 10:
        number = number // 10 + number % 10
    return number


print(stripCentury("199708232898"))

user_input_strip = stripCentury("19970823--2898")

print(fixFormat(user_input_strip))

user_input_fix = fixFormat(user_input_strip)

print()
