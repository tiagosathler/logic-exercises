"""HackerRank
The Hurdle Race
https://www.hackerrank.com/challenges/the-hurdle-race
"""

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#


def hurdle_race(k: int, height: list[int]) -> int:
    """Hurdle Race function

    Args:
        k (int): the height the character can jump naturally
        height (list[int]): the heights of each hurdle

    Returns:
        int: the minimum number of doses required, always 0 or more
    """
    max_height = max(height)
    if max_height > k:
        return max_height - k
    return 0


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # k = int(first_multiple_input[1])

    # height = list(map(int, input().rstrip().split()))

    j = int(4)
    height_values = [1, 6, 3, 5, 2]

    result = hurdle_race(j, height_values)
    print(result)

    j = int(7)
    height_values = [2, 5, 4, 5, 2]

    result = hurdle_race(j, height_values)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
