class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def reduce_cash_from_wallet(self, amount):
        self.wallet -= amount