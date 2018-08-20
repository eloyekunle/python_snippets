def solution(N):
    """
    Problem Statement: https://app.codility.com/programmers/lessons/1-iterations/binary_gap
    """
    binary_rep = format(N, 'b')
    longest_length = 0
    i = 0
    len_br = len(binary_rep)
    while i < len_br:
        if binary_rep[i] == '0':
            count = 0
            while i < len_br and binary_rep[i] == '0':
                count += 1
                i += 1
            if i < len_br and binary_rep[i] == '1' and count > longest_length:
                longest_length = count
        else:
            i += 1

    return longest_length


if __name__ == '__main__':
    assert (solution(1041) == 5)
    assert (solution(-1041) == 5)
    assert (solution(32) == 0)
    assert (solution(529) == 4)
    assert (solution(9) == 2)
    assert (solution(20) == 1)
    assert (solution(15) == 0)
    assert (solution(32) == 0)
    assert (solution(0) == 0)
