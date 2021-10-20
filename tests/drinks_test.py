import unittest
from src.drinks import *


class TestDrinks(unittest.TestCase):

    def setUp(self):
        self.drinks = Drinks("Tennents", 4.50)

    def test_drink__has_name(self):
        self.assertEqual("Tennents", self.drinks.name)

    def test_drink__has_price(self):
        self.assertEqual(4.50, self.drinks.price)
    
