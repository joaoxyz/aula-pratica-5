import unittest, calc

class Tests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1, 5), 6)

    def test_sub(self):
        self.assertEqual(calc.sub(7, 5), 2)

    def test_mul(self):
        self.assertEqual(calc.mul(10, 2), 20)

    def test_div(self):
        self.assertEqual(calc.div(12, 3), 4)

if __name__ == "__main__":
    unittest.main()