import unittest
import pdb
from src.pub import Pub
from src.drinks import Drinks

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.ourpub = Pub("The Prancing Pony")

    def test_pub__has_name(self):
        self.assertEqual("The Prancing Pony", self.ourpub.name)

    def test_drink_count__is_empty(self):
        self.assertEqual(0, self.ourpub.drink_count())

    def test_add_drink_to_pub(self):
        new_drink = Drinks("Brewdog", 9.10)
        self.ourpub.add_drink(new_drink)
        self.assertEqual(1, len(self.ourpub.drinks))

