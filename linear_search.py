def linear_search(key, arr):
	i = 0
	while i < len(arr):
		if arr[i] == key:
			return i
		i += 1
	return 0

search_list = list(map(int, input("Enter numbers, separated by space: ").split()))
search_key = int(input("Enter number to search for: "))
index = linear_search(search_key, search_list)
message = "Index = " + str(index) if index else "Item not found"
print(message)
