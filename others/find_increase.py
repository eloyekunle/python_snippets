# an algorithm that finds all terms of a finite sequence of integers that are greater than the sum of all
# previous terms of the sequence.


def find_increase(numbers):
    increases = []
    length = len(numbers)
    for i in range(1, length):
        summation = 0
        for j in range(i):
            summation += numbers[j]
        if numbers[i] > summation:
            increases.append(numbers[i])

    return increases


the_numbers = list(map(int, input("Enter space-separated integers: ").split()))
all_increases = find_increase(the_numbers)
print(all_increases)
