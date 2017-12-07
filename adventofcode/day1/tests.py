import unittest
from inverse_captcha import captcha, captcha2


class Test(unittest.TestCase):

    def test_captcha_part1(self):
        self.assertEqual(captcha([1, 1, 2, 2]), 3)
        self.assertEqual(captcha([1, 1, 1, 1]), 4)
        self.assertEqual(captcha([1, 2, 3, 4]), 0)
        self.assertEqual(captcha([9, 1, 2, 1, 2, 1, 2, 9]), 9)

    def test_captcha_part2(self):
        self.assertEqual(captcha2([1, 2, 1, 2]), 6)
        self.assertEqual(captcha2([1, 2, 2, 1]), 0)
        self.assertEqual(captcha2([1, 2, 3, 4, 2, 5]), 4)
        self.assertEqual(captcha2([1, 2, 3, 1, 2, 3]), 12)
        self.assertEqual(captcha2([1, 2, 1, 3, 1, 4, 1, 5]), 4)


if __name__ == '__main__':
    unittest.main()
