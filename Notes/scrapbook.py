#Iterating over dataframe rows

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

    def buy(self, buy):
        self.shares += buy
        self.cash -= buy * self.price

class Wallet:
    def __init__(self, portfolio, cash=0):
        self.cash = cash

    def buy(self, Stock):
        Stock.buy

    def sell(self, Stock):
        Stock.sell

portdf = pd.read_csv('../Data/portfolio.csv')
portfolio = [Stock(d.name, d.shares, d.price) for d in portdf.itertuples()]
print(sum([s.cost() for s in portfolio]))

