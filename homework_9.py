'''
分别计算对比《红楼梦》和《诛仙》出现的字的概率，计算在TOP100中有多少个相同的汉字，打印这些相同的字在两部小说中出现的频率。《红楼梦》路径对应 "../hlm.txt"《诛仙》路径对应 "../qyz.txt"
'''

from ex4_5 import *

def printf(set_common, *dcts):
    lst_common = list(set_common)
    for i in lst_common:
        print "%s: %d, %d" % (i, dcts[0][i], dcts[1][i])  

if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")
    hlm_dct = count_chinese_word("../hlm.txt", 'gbk')
    qyz_dct = count_chinese_word("../qyz.txt", 'gbk')
    
    hlm_set = set(i[0] for i in sorted(
        hlm_dct.items(), key=lambda x: x[1], reverse=True)[:100])
    qyz_set = set(i[0] for i in sorted(
        qyz_dct.items(), key=lambda x: x[1], reverse=True)[:100])
    
    hlm_n_qyz_set = hlm_set & qyz_set
    printf(hlm_n_qyz_set, hlm_dct, qyz_dct)
