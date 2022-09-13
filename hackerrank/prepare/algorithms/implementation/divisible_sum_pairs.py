#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#


def divisibleSumPairs(n: int, k: int, ar: list[int]) -> int:
    """
    https://www.hackerrank.com/challenges/divisible-sum-pairs/
    """
    result = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            sum = ar[i] + ar[j]
            if sum % k == 0:
                result += 1
    return result


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])
    n = 6

    # k = int(first_multiple_input[1])
    k = 3

    # ar = list(map(int, input().rstrip().split()))
    ar = [1, 3, 2, 6, 1, 2]

    result = divisibleSumPairs(n, k, ar)

    # fptr.write(str(result) + "\n")
    print(result)

    # fptr.close()
