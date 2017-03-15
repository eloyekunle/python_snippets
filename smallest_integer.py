# an algorithm for finding the smallest integer in a finite sequence of natural numbers.


def smallest_integer(numbers):
    smallest = numbers[0]
    for i in range(1, len(numbers) - 1):
        if numbers[i] < smallest:
            smallest = numbers[i]

    return smallest


nums = list(map(int, input("Enter a sequence of space-separated integers: ").split()))
smallest_int = smallest_integer(nums)
print("The smallest integer is", smallest_int)
