#!/bin/python3

# import math
# import os

# import random
# import re
# import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#


def pageCount(n: int, p: int) -> int:
    """
    https://www.hackerrank.com/challenges/drawing-book
    """
    if p <= n // 2:
        return p // 2
    else:
        return n // 2 - p // 2


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    # n = int(input().strip())
    n = 5

    # p = int(input().strip())
    p = 3

    result = pageCount(n, p)

    # fptr.write(str(result) + "\n")
    print(result)

    # fptr.close()
