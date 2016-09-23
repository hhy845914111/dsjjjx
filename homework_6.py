# 分析豆瓣所有网电影评分数据集，画出CDF图示。
from Cdf import *
from douban import *
import myplot as mpt

mpt.Cdf(MakeCdfFromList(rating()))
