def last_even_number(numbers):
    index = None
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            index = (numbers[i], i)

    return index


nums = list(map(int, input("Enter a sequence of numbers, separated by space: ").split()))
last_even = last_even_number(nums)
print("The last even number is", last_even[0], "at index", last_even[1])
