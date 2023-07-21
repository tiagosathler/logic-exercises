"""HackerRank
Save The Prisoners
https://www.hackerrank.com/challenges/save-the-prisoner
"""

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#


def save_the_prisoner(prisoners: int, sweets: int, chair: int) -> int:
    """Given M sweets and a circular queue of N prisoners,
    find the ID of the last prisoner to receive a sweet.

    Args:
        prisoners (int): the number of prisoners
        sweets (int): the number of sweets
        chair (int): the chair number to begin passing out sweets from

    Returns:
        int: the chair number of the prisoner to warn
    """
    remainder = sweets % prisoners

    if remainder == 0:
        remainder = prisoners

    position = remainder + chair - 1

    if position <= prisoners:
        return position

    return position - prisoners


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input().strip())

    # for t_itr in range(t):
    #     first_multiple_input = input().rstrip().split()

    #     n = int(first_multiple_input[0])

    #     m = int(first_multiple_input[1])

    #     s = int(first_multiple_input[2])

    #     result = saveThePrisoner(n, m, s)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
    # print(save_the_prisoner(5, 2, 1))
    # print(save_the_prisoner(5, 2, 2))
    # print(save_the_prisoner(7, 19, 2))
    # print(save_the_prisoner(3, 7, 3))

    matrix = [
        [1000000000, 1, 213261504],
        [560644246, 7879023, 2],
        [1000000000, 847287808, 999999999],
        [999999999, 27602, 999969369],
        [53, 694907486, 2],
        [198, 508815647, 1],
        [999999999, 999999998, 914195001],
        [158, 355311663, 2],
        [7, 770713665, 6],
        [559971089, 559971089, 559971088],
        [177, 35398760, 176],
        [29, 514245574, 1],
        [5, 562808318, 2],
        [909, 500472699, 590],
        [141, 121950476, 140],
        [172, 873591946, 1],
        [14, 94396418, 13],
        [6, 630393971, 5],
    ]
    for line in matrix:
        print(save_the_prisoner(line[0], line[1], line[2]))
