# The ternary search algorithm locates an element in a list
# of increasing integers by successively splitting the list into
# three sublists of equal (or as close to equal as possible)
# size, and restricting the search to the appropriate piece.


def ternary_search(key, numbers):
    i = 0
    j = len(numbers) - 1
    while i < j - 1:
        low = i + (j - i) // 3
        upper = i + 2 * (j - i) // 3

        if key > numbers[upper]:
            i = upper + 1
            print(numbers[i : j + 1])
        elif key > numbers[low]:
            i = low + 1
            j = upper
            print(numbers[i : j + 1])
        else:
            j = low
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
index = ternary_search(search_key, search_list)
message = "Index = " + str(index) if index >= 0 else "Item not found"
print(message)
