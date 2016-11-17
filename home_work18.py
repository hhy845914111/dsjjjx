from douban1 import douban
from ex9_2 import corr

raw_lst = doubana()
rate_lst = [float(i[3]) for i in raw_lst]
count_lst = [int(i[11]) for i in raw_lst]

print corr(rate_lst, count_lst)
