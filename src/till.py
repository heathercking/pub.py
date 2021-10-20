class Till:

    def __init__(self, total_cash):
        self.total_cash = total_cash

    def increase_cash_in_till(self, amount):
        self.total_cash += amount