#!/bin/python3

def abbreviation(a, b):
    len_a = len(a)
    len_b = len(b)
    s = [[False] * (len_a + 1) for _ in range(len_b + 1)]
    s[0][0] = True

    for k in range(1, len_a + 1):
        if a[k-1].islower():
            s[0][k] = s[0][k-1]

    for i in range(1, len_b + 1):
        c_b = b[i-1]
        for j in range(1, len_a + 1):
            c_a = a[j-1]
            if c_a.isupper():
                if c_a == c_b:
                    s[i][j] = s[i-1][j-1]
            elif c_a.upper() == c_b:
                s[i][j] = s[i-1][j-1] or s[i][j-1]
            else:
                s[i][j] = s[i][j-1]
    if s[-1][-1]:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    f = open('/home/elijah/MyCode/python_snippets/data/abbr-003.txt')
    q = int(f.readline())
    results = open('../../data/abbr-003.sol.txt').readlines()

    for q_itr in range(q):
        a = f.readline().rstrip()

        b = f.readline().rstrip()

        result = abbreviation(a, b)

        result_correct = results[q_itr].rstrip()
        assert result == result_correct