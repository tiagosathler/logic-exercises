#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(n: int, arr: list):
    """
    https://www.hackerrank.com/challenges/plus-minus
    """
    negative = 0
    positive = 0
    zeros = 0
    for value in arr:
        if (value < 0):
            negative += 1
        elif (value > 0):
            positive += 1
        else:
            zeros += 1
    negative /= n
    positive /= n
    zeros /= n

    print("%.6f" % positive)
    print("%.6f" % negative)
    print("%.6f" % zeros)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(n, arr)
