#!/bin/python3

def abbreviation(a, b):
    c_a = c_b = None
    len_a = len(a)
    len_b = len(b)
    s = [[0] * (len_a + 1) for _ in range(len_b + 1)]
    # Loop over target string
    for i in range(len_b):
        c_b = b[i]
        c_b_upper = c_b.isupper()
        s[i][0] = i
        # Compare original string, start from current index in target string.
        for j in range(1, len_a + 1):
            c_a = a[j-1]
            if i == 0:
                s[i][j] = j
            elif j < i:
                s[i][j] = 1001
            elif c_b == c_a:
                s[i][j] = min(s[i-1][j], s[i][j-1], s[i-1][j-1])
            elif c_b_upper and c_a.upper() == c_b:
                s[i][j] = min(s[i-1][j], s[i][j-1], s[i-1][j-1]) + 1
            elif 9999 in (s[i-1][j], s[i][j-1], s[i-1][j-1]):
                s[i][j] = 9999
            else:
                s[i][j] = 9999
    print(s)
    return 'YES'

if __name__ == '__main__':
    f = open('/home/elijah/MyCode/python_snippets/data/abbr-001.txt')
    q = int(f.readline())

    for q_itr in range(q):
        a = f.readline().rstrip()

        b = f.readline().rstrip()

        result = abbreviation(a, b)

        print(result)