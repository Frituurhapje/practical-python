import pandas as pd

class Stock:
    def __init__(self, name, shares, price, cash=0):
        self.name = name
        self.shares = shares
        self.price = price
        self.cash = cash

    def cost(self):
        return self.shares * self.price

    def sell(self, sell):
        self.shares -= sell
        self.cash += sell * self.price

portdf = pd.read_csv('../Data/portfolio.csv')
portfolio = [Stock(d.name, d.shares, d.price) for d in portdf.itertuples()]
print(sum([s.cost() for s in portfolio]))
