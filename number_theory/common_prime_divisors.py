"""
Problem Statement: https://app.codility.com/programmers/lessons/12-euclidean_algorithm/common_prime_divisors

Pretty much copied from after ~2hrs with no progress:
 https://codesays.com/2014/solution-to-common-prime-divisors-by-codility/
"""


from math import gcd


def solution(A, B):
    count = 0
    for j, k in zip(A, B):
        if calc_div(j, k):
            count += 1

    return count


def proc_div(x, y):
    while x != 1:
        gcd_val = gcd(x, y)

        if gcd_val == 1:
            break
        x //= gcd_val

    return x


def calc_div(x, y):
    common_div = gcd(x, y)

    x = proc_div(x, common_div)
    if x != 1:
        return False
    y = proc_div(y, common_div)
    return y == 1


if __name__ == '__main__':
    assert solution([15, 10, 9], [75, 30, 5]) == 1
