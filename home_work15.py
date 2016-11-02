from scipy import stats
from douban1 import douban
from math import sqrt

rank_lst = [float(i[3]) for i in douban()]

mean = sum(rank_lst) / len(rank_lst)
stdev = sqrt(sum([(i - mean)**2 for i in rank_lst]))
stdrk = [((i - mean) / stdev) for i in rank_lst]
             
print stats.kstest(stdrk, 'norm')
print "不服从正态分布"

