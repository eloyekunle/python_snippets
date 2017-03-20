def binary_search(search_key, search_list):
    i = 0
    j = len(search_list) - 1

    while i < j:
        # For binary divisions, this is the same thing as middle_element = (i + j) // 2
        middle_element = i + (j - i) // 2
        if search_key > search_list[middle_element]:
            i = middle_element + 1
            print(search_list[i:j+1])
        else:
            j = middle_element
            print(search_list[i:j+1])

    if search_list[i] == search_key:
        return i

    return -1


search_list = list(map(int, input("Enter numbers, separated by space: ").split()))
search_key = int(input("Enter number to search for: "))
index = binary_search(search_key, search_list)
message = "Index = " + str(index) if index >= 0 else "Item not found"
print(message)
