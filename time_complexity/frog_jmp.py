from math import ceil


def solution(x, y, d):
    return ceil((y - x) / d)


if __name__ == '__main__':
    assert solution(10, 85, 30) == 3
    assert solution(0, 30, 40) == 1
    assert solution(0, 0, 40) == 0
    assert solution(30, 40, 0) == 0
