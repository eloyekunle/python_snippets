# A palindrome is a string that reads the same forward and backward. Describe an algorithm for determining
# whether a string of n characters is a palindrome.


def palindrome(string):
    answer = True
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - 1 - i]:
            answer = False
            break

    return answer


strr = input("Enter a string: ")
message = palindrome(strr)
print(message)
