import unittest
from registers import Register


class Test(unittest.TestCase):

    def test_parse_modify(self):
        self.assertEqual(Register().parse_modify("b inc 5"), ("b", 5))
        self.assertEqual(Register().parse_modify("a inc 1"), ("a", 1))
        self.assertEqual(Register().parse_modify("c dec -10"), ("c", 10))
        self.assertEqual(Register().parse_modify("c inc -20"), ("c", -20))

    def test_parse_condition(self):
        self.assertFalse(Register().parse_condition("a > 1"))
        self.assertTrue(Register().parse_condition("b < 5"))
        self.assertTrue(Register({"a": 1}).parse_condition("a >= 1"))
        self.assertTrue(Register({"c": 10}).parse_condition("c == 10"))

    def test_register(self):
        self.assertEqual(Register().register("b inc 5 if a > 1"), {"a": 0, "b": 0})


if __name__ == '__main__':
    unittest.main()
