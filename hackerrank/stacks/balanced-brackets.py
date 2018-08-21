def isBalanced(s):
    """
    Problem: https://www.hackerrank.com/challenges/balanced-brackets/problem
    :param s:
    :return:
    """
    stack = []
    openers= '[{('
    closers = ']})'
    for char in s:
        if char in openers:
            stack.append(char)
        elif char in closers:
            if len(stack) == 0:
                return False
            if closers.index(char) != openers.index(stack.pop()):
                return False
    return len(stack) == 0
