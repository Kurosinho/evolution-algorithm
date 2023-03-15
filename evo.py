import read_data
import random
#import numpy as np

links, demands, paths = read_data.read_data("data.txt")

chromosome = []

for i in range(len(demands)):
    hd = int(demands[i].volume)
    print(hd)
    check = 0
    gene = []
    for j in range(demands[i].no_of_links - 1):
        x = random.randint(0, hd)
        gene.append(x)
        hd = hd - x
    for a in range(len(gene)):
        check = check + gene[a]
    if check != demands[i].volume:
        gap = int(demands[i].volume) - check
        gene.append(gap)
    chromosome.append(gene)

print(chromosome)