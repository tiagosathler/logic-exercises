#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    """
    https://www.hackerrank.com/challenges/staircase
    """
    for i in range(n):
        result = " " * (n - 1 - i)
        result += "#" * (i + 1)
        print(result)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
