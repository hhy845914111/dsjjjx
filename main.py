# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 14:01:11 2016

@author: S
"""

'''
蒙特卡洛模拟：
模拟微信抢红包，将100元按次序随机发放9个（次）红包，第10个红包就是第9
个红包发完后的剩余金额。模拟1000次，计算不同次序红包的均值和标准差。如何调整才
能使得10个红包金额的均值大致相等，写出思路并尽可能实现。（25分）
'''

import random as rd
import numpy as np

def gen_redbeg1():
    result = []
    result = [round(rd.uniform(0, 100), 2) for i in range(9)]    
    while sum(result) > 100:    
        result = [round(rd.uniform(0, 100), 2) for i in range(9)]
    
    result.append(round(100 - sum(result), 2))
    return result
    
def gen_redbeg2(amount=10, money=100, k=0.1):
    mean     = money / amount
    interval = mean * k
    
    result = [round(rd.uniform(mean - interval, mean + interval), 2) for i in range(9)]    
    while sum(result) > 100:    
        result = [round(rd.uniform(mean - interval, mean + interval), 2) for i in range(9)]
    
    result.append(round(100 - sum(result), 2))
    return result


def main(n=1000):
    qian9 = []
    hou1  = []
    
    for i in range(n):
        to_in = gen_redbeg2() 
        qian9.append(to_in[0])
        hou1.append(to_in[9])
    
    average9 = sum(qian9) / len(qian9)
    stdev9   = np.var(qian9)
    
    average1 = sum(hou1) / len(hou1)
    stdev1   = np.var(hou1)

    print(average9, average1)
    print(stdev9, stdev1)        
    
if __name__ == "__main__":
    main()