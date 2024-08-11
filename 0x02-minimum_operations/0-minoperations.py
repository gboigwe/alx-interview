#!/usr/bin/env python3
"""This code contains function for minimum operations"""


def minOperations(n):
    """Performing operations needed to result in
    n H character times
        Return 0 if n cannot be obtained
    """
    if n <= 1:
        return 0

    min_ope = 0
    div = 2

    while n > 1:
        while n % div == 0:
            min_ope += div
            n //= div
        div += 1
    return min_ope


if __name__ == "__main__":
    # test code here
    pass
