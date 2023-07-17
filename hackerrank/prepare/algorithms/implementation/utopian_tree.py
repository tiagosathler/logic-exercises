"""HackerRank
Utopian Tree
https://www.hackerrank.com/challenges/utopian-tree/
"""

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def utopian_tree(cycles: int) -> int:
    """Utopian Tree

    Args:
        cycles (int): the number of growth cycles to simulate

    Returns:
        int: the height of the tree after the given number of growth cycles
    """
    height = 1

    for i in range(1, cycles + 1):
        if i % 2 == 0:
            height += 1
        else:
            height *= 2

    return height


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input().strip())

    # for t_itr in range(t):
    #     n = int(input().strip())

    #     result = utopianTree(n)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
    result = utopian_tree(0)
    print(result)

    result = utopian_tree(1)
    print(result)

    result = utopian_tree(4)
    print(result)
