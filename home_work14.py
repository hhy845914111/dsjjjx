'''
修改“高抛低吸策略”为双均线策略（金叉买入，死叉卖出）。 
1.测试某一种价格场景下下的策略收益率，采几种用不同的均线组合（5天，10天组合还是其他等），看看那种收益率最高。 
2.计算1000次不同价格场景下的策略收益率。
'''
from random import uniform

def random_price(days, S0=10):
	price_lst = [S0]
	for i in range(1, days+1):
		price_lst.append(max([price_lst[-1] * uniform(0.9, 1.1), 2]))
	return price_lst;

def days_average(price_lst, interval):
	count_range = price_lst[interval:]
	average_lst = []
	for i in range(len(price_lst)-interval):
		average_lst.append(sum(price_lst[i:i+interval])/interval)
	return average_lst

def trader_work(hist_lst, cash=100, short_interval=5, long_interval=10):
	stock_position = 0
	cash_position = cash
	short_average = days_average(hist_lst, short_interval)
	long_average = days_average(hist_lst, long_interval)
	skip = max([short_interval, long_interval])
	trade_history = []
	for i in range(skip, len(hist_lst)):
		if (short_average[i-short_interval] > long_average[i-long_interval] 
			and short_average[i-1-short_interval] < long_average[i-1-long_interval]
			):
			stock_position += cash_position // hist_lst[i]
			cash_position = 0
			trade_history.append((i, hist_lst[i], cash, stock_position))
		if (short_average[i-short_interval] < long_average[i-long_interval] 
			and short_average[i-1-short_interval] > long_average[i-1-long_interval]
			):
			cash_position = stock_position * hist_lst[i]
			stock_position = 0
			trade_history.append((i, hist_lst[i], cash_position, stock_position))
	return ((cash_position + stock_position * hist_lst[-1]) / cash, trade_history)

def once(cash, short_t, long_t):
	hist_price = random_price(1000)
	return trader_work(hist_price, 1000, short_t, long_t)[0]

if __name__ == "__main__":
	for i in range(10, 70, 10):
	    for j in range(i+10, 130, 10):
             print("%d, %d: %f" % (i, j, sum([once(1000, i, j) for k in range(10)])/10))
