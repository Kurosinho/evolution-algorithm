class Link:
    def __init__(self, number, node1, node2, capacity):
        self.number = number
        self.node1 = node1
        self.node2 = node2
        self.capacity = capacity

    def __str__(self) -> str:
        return f"{self.number} {self.node1} {self.node2} {self.capacity}"

class Demand:
    def __init__(self, number, node1, node2, volume):
        self.number = number
        self.node1 = node1
        self.node2 = node2
        self.volume = volume

    def __str__(self) -> str:
        return f"{self.number} {self.node1} {self.node2} {self.volume}"


class Path:
    def __init__(self, amount, paths):
        self.amount = amount
        self.paths = paths

    def __str__(self) -> str:
        return f"{self.amount} {self.paths}"


f = open("data.txt", "r")
f.readline()
links = []
demands = []
paths = []

for x in range(5):
    linkData = f.readline()
    newData = linkData.split(" ")
    link = Link(newData[0], newData[1], newData[2], newData[3])
    links.append(link)

f.readline()
f.readline()

for x in range(6):
    demandData = f.readline()
    newData = demandData.split(" ")
    demand = Demand(newData[0], newData[1], newData[2], newData[3])
    demands.append(demand)
    no_of_links = int(f.readline())
    for i in range(no_of_links):
        pathData = f.readline()
        newPath = pathData.split(" ")
        path = Path(newPath[0], newPath[1:])
        paths.append(path)
    f.readline()

print("Links:")
for a in range(len(links)):
    print(links[a])

print("Demands:")
for b in range(len(demands)):
    print(demands[b])

print("Paths:")
for c in range(len(paths)):
    print(paths[c])
