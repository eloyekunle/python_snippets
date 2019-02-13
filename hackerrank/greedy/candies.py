#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    candies = [None] * n
    candies[0] = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            candies[i] = candies[i-1] + 1
        else:
            candies[i] = 1

    for i in reversed(range(0, len(arr) - 1)):
        if arr[i] > arr[i + 1] and candies[i] <= candies[i + 1]:
            candies[i] = candies[i+1] + 1

    return sum(candies)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
