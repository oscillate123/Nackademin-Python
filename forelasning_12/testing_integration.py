import forelasning_8.personnummer_simon as pnummer_control
import unittest


class TestCase(unittest.TestCase):

    def test_fixFormat(self):
        # TODO dependencies - stripCentury 2019.09.20
        number = "199708-2328"
        fixed_number = pnummer_control.fixFormat(number)
        self.assertNotIn("-", fixed_number, msg=" '-' finns kvar efter funktionen")

    def test_calculate_control_digit(self):
        # TODO dependencies - fixFormat 2019.09.20
        number_10_digits = "9708232898"
        number_09_digits = "970823289"

        pass


if __name__ == '__main__':
    unittest.main()



"""

    # Make it easier to handle individual digits
    number_as_string = str(number)

    cumulative_sum = 0
    
    # Enumerate makes a tuple of index and element
    for index, digit in enumerate(number_as_string):

        # Make calculations possible
        current_number = int(digit)
        
        if index % 2 == 0:
            current_number = doubleAndSum(current_number)

        cumulative_sum += current_number
            
    #This is equivalent to taking the following multiple of ten minus the number
    control_digit = (10 - (cumulative_sum % 10))%10

    return control_digit

"""