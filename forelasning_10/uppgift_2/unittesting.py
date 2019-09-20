import unittest
import forelasning_10.uppgift_2.team as team_file
import forelasning_10.uppgift_2.main as main_file


class TestCase(unittest.TestCase):

    def test_Returning_team(self):
        read_test = main_file.file_read("PL_1819.csv")
        del read_test[0]
        for match in read_test:
            x = team_file.Team(match)
            integer = x.goal_difference()
            text = x.counter()

            self.assertTrue(type(integer) == int, "Not returning goal_difference")
            if text is str:
                self.assertIsInstance(text, str)
            elif text is None:
                pass

    def test_Table_maker(self):
        pass


if __name__ == '__main__':
    unittest.main()
