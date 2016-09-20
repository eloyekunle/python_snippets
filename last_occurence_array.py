x = input()
# arr_size = int(x[0])
ele = x[2]
y = input()
arr = y.split()
arr_r = arr[::-1]
try:
    print(len(arr_r) - (arr_r.index(ele)))
except ValueError:
    print(-1)