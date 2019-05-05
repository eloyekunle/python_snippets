def is_even(x):
    return(False if x & 1 else True) # bitwise and

x = int(input())
print(is_even(x))
