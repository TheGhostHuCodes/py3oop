import unittest

def average(seq):
    return sum(seq) / len(seq)

class CheckNumbers(unittest.TestCase):
    def test_int_float(self):
        self.assertEqual(1, 1.0)

    @unittest.expectedFailure
    def test_str_float(self):
        self.assertEqual("1", 1.0)

class TestAverage(unittest.TestCase):
    def test_python30_zero(self):
        self.assertRaises(ZeroDivisionError, average, [])

    def test_python31_zero(self):
        with self.assertRaises(ZeroDivisionError):
            average([])

if __name__ == "__main__":
    unittest.main()
