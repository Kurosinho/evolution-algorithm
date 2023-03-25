import chromosome
import read_data
import random

links, demands, paths = read_data.read_data("newData.txt")

#chrome = chromosome.create_chromosome()
#chrome = [[0,3,0],[2,0,2],[2,3],[1,0,1],[1,2,0],[2,2,0]]
#TODO: Generalnie chodzi o to, żeby tworzył nowe populacje dopóki nie osiągniemy pożądanego 
#poziomu optymalizacji
pop = chromosome.create_population(10)
ce = [2, 4, 3, 2, 6]
m = 2
#print(pop)
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

def crossover(population, w):
    bestPop = []
    newPop = []
    for g in range(len(population)):
        x = random.choices(population, w)
        y = random.choices(population, w)
        while y == x:
            y = random.choices(population, w)
        newChrom = []
        newChrom2 = []
        for i in range(len(population[0])):
            r = random.randint(0, 1)
            if r == 0:
                newChrom.append(x[0][i])
                newChrom2.append(y[0][i])
            elif r == 1:
                newChrom.append(y[0][i])
                newChrom2.append(x[0][i])
        newPop.append(newChrom)
        newPop.append(newChrom2)
        
    betterWeights = []
    for chrom in newPop:
        p = overload(chrom)
        betterWeights.append(p)

    upset = max(betterWeights)
    downset = min(betterWeights)
    weights = [z - downset + upset for z in betterWeights]
    k = len(newPop)/2
    betterPop = random.choices(newPop, weights, k=int(k))
    bestPop = betterPop
    
    return bestPop
        


def evolution(population, k):
    popul = []
    newPop = []

    for chrom in population:
        p = overload(chrom)
        popul.append(p)

    upset = max(popul)
    downset = min(popul)
    weights = [z - downset + upset for z in popul]

    for p in range(k):
        newPop = crossover(population, weights)
                
    for x in range(len(newPop)):
        mutation = random.randint(0, 100)
        if mutation > 90:
            gene = random.randint(0, len(newPop[0]) - 1)
            allelle = random.randint(0, len(newPop[0][gene]) - 1)
            if newPop[x][gene][allelle] != 0:
                newPop[x][gene][allelle] = newPop[x][gene][allelle] - 1
                newAllelle = random.randint(0, len(newPop[0][gene]) - 1)
                newPop[x][gene][newAllelle] = newPop[x][gene][newAllelle] + 1
    return newPop

sg = evolution(pop, 6)
np = []
for i in range(10):
    sg = evolution(sg, 6)
    np = sg


print ("new population")
for a in range(len(np)):
    print(a, np[a])


            