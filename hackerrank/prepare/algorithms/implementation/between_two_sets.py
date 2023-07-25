"""HackerRank
Between Two Sets
https://www.hackerrank.com/challenges/between-two-sets
"""

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def get_total_x(arr_a: list[int], arr_b: list[int]) -> int:
    """Between Two Sets

    Args:
        arr_a (list[int]): an array of integers
        arr_b (list[int]): an array of integers

    Returns:
        int: the number of integers that are between the sets
    """
    x_min = arr_a[-1]  # max value of arr_a
    x_max = arr_b[0]  # min value of arr_b

    factors: list[int] = []

    for number in range(x_min, x_max + 1):
        if all(number % a == 0 for a in arr_a) and all(
            b % number == 0 for b in arr_b
        ):
            factors.append(number)

    return len(factors)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # m = int(first_multiple_input[1])

    # arr = list(map(int, input().rstrip().split()))

    # brr = list(map(int, input().rstrip().split()))

    # total = getTotalX(arr, brr)

    # fptr.write(str(total) + '\n')

    # fptr.close()
    print(get_total_x([2, 4], [16, 32, 96]))
