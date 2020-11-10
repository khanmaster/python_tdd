# This file will have our tests writen

# importing the required modules/libraries and frame works

from simple_calc import Simple_Calc
import unittest
import pytest

# Let's create a class to write our tests

class Calctest(unittest.TestCase):

    calc = Simple_Calc()
# creating an object of our class

# IMPORTANT - we MUST use TEST word in our functions so python interpreter  knows what are we testing

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)
# self.assertEqual(self.calc.add(2, 4), 6)
# what are we asking python to test for us
# we are asking python to test/check if 2 + 4 = 6 if True pass the test if False fail the test

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)  # Boolean
        # Test if 4 - 2 = 2 if True pass the test if False then Fail the test

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)  # Boolean
        # Test if 2 * 2 = 4 if True pass the test if False fail the test

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

