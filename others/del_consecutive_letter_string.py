import sys

x = int(input())
while x > 0:
    y = input()
    sys.stdout.write(y[0])
    for i in range(1, len(y)):
        if y[i] != y[i - 1]:
            sys.stdout.write(y[i])
    print()
    x -= 1
