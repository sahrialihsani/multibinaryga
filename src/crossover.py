import numpy as np
import random
import math

def parent_selection(population, crossover_rate):

  parents = []
  parents_idx = []  
  
  rand = np.random.uniform(0, 1, len(population))

  for i in range(len(population)):

    if rand [i] < crossover_rate:

      # print("selected parent is:", i)
      # print(population[i])

      parents.append(population[i].copy())
      parents_idx.append(i)

  if len(parents) == 0:
    parents.append(population[0].copy)

  return parents, parents_idx

def crossover(parents):

  child = parents.copy()
  
  if len(child) == 1:
    return child  

  else:

    rand = random.randint(1,child[0].shape[0]-1)

    # print("cut off point:", rand)

    # check if num of selected is odd or even
    if (len(child)%2 == 0):
      # print("even")

      for i in range(0, len(child), 2):

        # print(i, "x", i+1)

        # swap the genes

        child[i][rand:], child[i+1][rand:]  = child[i+1][rand:].copy(), child[i][rand:].copy()

      return child

    else:
      # print("odd")

      temp = child[0][rand:].copy()

      for i in range(0, len(child), 2):

        if i == len(child)-1:

          # print(i, "x", 0)

          child[i][rand:] = temp

        else:
          
          # print(i, "x", i+1)

          child[i][rand:], child[i+1][rand:] = child[i+1][rand:].copy(), child[i][rand:].copy()

      return child

def merge_crossover(cross_over, populations, idx):

  populations = populations.copy()

  j = 0
  for i in idx:
    
    populations[i] = cross_over[j].copy()
    j = j+1

  return populations.copy()

if __name__ == "__main__":

    from initialize import init_pop
    from fitness import decoding, fitness_func
    from selection import cumprob, selection
    from utils import load_config

    params = load_config()

    x1_encoded = init_pop(params["n_chrom"], params["lower_x1"], params["upper_x1"], params["precision"])
    x2_encoded = init_pop(params["n_chrom"], params["lower_x2"], params["upper_x2"], params["precision"])

    x1_decoded = decoding(x1_encoded, params["lower_x1"], params["upper_x1"])
    x2_decoded = decoding(x2_encoded, params["lower_x2"], params["upper_x2"])

    population = fitness_func(x1_decoded, x2_decoded)

    prop_table = cumprob(population)

    new_pop = selection(x1_encoded, x2_encoded, prop_table, params["n_chrom"])

    parents, idx = parent_selection(new_pop, params["crossover_rate"])

    crossed_pop = crossover(parents)

    all_new_pop = merge_crossover(crossed_pop, new_pop, idx)

    print(all_new_pop)

    