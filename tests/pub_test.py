import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony")

    def test_pub__has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

  

    # def test_pub__has_drinks(self):
    #     self.assertEqual("The Prancing Pony", self.drinks.name)
