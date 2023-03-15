import chromosome
import read_data
import random

links, demands, paths = read_data.read_data("newData.txt")

#chrome = chromosome.create_chromosome()
#chrome = [[0,3,0],[2,0,2],[2,3],[1,0,1],[1,2,0],[2,2,0]]

pop = chromosome.create_population(100)
ce = [2, 4, 3, 2, 6]
m = 2

Ce = [h * m for h in ce]


def overload(chromosome):
    linkloads = []
    maximum = -1000000
    for link in range(len(links)):
        linksum = 0
        check = link + 1 
        for demand in range(len(demands)):
            for path in range(len(paths)):
                if paths[path].d == demand:
                    for l in range(len(paths[path].paths)):
                        if int(paths[path].paths[l]) == check:
                            linksum = linksum + int(chromosome[demand][paths[path].l])
        linkloads.append(linksum)

    for f in range(len(linkloads)):
        newMax = linkloads[f] - Ce[f]
        if newMax > maximum:
            maximum = newMax
    
    return maximum


def evolution(population):
    popul = []
    newPop = []

    for chrom in pop:
        p = overload(chrom)
        popul.append(p)
    
    for p in range(len(popul)):
        newChrom = []
        for g in range(len(population[0])):
            mutation = random.randint(0, 100)
            x = random.randint(0, len(population) - 1)
            y = random.randint(0, len(population) - 1)
            r = random.randint(0, 1)
            if r == 0:
                if mutation > 90:
                    random.shuffle(population[x][g])
                    newChrom.append(population[x][g])
                else:
                    newChrom.append(population[x][g])
            elif r == 1:
                if mutation > 90:
                    random.shuffle(population[y][g])
                    newChrom.append(population[y][g])
                else:
                    newChrom.append(population[y][g])
        newPop.append(newChrom)
    return newPop


print(evolution(pop))

            