"""
Apple and Orange
https://www.hackerrank.com/challenges/apple-and-orange
"""


# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER start
#  2. INTEGER end
#  3. INTEGER apple_tree
#  4. INTEGER orange_tree
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#


def count_apples_and_oranges(
    start: int,
    end: int,
    apple_tree: int,
    orange_tree: int,
    apples: list[int],
    oranges: list[int],
) -> None:
    """Count Apples and Oranges

    Args:
        start (int): starting point of Sam's house location
        end (int): ending location of Sam's house location
        apple_tree (int): location of the Apple tree
        orange_tree (int): location of the Orange tree
        apples (list[int]): distances at which each apple falls from the tree
        oranges (list[int]): distances at which each orange falls from the tree
    """

    apples_count = 0
    oranges_count = 0

    for apple in apples:
        if start <= apple + apple_tree <= end:
            apples_count += 1

    for orange in oranges:
        if start <= orange + orange_tree <= end:
            oranges_count += 1

    print(apples_count)
    print(oranges_count)


if __name__ == "__main__":
    # first_multiple_input = input().rstrip().split()

    # s = int(first_multiple_input[0])

    # t = int(first_multiple_input[1])

    # second_multiple_input = input().rstrip().split()

    # a = int(second_multiple_input[0])

    # b = int(second_multiple_input[1])

    # third_multiple_input = input().rstrip().split()

    # m = int(third_multiple_input[0])

    # n = int(third_multiple_input[1])

    # apples = list(map(int, input().rstrip().split()))

    # oranges = list(map(int, input().rstrip().split()))

    count_apples_and_oranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])
