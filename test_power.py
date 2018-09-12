import unittest

from day4_power import power


class test_calc(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(2,4),16)

    def test_type_input(self):
        self.assertEqual(power(8,'a'),'invalid type for opperand')
    


if __name__ == '__main__':
    unittest.main()
    