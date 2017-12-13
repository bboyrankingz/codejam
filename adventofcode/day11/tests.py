import unittest
from hex import hex


class Test(unittest.TestCase):

    def test_hex(self):
        self.assertEqual(hex("ne,ne,ne")[1], 3)
        self.assertEqual(hex("ne,ne,sw,sw")[1], 0)
        self.assertEqual(hex("ne,ne,s,s")[1], 2)
        self.assertEqual(hex("se,sw,se,sw,sw")[1], 3)

    def test_same_hex(self):
        self.assertEqual(hex("ne,ne,s,s")[1], hex("se,se")[1])
        self.assertEqual(hex("se,sw,se,sw,sw")[1], hex("s,s,sw")[1])


if __name__ == '__main__':
    unittest.main()
