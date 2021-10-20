import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Barry Brexit", 60)

    def test_customer__has_name(self):
        self.assertEqual("Barry Brexit", self.customer.name)
    
    def test_customer__has_walllet(self):
        self.assertEqual(60, self.customer.wallet)

    def test_customer_cash(self):
        self.customer.reduce_cash_from_wallet(10)
        self.assertEqual(50, self.customer.wallet)
