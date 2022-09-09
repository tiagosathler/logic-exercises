#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1 - m
#  2. INTEGER v1 - m/jump
#  3. INTEGER x2 - m
#  4. INTEGER v2 - m/jump
#

def kangaroo(x1, v1, x2, v2):
    """
    https://www.hackerrank.com/challenges/kangaroo    
    """
    # x(j) = x1 + v1*j = x2 + v2*j
    # j = (x2 - x1)/(v1 - v2)
    delta_x = x2 - x1
    delta_v = v1 - v2

    if ((delta_x < 0 and delta_v > 0) or (delta_x != 0 and delta_v == 0)):
        return 'NO'

    j = delta_x / delta_v

    if ( j >= 0 and j % 1 == 0):
        return 'YES'

    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
