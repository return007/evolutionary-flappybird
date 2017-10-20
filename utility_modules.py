from constants import *
import numpy as np

def get_random_chromosome(size):
	return np.random.uniform(-3.0, 5.0, size)
	
def init_population():
	for i in range(1, POP_SIZE+1):
		ch = get_random_chromosome(NUMBER_OF_UNITS_L2 * (NUMBER_OF_UNITS_L1 + NUMBER_OF_UNITS_L3))
		filename = NN_PATH + "NN_" + str(i) + ".txt"
		np.savetxt(filename, ch, fmt="%f")

def get_init_population():
	pop = []
	for i in range(1, POP_SIZE+1):
		filename = NN_PATH + "NN_" + str(i) + ".txt"
		ch = np.loadtxt(filename, dtype=float)
		pop.append(ch)
	
	return pop

def get_index_for(arr, key):
	ret_val = -1
	for i in range(len(arr)) :
		if arr[i] < key :
			ret_val = i
		else:
			break
	return ret_val + 1

def run_roulette_wheel(fitness_score):
	fitness_score = np.array(fitness_score, dtype=float)
	total = np.sum(fitness_score)
	prob = fitness_score / total
	cumulative_prob = np.cumsum(prob)
	print cumulative_prob
	indices = []
	for _ in fitness_score :
		val = np.random.random()
		print ">>", val
		indices.append(get_index_for(cumulative_prob, val))
	return indices

