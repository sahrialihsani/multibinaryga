import numpy as np
import math
import random

import matplotlib.pyplot as plt

random.seed(42)
np.random.seed(42)

def get_best_gen(all_gen, plot=False):

  fitness_history = []
  for sol in all_gen:
    fitness_history.append(sol["fitness"])
  
  best_gen_idx = fitness_history.index(max(fitness_history))

  best_gen = all_gen[best_gen_idx]

  if plot == True:
    
    plt.figure(figsize=(8,6))

    plt.title("Fitness Score")

    plt.plot(fitness_history)

    plt.axvline(x=best_gen_idx, color='r', linestyle="--", label="best_generation")

    plt.legend()

    plt.show()

  print()
  print("Best generation number:", best_gen_idx)
  print("Best solution:", best_gen)

  return best_gen_idx, best_gen


def decoding(chrom, lower, upper):

  decoded = {}

  # change the array of bit into array of string
  # so the decimal can be calculated
  temp=[]
  for i in range(len(chrom)):
    temp.append(np.array2string(chrom[i,], separator="").strip("[]"))

  for i in range(len(temp)):

    num_gene = len(temp[i])

    individual = int(temp[i], 2)

    decode = lower + individual*((upper-lower)/((2**num_gene)-1))

    decoded.update({i+1:float(f"{decode:.2f}")})

  return decoded


def fitness_func(x1_decoded, x2_decoded):

  fitness = {
      "chrom": [],
      "x1": [],
      "x2": [],
      "fitness": [],
  }

  for i in range(len(x1_decoded)):
    
    # this is the objective function
    fx1_x2 = 33.7+x1_decoded[i+1]*math.sin(4*math.pi*x1_decoded[i+1])+x2_decoded[i+1]*math.sin(20*math.pi*x2_decoded[i+1])

    # fitness.update({i+1,[fx1_x2, x1_decoded[i+1], x2_decoded[i+1]]})
    fitness["chrom"].append(i+1)
    fitness["x1"].append(x1_decoded[i+1])
    fitness["x2"].append(x2_decoded[i+1])
    fitness["fitness"].append(fx1_x2)

  return fitness

def find_max(solutions):
  
  idx = solutions["fitness"].index(max(solutions["fitness"]))

  chrom = solutions["chrom"][idx]

  fitness = solutions["fitness"][idx]

  x1 = solutions["x1"][idx]

  x2 = solutions["x2"][idx]

  return({
      "chrom": chrom,
      "x1": x1,
      "x2": x2,
      "fitness": fitness,
  })

def get_x1_x2(populations, x1_encoded):

  x1 = []
  x2 = []

  mutated = populations.copy()

  for i in range(len(populations)):

    x1.append(list(mutated[i][:len(x1_encoded[0])].copy()))
    x2.append(list(mutated[i][len(x1_encoded[0]):].copy()))

  return np.array(x1), np.array(x2)


if __name__ == "__main__":

  from initialize import init_pop
  from utils import load_config

  params = load_config()

  x1_encoded = init_pop(params["n_chrom"], params["lower_x1"], params["upper_x1"], params["precision"])
  x2_encoded = init_pop(params["n_chrom"], params["lower_x2"], params["upper_x2"], params["precision"])

  x1_decoded = decoding(x1_encoded, params["lower_x1"], params["upper_x1"])
  x2_decoded = decoding(x2_encoded, params["lower_x2"], params["upper_x2"])

  population = fitness_func(x1_decoded, x2_decoded)

  best_chrom = find_max(population)

  print(best_chrom)