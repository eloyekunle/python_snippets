# an algorithm that locates an element in a list of increasing integers by successively splitting
# the list into four sublists of equal (or as close to equal as
# possible) size, and restricting the search to the appropriate piece.


def fourary_search(key, numbers):
    i = 0
    j = len(numbers) - 1
    while i < j - 1:
        lo = i + (j - i) // 4
        mi = i + (j - i) // 2  # Same as i + 2 * (j - i) // 4 since 2/4 = 1/2
        hi = i + 3 * (j - i) // 4
        if key > numbers[hi]:
            i = hi + 1
            print(numbers[i : j + 1])
        elif key > numbers[mi]:
            i = mi + 1
            j = hi
            print(numbers[i : j + 1])
        elif key > numbers[lo]:
            i = lo + 1
            j = mi
            print(numbers[i : j + 1])
        else:
            j = lo
            print(numbers[i : j + 1])

    if key == numbers[i]:
        location = i
    elif key == numbers[j]:
        location = j
    else:
        location = 0

    return location


search_list = list(
    map(int, input("Enter sorted numbers, separated by space: ").split())
)
search_key = int(input("Enter number to search for: "))
index = fourary_search(search_key, search_list)
message = "Index = " + str(index) if index >= 0 else "Item not found"
print(message)
