import unittest
from src.till import Till


class TestTill(unittest.TestCase):

    def setUp(self):
        self.till = Till(1000.0)

    def test_pub__has_till(self):
        self.assertEqual(1000.0, self.till.total_cash)

    def test_increase_cash_in_till(self):
        self.till.increase_cash_in_till(9.50)
        self.assertEqual(1009.5, self.till.total_cash)
