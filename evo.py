import chromosome
import read_data

links, demands, paths = read_data.read_data("newData.txt")

#chrome = chromosome.create_chromosome()
chrome = [[0,3,0],[2,0,2],[2,3],[1,0,1],[1,2,0],[2,2,0]]

pop = chromosome.create_population(1)

m = 2
linkloads = []
for link in range(len(links)):
    linksum = 0
    check = link + 1 
    for demand in range(len(demands)):
         for path in range(len(paths)):
            s = paths[path].d
            if paths[path].d == demand:
                for l in range(len(paths[path].paths)):
                    view = int(paths[path].paths[l])
                    if int(paths[path].paths[l]) == check:
                        add = int(chrome[demand][paths[path].l])
                        linksum = linksum + add
    linkloads.append(linksum)

print(linkloads)
                
            