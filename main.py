from constants import *
from utility_modules import *
import os.path
import random

# Check if NN has already been trained or not
first_time = True
if os.path.isfile(NN_PATH+"NN_1.txt") :
	first_time = False

if first_time :
	init_population()

# STEP 1 :: INITIAL POPULATION (RANDOM or BASED ON PAST LEARNING)
population = get_init_population()

# STEP 2 :: SELECTION OF PARENT
fitness_score = [10, 12, 3, 15]
# Run code and get fitness function for each parent, fitness_score is returned

parent_indices = run_roulette_wheel(fitness_score)
random.shuffle(parent_indices)

parent = [population[i] for i in parent_indices]

# STEP 3 :: CROSS OVER BETWEEN PARENTS
