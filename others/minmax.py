def minmax(x):
    x.sort()
    smallest = x[0]
    largest = x[-1]
    return (smallest, largest)


items = input()
print(minmax(items))
