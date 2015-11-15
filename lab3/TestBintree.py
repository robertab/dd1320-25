import unittest
from Bintree import Bintree, putta, Node

class TestBintree(unittest.TestCase):

    def testBintree_without_args(self):
        svenska = Bintree()

    def test_putta_nar_tom(self):
        svenska = Bintree()
        svenska.put(1)
        self.assertEqual(1, svenska.root.value)

    def test_putta_nar_ej_tom_med_varde_mindre_an_rotens(self):
        svenska = Bintree()
        svenska.put(3)
        svenska.put(2)
        self.assertEqual(2, svenska.root.left.value)

    def test_putta_nar_ej_tom_med_varde_storre_an_rotens(self):
        svenska = Bintree()
        svenska.put(1)
        svenska.put(3)
        svenska.put(4)
        svenska.put(5)
        self.assertEqual(5, svenska.root.right.right.right.value)


    def test_finns_med_givna_varden(self):
        svenska = Bintree()
        svenska.put(1)
        self.assertEqual(True, svenska.__contains__(1))
        


if __name__ == '__main__':
    unittest.main()
    

