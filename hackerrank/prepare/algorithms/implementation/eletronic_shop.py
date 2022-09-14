#!/bin/python3

import os
import math

# import sys


def getMoneySpent(keyboards: list[int], drives: list[int], b: int) -> int:
    """
    https://www.hackerrank.com/challenges/electronics-shop/
    """
    max = -math.inf
    for keyboard in keyboards:
        for drive in drives:
            sum = keyboard + drive
            if max < sum <= b:
                max = sum
    if max != -math.inf:
        return max
    else:
        return -1


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + "\n")

    fptr.close()
