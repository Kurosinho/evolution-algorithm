import chromosome

n = 10

population = []

for i in range(n):
    chrome = chromosome.create_chromosome()
    population.append(chrome)

print(population)