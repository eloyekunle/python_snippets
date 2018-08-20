from collections import deque

def array_left_rotation(a, rotations):
    """
    Problem: https://www.hackerrank.com/challenges/array-left-rotation/problem
    :param a:
    :param rotations:
    :return:
    """
    d = deque(a)
    d.rotate(-rotations)
    return list(d)
