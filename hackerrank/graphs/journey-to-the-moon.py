import math
import os
import random
import re
import sys
from collections import Counter

def dfs(g, u, discovered, c):
    for v in g[u]:
        if v not in discovered:
            discovered[v] = c
            dfs(g, v, discovered, c)

def journeyToMoon(n, astronaut):
    g = {}
    for i in range(n):
        g[i] = set()

    for a, b in astronaut:
        g[a].add(b)
        g[b].add(a)

    forest = {}
    component = 0
    for v in range(n):
        if v not in forest:
            forest[v] = component
            dfs(g, v, forest, component)
            component += 1

    vs = Counter(forest.values()).values()

    c_sum = 0
    result = 0
    for s in vs:
        result += c_sum * s
        c_sum += s

    return result

if __name__ == '__main__':
    f = open('/home/elijah/Downloads/input13.txt')

    np = f.readline().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, f.readline().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    print(result)
