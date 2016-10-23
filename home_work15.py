from scipy import stats
from douban1 import douban

rank_lst = [float(i[3]) for i in douban()]
print stats.kstest(rank_lst, 'norm')
print "不服从正态分布"

