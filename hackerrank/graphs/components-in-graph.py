#!/bin/python3

import os
import sys
from data_structures.graph_no_vertice_object import Graph
from data_structures.partition import Partition

def componentsInGraph(gb):
    forest = Partition()
    p = {}
    for v in gb.vertices():
        p[v] = forest.make_group(v)

    for

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gb = Graph()

    for _ in range(n):
        gb.insert_edge(*map(int, input().rstrip().split()))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, SPACE)))
    fptr.write('\n')

    fptr.close()
