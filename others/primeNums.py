def primeNums(n):
    i = 2
    while i < n:
        j = 2
        while j < i:
            if i % j == 0:
                break
            else:
                print(i)
                break
            j += 1
        i += 1


primeNums(25)
