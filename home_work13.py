#生成10个不同随机变量的随机数之和，重复多次，计算其分布
import numpy as np 
import random
import rankit

def once():
	binomial = np.random.binomial(2, 0.4)
	poisson = np.random.poisson(2)
	uniform = random.uniform(1, 10)
	chisquare = np.random.chisquare(2)
	normal = np.random.normal(3, 3)
	lognormal = np.random.lognormal(2, 3)
	standard_t = np.random.standard_t(2)
	exponential = np.random.exponential(2)
	triangular = np.random.triangular(1, 3, 10)
	beta = np.random.beta(3, 2)
	gamma = np.random.gamma(3)
	weibull = np.random.weibull(3)
	gumbel = np.random.gumbel(3, 2)
	return (
		binomial + poisson + uniform + chisquare + normal + lognormal
		+ standard_t + exponential + triangular + beta + gamma + weibull + gumbel)

if __name__ == "__main__":
	rankit.MakeNormalPlot([once() for i in range(10000)])
