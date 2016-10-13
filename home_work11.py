'''
根据美国疾控中心统计，男性吸烟者患肺癌的概率比男性非吸烟者高23倍。
而女性吸烟者患肺癌的概率比女性非吸烟者高13倍，女性吸烟的概率为17.9%。
已知某女性患了肺癌，她是吸烟者的概率有多高？分别用贝叶斯公式和模拟两种方法计算。
'''
import random

class Diagnose(object):

	def bayes(self, C_B=0.14, B=0.179, C_not_B=0.01):
		'''
		Let
		{
			A == male; 
			B == smoke;
			C == have cancer;
		} 
		then
		{
			P(B|(!A && C)) == P((!A && C) | B) / P(!A && C);
		also:
			P(!A && B && C) == 13 * P(!A && !B && C);
		}

		'''
		return float(C_B) * B / (C_B * B + C_not_B * (1-B))
		

	def monti_carlo(self, rate_smoke=0.179, rate_nonsmoke_cancer=0.07, times=14):
		smoke_cancer = 0
		non_smoke_cancer = 0
		smoke_non_cancer = 0
		non_smoke_non_cancer = 0

		smoke_lst = [1 for i in range(int(rate_smoke*1000))]
		smoke_lst += [0 for i in range(1000 - len(smoke_lst))]

		smoke_cancer_lst = [1 for i in range(int(rate_nonsmoke_cancer*1000*times))]
		smoke_cancer_lst += [0 for i in range(1000 - len(smoke_cancer_lst))]

		non_smoke_cancer_lst = [1 for i in range(int(rate_nonsmoke_cancer*1000))]
		non_smoke_cancer_lst += [0 for i in range(1000 - len(non_smoke_cancer_lst))]

		for i in range(10000):
			tester = {"smoke": 0, "cancer": 0}	
			tester["smoke"] = random.choice(smoke_lst)
			if tester["smoke"]:	
				tester["cancer"] = random.choice(smoke_cancer_lst)
			else:
				tester["cancer"] = random.choice(non_smoke_cancer_lst)

			if tester["cancer"]:
				if tester["smoke"]: smoke_cancer += 1
				else: non_smoke_cancer += 1
			else:
				if tester["smoke"]: smoke_non_cancer += 1
				else: non_smoke_non_cancer += 1

		return float(smoke_cancer) / (smoke_cancer + non_smoke_cancer)

if __name__ == "__main__":
	d1 = Diagnose()
	print(d1.bayes())
	print(d1.monti_carlo())



			


