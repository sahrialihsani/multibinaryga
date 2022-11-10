import numpy as np
import math
import random

random.seed(42)
np.random.seed(42)

def init_pop(n_chrom, lower, upper, precision):

  n_gene = math.ceil(math.log(((upper-lower)*(10**precision))+1, 2))

  population = np.zeros([n_chrom, n_gene], dtype=int)

  for i in range(n_chrom):

    for j in range(n_gene):

      population[i,j] = random.randint(0,1)

  return population


if __name__ == "__main__":

    n_chrom = int(input("Number of chromosom: "))

    lower = float(input("Lower bound: "))

    upper = float(input("Upper bound: "))

    precision = int(input("Precision: "))

    print()
    print(init_pop(n_chrom, lower, upper, precision))