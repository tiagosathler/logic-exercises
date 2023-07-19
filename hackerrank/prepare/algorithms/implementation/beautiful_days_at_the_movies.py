"""HackerRank
Beautiful Days at the Movies
https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/
"""

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#


def beautiful_days(minimum: int, maximum: int, divisor: int) -> int:
    """Beautiful days function

    Args:
        minimum (int): the starting day number
        maximum (int): the ending day number
        divisor (int): the divisor

    Returns:
        int: the number of beautiful days in the range
    """
    days = int(0)

    for day in range(minimum, maximum + 1):
        reversed_day = int("".join(reversed(str(day))))
        if (day - reversed_day) % divisor == 0:
            days += 1

    return days


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # i = int(first_multiple_input[0])

    # j = int(first_multiple_input[1])

    # k = int(first_multiple_input[2])

    # result = beautifulDays(i, j, k)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    print(beautiful_days(20, 23, 6))
