import unittest
from stream_processing import stream


class Test(unittest.TestCase):

    def test_stream(self):
        self.assertEqual(stream("{}"), 1)
        self.assertEqual(stream("{{},{}}"), 5)
        self.assertEqual(stream("{{{}}}"), 6)
        self.assertEqual(stream("{{{},{},{{}}}}"), 16)


if __name__ == '__main__':
    unittest.main()
