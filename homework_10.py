'''
参考ex4_13.py导入数据的方法，利用基尼系数公式完成美国2008年基尼系数的计算。 提示： （1）生成新的空白Pmf对象diff=Pmf.Pmf() （2）for v1, p1 in pmf.Items():实现老pmf中值和概率的遍历，计算 （3）diff.Incr(abs(v1-v2), p1*p2)可以新pmf对象填充完整 （4）PmfMean(pmf)，可以求新旧Pmf对象的均值。 （5）新pmf均值/旧Pmf均值/2即为基尼系数
'''
from ex4_13 import *

diff = Pmf.Pmf()

_,pmf_old,_1 = MakeIncomeDist(ReadIncomeFile())

for v1, p1 in pmf_old.Items():
    for v2, p2 in pmf_old.Items():
        diff.Incr(abs(v1-v2), p1*p2)

print diff.Mean() / pmf_old.Mean() / 2
