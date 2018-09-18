import os
import sys
import math

def floyd_warshall(m):
    # print(m)
    n = len(m)
    d_matrices = {0: m}

    for k in range(n):
        m_cur = d_matrices[k+1] = [[] for _ in range(n)]
        m_prev = d_matrices[k]
        for i in range(n):
            for j in range(n):
                # print(k,i,j)
                m_cur[i].append(min(m_prev[i][j], m_prev[i][k] + m_prev[k][j]))

        # Space efficiency.
        # print(d_matrices[k+1])
        del d_matrices[k]

    return d_matrices[n]

def roadsInHackerland(n, g_matrix):
    apsp = floyd_warshall(g_matrix)
    # print(apsp)
    return bin(sum(sum(e) for e in apsp) // 2)[2:]

if __name__ == '__main__':
    f = open('../data/johnland-001.txt')

    nm = f.readline().split()

    n = int(nm[0])

    m = int(nm[1])

    g_matrix = [[math.inf] * n for _ in range(n)]

    for _ in range(m):
        u,v,w = map(int, f.readline().rstrip().split())
        w1 = min(2 ** w, g_matrix[u-1][v-1])
        g_matrix[u-1][v-1] = w1
        g_matrix[v-1][u-1] = w1

    for i in range(n):
        g_matrix[i][i] = 0

    result = roadsInHackerland(n, g_matrix)

    print(result)
