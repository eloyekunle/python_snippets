#!/bin/python3

import os
import sys
from data_structures.partition_min import Partition

def componentsInGraph(g, b):
    forest = Partition()
    p = {}

    for v in set(g):
        p[v] = forest.make_group(v)

    for v in set(b):
        p[v] = forest.make_group(v)

    s = list(zip(g,b))
    while len(s) != 0:
        n,m = s.pop()
        a = forest.find(p[n])
        b = forest.find(p[m])

        if a != b:
            forest.union(a,b)

    vals = [len(x) for x in forest.positions()]
    return min(vals), max(vals)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    g = []
    b = []

    for _ in range(n):
        e = [int(x) for x in sys.stdin.readline().rstrip().split()]
        g.append(e[0])
        b.append(e[1])

    result = componentsInGraph(g, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()