# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 14:33:03 2016

@author: S
"""

'''
采用big数据集，分别计算女性和男性的利息率和借款金额的均值，并判断是否存在统计意义上的
差异，该结果能说明什么问题？（25分）
'''

from pandas import read_csv
from scipy.stats import ttest_ind
from scipy.stats import levene

def initiate_data(offline=True, path="p2p_big.csv"):
    global df_raw
    
    if offline:
        df_raw = read_csv(path)
    else:
        pass
   
def check_u(df1, df2, alpha1=0.05, alpha2=0.05):
    result = 0.0
    mean_df1 = sum(df1.values) / len(df1.values)
    mean_df2 = sum(df2.values) / len(df2.values)
    mid = 0
    
    _, pvalue = levene(df1, df2)
    if pvalue <= alpha1: #reject null hypo: they have same var
        _, result = ttest_ind(df1, df2, equal_var = False)
        mid = False
    else: #accept null hypo
        _, result = ttest_ind(df1, df2, equal_var = True)
        mid = True
        
    if result <= alpha2:
        return (mean_df1, mean_df2, mid, False)
    else:
        return (mean_df1, mean_df2, mid, True)

def main():
    initiate_data()

    df_female_interest = df_raw[df_raw["sex"] == 1]["interest"]
    df_male_interest   = df_raw[df_raw["sex"] == 2]["interest"]

    df_female_amount   = df_raw[df_raw["sex"] == 1]["amount"] 
    df_male_amount   = df_raw[df_raw["sex"] == 2]["amount"]

    print(check_u(df_female_amount, df_male_amount))
    print(check_u(df_female_interest, df_male_interest))
    
if __name__ == "__main__":
    main()
