import unittest
from tubes import Tubes, parse_puzzle_line


class Test(unittest.TestCase):

    def test_parse_puzzle(self):
        puzzle = "F---|----E|--+"
        self.assertEqual(parse_puzzle_line(puzzle), ["F", "-", "-", "-", "|", "-", "-", "-", "-", "E", "|", "-", "-", "+"])

    def test_simple_tubes(self):
        tubes = Tubes([[" ", " ", " ", "|", " "], [" ", " ", " ", "|", " "], [" ", " ", " ", "A", " "], [" ", " ", " ", " ", " "]])
        tubes.start()
        self.assertEqual(tubes.path, "A")

    def test_direction_change_tubes(self):
        tubes = Tubes([[" ", "A", " ", "|", " "], [" ", "+", "-", "+", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "]])
        tubes.start()
        self.assertEqual(tubes.path, "A")

    def test_direction_change_into_outside_tubes(self):
        tubes = Tubes([["|", " ", " ", " ", " "], ["|", " ", " ", " ", " "], ["|", " ", " ", " ", " "], ["+", "-", "A", " ", " "]])
        tubes.start()
        self.assertEqual(tubes.path, "A")

    def test_direction_path_throw_a_tunnel(self):
        tubes = Tubes([["|", " ", " ", " ", " "], ["|", " ", "A", " ", " "], ["+", "-", "|", "-", "+"], [" ", " ", "|", " ", "|"], [" ", " ", "+", "-", "+"]])
        tubes.start()
        self.assertEqual(tubes.path, "A")


if __name__ == '__main__':
    unittest.main()
