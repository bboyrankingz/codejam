import unittest
from trampoline import jumps


class Test(unittest.TestCase):

    def test_jumps(self):
        self.assertEqual(jumps([0, 3, 0, 1, -3], lambda x: False, 5), 0)
        self.assertEqual(jumps([0, 3, 0, 1, -3], lambda x: False),  5)

    def test_jumps2(self):
        self.assertEqual(jumps([0, 3, 0, 1, -3], lambda x: x >= 3), 10)


if __name__ == '__main__':
    unittest.main()
