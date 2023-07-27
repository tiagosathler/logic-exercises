"""HackerRank
Cut the sticks
https://www.hackerrank.com/challenges/cut-the-sticks/
"""

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def cut_the_sticks(arr: list[int]) -> list[int]:
    """Cut the Sticks

    Args:
        arr (list[int]): the lengths of each stick

    Returns:
        list[int]: the number of sticks after each iteration
    """
    size = len(arr)
    result = [size]

    while size > 1:
        lower = min(arr)
        arr = [number - lower for number in arr if number > lower]
        size = len(arr)
        if size >= 1:
            result.append(size)

    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))

    # result = cutTheSticks(arr)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
    print(cut_the_sticks([5, 4, 4, 2, 2, 8]))
    print(cut_the_sticks([1, 2, 3, 4, 3, 3, 2, 1]))
