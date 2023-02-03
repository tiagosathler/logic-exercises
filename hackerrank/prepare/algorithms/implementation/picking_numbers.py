#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

from typing import List


def pickingNumbers(a: List[int]) -> List[int]:
    """
    https://www.hackerrank.com/challenges/picking-numbers
    """
    lists = {e: list() for e in a}

    for e, l in enumerate(lists):
        continue

    sub_array = list()
    for i in range(len(a)):
        condition = True
        for j in range(len(a)):
            if i != j and abs(a[i] - a[j]) > 1:
                condition = False
                break
        if condition:
            sub_array.append(a[i])
    return sub_array


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # a = list(map(int, input().rstrip().split()))

    # result = pickingNumbers(a)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    a = [4, 6, 5, 3, 3, 1]
    result = pickingNumbers(a)
    print(result)
