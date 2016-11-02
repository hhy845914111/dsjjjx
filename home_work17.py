'''
利用贝叶斯框架完成霍尔提蒙问题：将门的数量增加到10个，将主持人打开门的数量增加到3扇，
挑战者只选择1扇门（可假定为1号门）。计算主持人打开3扇空门后，挑战者再选择各扇门获胜的概率。
'''

def pre(hypos):
	'''to calculate P(Hx)'''
	probs = {}
	length = len(hypos)

	for i in hypos:
		probs[i] = 1.0 / length

	return probs


def likelihood(data, hypo, count, choice=1):
	'''to calculate P(Ey|Hx)'''
	if hypo == data: return 0
	elif hypo == choice: return 1.0 / (count - 1)
	else: return 1.0 / (count - 2)

def update(new_evidence, probs, count, choice=1):
	'''to calculate P(Ey && Hx)'''
	for hypo, _ in probs.items():
		probs[hypo] *= likelihood(new_evidence, hypo, count)

def run_test(new_evidence, hypos, choice=1):
	'''to calculate P(Hx|E)'''
	probs = pre(hypos)
	doors_left = len(hypos) #assume that the player insists on first door
	
	for data in new_evidence:
		update(data, probs, doors_left)
		doors_left -= 1
	
	new_sum = sum(list(probs.values()))
	print(probs)
	return (probs[1] / new_sum, probs[10] / new_sum)

def main():
	global DOOR_COUNT, ANHCER_OPEN

	DOOR_COUNT = 10
	ANHCOR_OPEN = 3

	hypos = [i for i in range(1, DOOR_COUNT + 1)]
	evidence_lst = [2, 3, 4]

	print(
'''->Before the anchor opens any doors, the probability of him to win
 is: %f''' % (1.0 / DOOR_COUNT)
 		 )

	print("->After the anchor opens three doors, if he did not change: %f" % run_test(evidence_lst, hypos)[0])
	print("->If he changed: %f" % run_test(evidence_lst, hypos)[1])


if __name__ == "__main__":
	main()
