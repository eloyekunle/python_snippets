# This algorithm takes as input a list of n integers and produces as output the largest difference obtained
#  by subtracting an integer in the list from the one following it.


def largest_difference_in_elements(elements):
    difference = elements[1] - elements[0]
    for i in range(len(elements) - 1):
        current_difference = elements[i + 1] - elements[i]
        print(elements[i + 1], "-", elements[i], "=", current_difference)
        if current_difference > difference:
            difference = current_difference

    return difference


numbers = list(
    map(int, input("Enter the list of numbers, separated by a space: ").split())
)
diff = largest_difference_in_elements(numbers)
print("The largest difference is:", diff)
