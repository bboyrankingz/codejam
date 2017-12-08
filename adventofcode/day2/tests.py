import unittest
from checksum import checksum, checksum2, sumall


class Test(unittest.TestCase):

    def test_checksum_part1(self):
        self.assertEqual(checksum([5, 1, 9, 5]), 8)
        self.assertEqual(checksum([7, 5, 3]), 4)
        self.assertEqual(checksum([2, 4, 6, 8]), 6)

    def test_sumall_part1(self):
        self.assertEqual(sumall([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]], checksum), 18)

    def test_checksum_part2(self):
        self.assertEqual(checksum2([5, 9, 2, 8]), 4)
        self.assertEqual(checksum2([9, 4, 7, 3]), 3)
        self.assertEqual(checksum2([3, 8, 6, 5]), 2)

    def test_sumall_part1(self):
        self.assertEqual(sumall([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]], checksum2), 9)


if __name__ == '__main__':
    unittest.main()
