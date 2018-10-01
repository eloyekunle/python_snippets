#!/bin/python3

import os


def decibinaryNumbers(x):
    d = None

    for i in range(1, x+1):



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        x = int(input())

        result = decibinaryNumbers(x)

        fptr.write(str(result) + '\n')

    fptr.close()
