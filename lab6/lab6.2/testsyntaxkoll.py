""" 
Kurs: DD1320/25 Tillämpad datalogi med Etik
Författare: Robert Åbert, Sara Ervik, CDATE_2.
Uppgift: Lab6.1
"""
###from main import *
#from labb62 import *
import unittest
from l6 import *

class TestSyntaxKoll(unittest.TestCase):
    """Testar olika fall som ska funka"""
    def testing_Na(self):
        self.assertEqual(readFormula("Na"), 'Formeln är syntaktiskt korrekt')
    def testing_H20(self):
        self.assertEqual(readFormula("H2O"), "Formeln är syntaktiskt korrekt")
    def testing_Si_C3_COOH_2_4_H2O_7(self):
        self.assertEqual(readFormula("Si(C3(COOH)2)4(H2O)7"), "Formeln är syntaktiskt korrekt")
    def testing_Na332(self):
        self.assertEqual(readFormula("Na332"), 'Formeln är syntaktiskt korrekt')


    """Testar fall som inte ska funka"""
    def testing_invalid_group_C_X_x_4_5(self):
        self.assertEqual(readFormula("C(Xx4)5"), "Okänd atom vid radslutet 4)5")
    def testing_invalid_group_C_O_H_4_C(self):
        self.assertEqual(readFormula("C(OH4)C"), "Saknad siffra vid radslutet C")
    def testing_invalid_group_C_O_H_4_C_nr_2(self):
        self.assertEqual(readFormula("C(OH4C"), "Saknad högerparentes vid radslutet ")
    def testing_invalid_group_H_2_0_F_e(self):
        self.assertEqual(readFormula("H2O)Fe"), "Felaktig gruppstart vid radslutet )Fe")
    def testing_invalid_group_H_0(self):
        self.assertEqual(readFormula("H0"), 'För litet tal vid radslutet ') #Dumt jävla mellanslag
    def testing_invalid_group_H_1_C(self):
        self.assertEqual(readFormula("H1C"), "För litet tal vid radslutet C")
    def testing_invalid_group_H_0_2_C(self):        
        self.assertEqual(readFormula("H02C"), "För litet tal vid radslutet 2C")
    def testing_invalid_group_no_cap_letter(self):        
        self.assertEqual(readFormula("Nacl"), "Saknad stor bokstav vid radslutet cl")
    def testing_invalid_group_no_cap_letter_2(self):        
        self.assertEqual(readFormula("a"), "Saknad stor bokstav vid radslutet a")
    def testing_wrong_start_0(self):
        self.assertEqual(readFormula("(Cl)2)3"), "Felaktig gruppstart vid radslutet )3")
    def testing_wrong_start(self):
        self.assertEqual(readFormula(")"), "Felaktig gruppstart vid radslutet )")
    def testing_wrong_start_2(self):
        self.assertEqual(readFormula("2"), "Felaktig gruppstart vid radslutet 2")



if __name__ == '__main__':
    unittest.main()

