#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubarray function below.
def maxSubarray(arr):
    max_subseq_sum = None
    max_subarr_sum = None

    if max(arr) <= 0:
        max_subarr_sum = max_subseq_sum = max(arr)
    elif min(arr) >= 0:
        max_subarr_sum = max_subseq_sum = sum(arr)
    else:
        max_subarr_sum = max_subarr_ending_here = arr[0]
        max_subseq_sum = max_subseq_ending_here = 0

        for i in range(1, len(arr)):
            el = arr[i]
            max_subarr_ending_here = max(el, max_subarr_ending_here + el)
            max_subarr_sum = max(max_subarr_sum, max_subarr_ending_here)

        for el in arr:
            max_subseq_ending_here = max(el, 0)
            max_subseq_sum += max_subseq_ending_here

    return [max_subarr_sum, max_subseq_sum]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
