def equal(arr):
    m = min(arr)
    f = 100000000
    for i in range(3):
        s = 0
        for num in arr:
            delta = num - m + i
            s += delta // 5 + delta % 5 // 2 + delta % 5 % 2

        f = min(f, s)
    return f

if __name__ == '__main__':
    assert equal([2, 2, 3, 7]) == 2
    assert equal([10, 7, 12]) == 3
