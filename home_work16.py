from scipy import stats
from douban1 import douban

'''
验证豆瓣网2015年评分和2016年评分均值是否有差异。在相邻的两年中，这种情况发生最近的一次是哪一年？
'''

def test(year1, year2, alpha1, alpha2):
    choice = lambda p, alpha, c1, c2: c1 if p <= alpha else c2
    
    print "对于%d, %d年：" % (year1, year2)
    
    raw_info_lst = douban() 
    
    rank_1_lst = [float(i[3]) for i in raw_info_lst if i[5] == str(year1)]
    rank_2_lst = [float(i[3]) for i in raw_info_lst if i[5] == str(year2)]
    
    p1 = stats.levene(rank_1_lst, rank_2_lst)[1]
    print "在%f的水平上，两个样本方差统计%s不同" % (alpha1, choice(p1, alpha1, "不显著", "显著"))
    
    p2 = stats.ttest_ind(rank_1_lst, rank_2_lst, equal_var=choice(p1, alpha1, True, False))[1]
    print "在%f的水平上，两个样本均值统计%s不同" % (alpha2, choice(p2, alpha2, "不显著", "显著"))
    
    return (year1, year2, choice(p2, alpha2, True, False))
    
def main():
    i = 2016
    result = [0, 0, False]
    while not result[2]:
        result = test(i, i-1, 0.05, 0.05)
    print result
    
if __name__ == "__main__":
    main()
