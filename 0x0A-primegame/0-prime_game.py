#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Prime Game"""
    if not nums or x < 1:
        return None
    if x != len(nums):
        return None

    ben, maria = 0, 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        remove_multiples(a, i)
    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    return None


def remove_multiples(ls, x):
    """Remove multiples of a prime number"""
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (IndexError, ValueError):
            break
