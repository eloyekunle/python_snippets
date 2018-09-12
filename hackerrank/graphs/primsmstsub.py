#!/bin/python3

import math
import os
import random
import re
import sys

class AdaptableHeapPriorityQueue():
    def add(self, key, value):
        pass

# Complete the prims function below.
def prims(n, edges, start):
    d = {}
    pq = AdaptableHeapPriorityQueue()
    locator = {}
    for i in range(1, n + 1):
        d[i] = math.inf
    d[start] = 0

    while not len(edges) == 0:
        pass
    return ''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    f = open('../../data/primsmstsub-001.txt')

    nm = f.readline().split()

    n = int(nm[0])

    m = int(nm[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, f.readline().rstrip().split())))

    start = int(f.readline())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
