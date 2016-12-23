# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 15:06:20 2016

@author: S
"""

'''
3. 采用small数据集，计算P2P环境下资金的利率需求/供给弹性（利息率每变动1%，
资金需求/供给变动的百分比），该结果能说明什么问题？（25分）
'''

from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from math   import log

from statsmodels.formula.api import ols

def initiate_data(offline=True, path="p2p_small.csv"):
    global df_raw
    
    if offline:
        df_raw = read_csv(path)
    else:
        pass

def main():
    initiate_data()
    df_interest = df_raw["interest"]
    df_amount   = df_raw["amount"]
    df_total    = concat([df_interest, df_amount], axis=1)

    df_regression = DataFrame(index=df_total.index)
    df_regression["log_interest"] = 0
    df_regression["log_amount"] = 0

    for i in df_total.index:
        df_regression.ix[i, "log_interest"] = log(df_total.ix[i, "interest"])
        df_regression.ix[i, "log_amount"]   = log(df_total.ix[i, "amount"])
    
    result = ols(formula="log_amount ~ log_interest ", data=df_regression).fit()
    print result.params

if __name__ == "__main__":
    main()