import read_data
import random

def create_chromosome():
    links, demands, paths = read_data.read_data("newData.txt")

    chromosome = []

    for i in range(len(demands)):
        hd = int(demands[i].volume)
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

    return chromosome