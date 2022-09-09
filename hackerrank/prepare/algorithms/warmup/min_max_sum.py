#!/bin/python3

import math
import os
import random
import re
import sys
import math

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    """
    https://www.hackerrank.com/challenges/mini-max-sum    
    """
    min = math.inf
    max = -math.inf

    for i in range(len(arr)):
        sum = 0
        for j, y in enumerate(arr):
            if (i != j):
                sum += y
        if sum < min:
            min = sum
        if sum > max:
            max = sum

    print("%d %d" % (min, max))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
