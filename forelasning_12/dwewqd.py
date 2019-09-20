import forelasning_8.personnummer_simon as pnummer_control
import unittest
import forelasning_12.unit_testing_pnummer as enhettest


class TestCase(unittest.TestCase):

    def test_strip_century(self):
        p_number = enhettest.TestCase.test_strip_century()
        the_func = pnummer_control.stripCentury(number=p_number)
        print(p_number)


if __name__ == '__main__':
    unittest.main()
