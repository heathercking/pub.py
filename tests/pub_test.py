import unittest
import pdb
from src.pub import Pub
from src.drinks import Drinks
from src.till import Till
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.ourpub = Pub("The Prancing Pony")
        self.ourtill = Till(1000)
        self.ourcustomer = Customer("Barry Brexit", 60)

    def test_pub__has_name(self):
        self.assertEqual("The Prancing Pony", self.ourpub.name)

    def test_drink_count__is_empty(self):
        self.assertEqual(0, self.ourpub.drink_count())

    def test_get_drink_price(self):
        new_drink1 = Drinks("Brewdog", 9.10)
        self.ourpub.add_drink(new_drink1)
        new_drink2 = Drinks("MD2020", 3.0)
        self.ourpub.add_drink(new_drink2)
        new_drink3 = Drinks("Frosty Jacks", 4.2)
        self.ourpub.add_drink(new_drink3)
        drink_price = self.ourpub.find_drink_price(new_drink3.name)
        self.assertEqual(4.2, drink_price)

    def test_add_drink_to_pub(self):
        new_drink = Drinks("Brewdog", 9.10)
        self.ourpub.add_drink(new_drink)
        self.assertEqual(1, len(self.ourpub.drinks))


    def test_customer_can_buy_drink(self):
        new_drink1 = Drinks("Brewdog", 9.10)
        self.ourpub.add_drink(new_drink1)
        new_drink2 = Drinks("MD2020", 3.0)
        self.ourpub.add_drink(new_drink2)
        drink_price = self.ourpub.find_drink_price(new_drink1.name)
        self.ourcustomer.reduce_cash_from_wallet(drink_price)
        self.ourtill.increase_cash_in_till(drink_price)
        self.assertEqual(1009.1, self.ourtill.total_cash)
        self.assertEqual(50.9, self.ourcustomer.wallet)
    

