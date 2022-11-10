import numpy as np
import random

random.seed(42)
np.random.seed(42)

def cumprob(solutions):
  
  prob_table = {
      "fitness_prob": list(solutions["fitness"]/np.sum(solutions["fitness"])),
      "cumulative_prob": list(np.cumsum(solutions["fitness"]/np.sum(solutions["fitness"]))),
  }

  return prob_table["cumulative_prob"]

def selection(x1_encoded, x2_encoded, cumulative_sum, n_chrom):

  # join bit from x1 and x2 altogther
  pop_x1_x2 = np.concatenate((x1_encoded, x2_encoded), axis=1)

  rand = np.random.uniform(0, 1, n_chrom)

  selected_chrom = []

  for i in range(len(rand)):

    for j in range(len(cumulative_sum)):

      if j <= 0:
        if rand[i] <= cumulative_sum[j]:
    
          selected_chrom.append(pop_x1_x2[j])
          break

      elif (j>0)&(j<=len(cumulative_sum)-1):
        if rand[i] <= cumulative_sum[j]:
          
          selected_chrom.append(pop_x1_x2[j])
          break
  return selected_chrom

if __name__ == "__main__":

    from initialize import init_pop
    from fitness import decoding, fitness_func
    from utils import load_config

    params = load_config()

    x1_encoded = init_pop(params["n_chrom"], params["lower_x1"], params["upper_x1"], params["precision"])
    x2_encoded = init_pop(params["n_chrom"], params["lower_x2"], params["upper_x2"], params["precision"])

    x1_decoded = decoding(x1_encoded, params["lower_x1"], params["upper_x1"])
    x2_decoded = decoding(x2_encoded, params["lower_x2"], params["upper_x2"])

    population = fitness_func(x1_decoded, x2_decoded)

    prop_table = cumprob(population)

    new_pop = selection(x1_encoded, x2_encoded, prop_table, params["n_chrom"])

    print(new_pop)