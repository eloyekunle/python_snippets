# an algorithm that takes as input a list of n distinct integers and finds the location of the largest even
# integer in the list or returns 0 if there are no even integers in the list.


def largest_even_number(numbers):
    largest_even = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            if numbers[i] > largest_even:
                largest_even = numbers[i]

    return largest_even


nums = list(
    map(int, input("Enter a sequence of numbers, separated by a space: ").split())
)
largest_ev = largest_even_number(nums)
print(largest_ev)
