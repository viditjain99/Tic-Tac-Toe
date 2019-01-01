#Vidit Jain
#2017370
#A2
import unittest
from a2 import game1
from a2 import game2
from a2 import game3
from a2 import validmove
from a2 import validBoard

# TEST cases should cover the different boundary cases.

class testpoint(unittest.TestCase):
    
        def test_game1(self):
            self.assertAlmostEqual(game1(1000),0.35,delta=0.11)
            self.assertAlmostEqual(game1(10000),0.35,delta=0.11)
            self.assertAlmostEqual(game1(100),0.35,delta=0.11)
            self.assertAlmostEqual(game1(5000),0.35,delta=0.11)
            self.assertAlmostEqual(game1(100000),0.35,delta=0.11)

        def test_game2(self):
            self.assertAlmostEqual(game2(1000),0.075,delta=0.1)
            self.assertAlmostEqual(game2(10000),0.075,delta=0.1)
            self.assertAlmostEqual(game2(100),0.075,delta=0.1)
            self.assertAlmostEqual(game2(5000),0.075,delta=0.1)
            self.assertAlmostEqual(game2(100000),0.075,delta=0.1)

        def test_game3(self):
            self.assertAlmostEqual(game3(1000),0.15,delta=0.1)
            self.assertAlmostEqual(game3(10000),0.15,delta=0.1)
            self.assertAlmostEqual(game3(100),0.15,delta=0.1)
            self.assertAlmostEqual(game3(5000),0.15,delta=0.1)
            self.assertAlmostEqual(game3(100000),0.15,delta=0.1)

        def test_validmove(self):
            self.assertTrue(validmove(5))
            self.assertTrue(validmove(1))
            self.assertTrue(validmove(9))
            self.assertFalse(validmove(0))
            self.assertFalse(validmove(10))

        def test_validBoard(self):
            self.assertTrue(validBoard())

if __name__=='__main__':
    unittest.main()
