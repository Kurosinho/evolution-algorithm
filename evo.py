import read_data
import random
import numpy as np

class gene:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

links, demands, paths = read_data("data.txt")

genes = []

for i in range(len(demands)):
    hd = demands[i].volume
    for j in range(demands[i].no_of_links):
        x = random.randint(0, hd)
        allelles = []
        for k in range(3):


pd, d = (3, len(demands))
chromosome = 