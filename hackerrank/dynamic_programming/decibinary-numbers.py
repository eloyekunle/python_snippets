#!/bin/python3

def decibinaryNumbers(x):
    pass

if __name__ == '__main__':
    f = open('../data/decibinary-numbers-003.txt')

    q = int(f.readline())

    decs = [[0]]

    for q_itr in range(q):
        x = int(f.readline())

        result = decibinaryNumbers(x)

        print(result)
