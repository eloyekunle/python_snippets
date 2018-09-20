#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the unboundedKnapsack function below.
def unboundedKnapsack(k, arr):
    arr = sorted(set(arr))
    n = len(arr)
    m = [[None] * (k + 1) for _ in range(n + 1)]

    m[0] = [0] * (k + 1)

    for i in range(n + 1):
        m[i][0] = 0

    for i in range(1, n + 1):
        mi_prev = m[i - 1]
        # print(mi_prev, m[i])
        for j in range(1, k + 1):
            # print(i, j, arr[i - 1])
            if arr[i - 1] > j:
                m[i][j] = mi_prev[j]
            else:
                m[i][j] = max(mi_prev[j], arr[i - 1] + m[i][j - arr[i - 1]])
    # print(m)
    return m[n][k]

if __name__ == '__main__':
    f = open('../data/unbounded-knapsack-001.txt')

    t = int(f.readline())

    for _ in range(t):
        nk = f.readline().split()

        n = int(nk[0])

        k = int(nk[1])

        arr = list(map(int, f.readline().rstrip().split()))

        result = unboundedKnapsack(k, arr)

        print(result)