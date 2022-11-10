import numpy as np
import math

def mutation(populations, mutation_rate):

  # banyaknya gen
  size = len(populations[0])*len(populations)

  # banyaknya gen yang akan dimutasikan
  mutation_size = math.ceil(size*mutation_rate)

  # generate random number sebanyak mutation_size
  rk = np.random.randint(0,size,mutation_size)

  for r in rk:

    # ambil index kromosom
    chr_idx = math.floor(r/len(populations[0]))

    # ambil index gen
    gen_idx = r - len(populations[0])*chr_idx

    if populations[chr_idx][gen_idx] == 1:

      populations[chr_idx][gen_idx] = 0

    else:

      populations[chr_idx][gen_idx] = 1

  return populations.copy()

if __name__ == "__main__":

    from initialize import init_pop
    from fitness import decoding, fitness_func, get_x1_x2
    from selection import cumprob, selection
    from crossover import parent_selection, crossover, merge_crossover
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

    mut_pop = mutation(all_new_pop, params["mutation_rate"])

    x1_encoded, x2_encoded = get_x1_x2(mut_pop, x1_encoded)

    print("x1")
    print(x1_encoded)
    print("x2")
    print(x2_encoded)