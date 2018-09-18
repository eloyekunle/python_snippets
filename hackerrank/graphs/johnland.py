#!/bin/python3

import os
import sys

#
# Complete the roadsInHackerland function below.
#
def roadsInHackerland(n, roads):
    """
    https://www.hackerrank.com/challenges/johnland/problem
    :param n:
    :param roads:
    :return:
    """
#
# Write your code here.
#

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    roads = []

    for _ in range(m):
        roads.append(list(map(int, input().rstrip().split())))

    result = roadsInHackerland(n, roads)

    fptr.write(result + '\n')

    fptr.close()
