# an algorithm to compute x^n , where x is a real number and n is an integer.


def exponential(num, exponent):
    number = num
    abs_exponent = abs(exponent)
    while abs_exponent > 1:
        num *= number
        abs_exponent -= 1
    if exponent == 0:
        return 1
    if exponent < 0:
        return 1 / num  # Returns 1/x^n

    return num


number = list(
    map(int, input("Enter a number and the exponent, space separated: ").split())
)
exponent = exponential(number[0], number[1])
print(exponent)
