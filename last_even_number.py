# An algorithm that takes as input a list of n integers and finds the location of the last even integer in the
# list or returns 0 if there are no even integers in the list.


def last_even_number(numbers):
    index = None
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            index = (numbers[i], i)

    return index


nums = list(map(int, input("Enter a sequence of numbers, separated by space: ").split()))
last_even = last_even_number(nums)
if last_even:
    print("The last even number is", last_even[0], "at index", last_even[1])
else:
    print(0)
