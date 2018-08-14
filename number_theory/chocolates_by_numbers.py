"""
Problem statement: https://app.codility.com/programmers/lessons/12-euclidean_algorithm/chocolates_by_numbers
"""


def solution(N, M):
    gcd = euclidean_algorithm(N, M)
    sol = 0

    if gcd:
        sol = N // gcd
    return sol


def euclidean_algorithm(x, y):
    if y == 0:
        return x
    return euclidean_algorithm(y, x % y)


if __name__ == '__main__':
    assert solution(10, 4) == 5
    assert solution(21, 6) == 7
    assert solution(0, 0) == 0
    assert solution(1, 1) == 1
