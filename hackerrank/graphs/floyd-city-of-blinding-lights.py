#!/bin/python3

import math
import os
import random
import re
import sys

def floyd_warshall(m):
    n = len(m)

    for k in range(n):
        kk = m[k]
        for i in range(n):
            ii = m[i]
            ik = ii[k]
            if ik == math.inf:
                continue
            for j in range(n):
                kj = kk[j]
                if kj == math.inf:
                    continue
                m[i][j] = min(ii[j], ik + kj)

    return m

if __name__ == '__main__':
    f = open('../data/floyd-city-of-blinding-lights-001.txt')

    n, m = map(int, f.readline().split())

    g_matrix = [[math.inf] * n for _ in range(n)]

    for _ in range(m):
        u,v,w = map(int, f.readline().rstrip().split())
        g_matrix[u-1][v-1] = w

    for i in range(n):
        g_matrix[i][i] = 0

    apsp = floyd_warshall(g_matrix)

    q = int(f.readline())

    for q_itr in range(q):
        xy = f.readline().split()

        x = int(xy[0])

        y = int(xy[1])

        if not apsp[x-1][y-1] == math.inf:
            print(apsp[x-1][y-1])
        else:
            print(-1)
