import unittest
from hex import hex


class Test(unittest.TestCase):

    def test_hex(self):
        self.assertEqual(hex("ne,ne,ne"), 3)
        self.assertEqual(hex("ne,ne,sw,sw"), 0)
        self.assertEqual(hex("ne,ne,s,s"), 2)
        self.assertEqual(hex("se,sw,se,sw,sw"), 3)

    def test_same_hex(self):
        self.assertEqual(hex("ne,ne,s,s"), hex("se,se"))
        self.assertEqual(hex("se,sw,se,sw,sw"), hex("s,s,sw"))


if __name__ == '__main__':
    unittest.main()
