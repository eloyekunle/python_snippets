def is_multiple(n, m):
    return(True if m%n == 0 else False)

pieces = input().split()
x = int(pieces[0])
y = int(pieces[1])

print(is_multiple(x, y))
