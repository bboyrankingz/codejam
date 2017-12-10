import unittest
from anagrams import anagram


class Test(unittest.TestCase):

    def test_anagrams(self):
        self.assertTrue(anagram("abcde fghij"))
        self.assertFalse(anagram("abcde xyz ecdab"))
        self.assertTrue(anagram("a ab abc abd abf abj"))
        self.assertTrue(anagram("iiii oiii ooii oooi oooo"))
        self.assertFalse(anagram("oiii ioii iioi iiio"))


if __name__ == '__main__':
    unittest.main()
