import unittest
from generators import gen, to_binary, compare


class Test(unittest.TestCase):

    def test_gen(self):
        self.assertEqual([_ for _ in gen(65, 16807)], [1092455, 1181022009, 245556042, 1744312007, 1352636452])

    def test_binary(self):
        self.assertEqual([_ for _ in to_binary(gen(65, 16807))], ["00000000000100001010101101100111",
                                                                  "01000110011001001111011100111001",
                                                                  "00001110101000101110001101001010",
                                                                  "01100111111110000001011011000111",
                                                                  "01010000100111111001100000100100"])

    def test_compare(self):
        self.assertEqual(len([_ for _ in compare(to_binary(gen(65, 16807)), to_binary(gen(8921, 48271)))]), 1)

    def test_compare_40_000_000(self):
        self.assertEqual(len([_ for _ in compare(to_binary(gen(65, 16807, 40000000)), to_binary(gen(8921, 48271, 40000000)), 40000000)]), 588)


if __name__ == '__main__':
    unittest.main()
