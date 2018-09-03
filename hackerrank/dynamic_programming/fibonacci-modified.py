def fibonacciModified(t1, t2, n):
    for _ in range(2,n):
        fib = t1 + (t2 * t2)
        t2,t1 = fib,t2
    return t2

if __name__ == '__main__':
    assert fibonacciModified(0,1,5) == 5