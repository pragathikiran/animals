class Profit:
    def __init__(self):
        self._maxprice = 900
        self._costprice = 200

    def sell(self):
        print("Selling price: {}".format(self._maxprice))
        profit = self._maxprice - self._costprice
        profit_percentage = (profit / self._costprice) * 100
        print("Cost price: {}".format(self._costprice))
        print("Profit: {}".format(profit))
        print("Profit percentage: {:.2f}%".format(profit_percentage))

# Example usage
p = Profit()
p.sell()
