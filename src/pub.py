import pdb
from src.drinks import Drinks


class Pub:

    def __init__(self, name):
        self.name = name
        self.drinks = []

    def drink_count(self):
        return len(self.drinks)

    def find_drink_by_name(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink

    def add_drink(self, drink):
        self.drinks.append(drink)