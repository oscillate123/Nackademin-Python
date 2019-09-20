import forelasning_8.personnummer_simon as pnummer_control
import unittest


class TestCase(unittest.TestCase):

    def test_strip_century(self):
        p_number = pnummer_control.user_input()
        the_func = pnummer_control.stripCentury(number=p_number)
        if len(p_number) > 10:
            self.assertEqual(len(the_func), len(p_number)-4, msg="Function not working")
        elif len(p_number) < 11:
            self.assertEqual(len(the_func), len(p_number), msg="Function not working")


if __name__ == '__main__':
    unittest.main()
