#!/bin/python3

import os

# Takes in Decibinary number and returns decimal equivalent.
# Input - 2016, Output - 24; Input - 2008, Output - 24
def dbn_to_dec(n):
    n = str(n)
    k = 0
    for i in range(len(n)):
        k += (int(n[i]) * 2**(len(n) - i - 1))
    return k

# Gets the current number to disintegrate, and the 'disintegration' index.
# Input - 60, Output - (11, 8).
def num_and_offset(x):
    j = 1
    i = 0
    while x-j > 0:
        x -= j
        i += 1
        if i == 2:
            j = 2
        elif i % 2 == 0:
            j += 2
    return i, x

def decibinaryNumbers(x):
    # num, offset = num_and_offset(x)
    num, offset = (0, 0)
    sums = 0

    for i in range(len(decs), x):
        sums += len(decs[-1])
        print(i, sums)
        decs_i = set()
        for j in decs[i-1]:
            str_j = str(j)
            if str_j[-1] == 9:
                continue
            decs_i.add(j + 1)
            if str_j[-1] == '1':
                decs_i.add(j + 9)
        decs_i.add(int(bin(i)[2:]))
        decs.append(sorted(decs_i))

    # print(decs)
    return decs[num][offset - 1]


if __name__ == '__main__':
    f = open('../data/decibinary-numbers-002.txt.big')

    q = int(f.readline())

    decs = [[0]]

    for q_itr in range(q):
        x = int(f.readline())

        result = decibinaryNumbers(x)

        print(result)
