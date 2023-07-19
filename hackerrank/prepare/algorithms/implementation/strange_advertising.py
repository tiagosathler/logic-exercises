"""HackerRank
Viral Advertising
https://www.hackerrank.com/challenges/strange-advertising
"""

import math
# import os
# import random
# import re
# import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def viral_advertising(day: int) -> int:
    """Viral Advertising function

    Args:
        day (int): the day number to report

    Returns:
        int: the cumulative likes at that day
    """
    shared = int(5)
    cumulative = int(0)

    for _ in range(day):
        liked = math.floor(shared / 2)
        shared = liked * 3
        cumulative += liked

    return cumulative


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # result = viralAdvertising(n)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    print(viral_advertising(5))
