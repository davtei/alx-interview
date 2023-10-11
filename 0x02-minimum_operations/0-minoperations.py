#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """
    A method that calculates the fewest number of operations needed to result
    in exactly n H characters in the file.
    Returns:
        [int]: [Minimum number of operations], or 0 if impossible
    """

    if n <= 1:
        return 0
    op = 0
    i = 2
    while i <= n:
        if n % i == 0:
            op += i
            n = n / i
            i = i - 1
        i = i + 1
    return int(op)
