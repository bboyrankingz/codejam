import unittest
from digital_plumber import DigitalPlumber


class Test(unittest.TestCase):

    def test_plumber(self):
        plumber = DigitalPlumber({0: [2], 1: [1], 2: [0, 3, 4], 3: [2, 4], 4: [2, 3, 6], 5: [6], 6: [4, 5]})
        plumber.plumber()
        self.assertEqual(plumber.count, 6)

    def test_launch(self):
        plumber = DigitalPlumber({0: [2], 1: [1], 2: [0, 3, 4], 3: [2, 4], 4: [2, 3, 6], 5: [6], 6: [4, 5]})
        plumber.launch()
        self.assertEqual(plumber.group, 2)


if __name__ == '__main__':
    unittest.main()
