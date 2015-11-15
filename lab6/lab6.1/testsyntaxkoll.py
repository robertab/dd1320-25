import unittest
from specc import *



class TestSyntaxKoll(unittest.TestCase):


    def test_upper_case_letter(self):
        self.assertEqual(check_cap_letter("A"), "Syntaktiskt korrekt")
        self.assertEqual(check_cap_letter("q"), "Fel!")

    def test_lower_case_letter(self):
        self.assertEqual(check_lower_letter("c"), "Syntaktiskt korrekt" )
        self.assertEqual(check_lower_letter("S"), "Fel!")
        self.assertEqual(check_lower_letter("ab"), "Fel!")

    def test_if_number_is_int_and_greater_than_1(self):
        self.assertEqual(check_num(4), "Syntaktiskt korrekt")
        self.assertEqual(check_num(0), "Fel!")
        
        




if __name__ == '__main__':
    unittest.main()

