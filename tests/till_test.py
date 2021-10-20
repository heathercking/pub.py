import unittest
from src.till import Till


class TestTill(unittest.TestCase):

    def setUp(self):
        self.till = Till(1000.0)

    def test_pub__has_till(self):
        self.assertEqual(1000.0, self.till.total_cash)
