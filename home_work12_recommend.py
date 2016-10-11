'''
1.建立一个价格函数random_price，该函数产生第0个交易日到第1000个交易日的价格。
第0期初始价格为10。每期在上期价格基础的0.9到1.1倍均匀波动。 
2.建立一个高抛低吸策略函数，参数为价格列表，高价格high，低价low。
当价格高于high模拟抛出股票，当价格低于low模拟买入股票。返回收益率。 
3.建立一次模拟函数once，先计算价格，然后计算策略的收益率。 
4.模拟1000次once,计算该策略的平均收益率。
'''

from random import uniform
import matplotlib.pyplot as plt
from math import floor

def random_price(days, S0=10):
	price_lst = [S0]
	for i in range(1, days+1):
		price_lst.append(price_lst[-1] * uniform(0.9, 1.1))
	return price_lst;

class Trader(object):
    def __init__(self, cash):
    	self.cash = cash
    	self.buy_p = 8
    	self.sell_p = 11
    	self.stock = 0
    	self.trading_hist_lst = []

    def _buy(self, price, day):
    	stock_change = floor(self.cash / price)
    	cash_change = -stock_change * price
    	self.cash += cash_change
    	self.stock += stock_change
    	self.trading_hist_lst.append((day, price, stock_change, cash_change))

    def _sell(self, price, day):
    	stock_change = -self.stock
    	cash_change = stock_change * price
    	self.cash += cash_change
    	self.stock += stock_change
    	self.trading_hist_lst.append((day, price, stock_change, cash_change))

    def auto_trade(self, day, St):
    	if St > self.sell_p:
    		self._sell(St, day)
    	elif St < self.buy_p:
    		self._buy(St, day)

    def get_position(self):
    	return (self.stock, self.cash)

    def set_barrier(self, buy_p, sell_p):
    	self.sell_p = sell_p
    	self.buy_p = buy_p

def trader_work(hist_lst, cash=100):
	a_trader = Trader(cash)
	for i, content in enumerate(hist_lst):
		a_trader.auto_trade(i, content)

	return (a_trader.cash + a_trader.stock * hist_lst[-1] - cash) / cash

def once():
	return trader_work(random_price(1000), 1000)

if __name__ == "__main__":
	result_lst = [once() for i in range(1000)]
	mean = sum(result_lst) / len(result_lst)
	print mean 

	
