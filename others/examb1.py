def fibonnaci(n):
    if n == 1 or n == 2:
        return 1
    elif num > 2:
        fib = fibonnaci(n - 1) + fibonnaci(n - 2)
        return fib


num = input("Enter a number\n=>")

while num > 0:
    print(fibonnaci(num))
    num -= 1
