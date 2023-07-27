"""HackerRank
Sherlock and Squares
https://www.hackerrank.com/challenges/sherlock-and-squares/
"""

import math

# import os
# import random
# import re
# import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#


def squares(lower: int, upper: int) -> int:
    """Squares Integers

    Args:
        lower (int): the lower range boundary
        upper (int): the upper range boundary

    Returns:
        int: the number of square integers in the range
    """
    min_square_root = math.ceil(math.sqrt(lower))
    max_square_root = math.floor(math.sqrt(upper))

    return max_square_root - min_square_root + 1


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # q = int(input().strip())

    # for q_itr in range(q):
    #     first_multiple_input = input().rstrip().split()

    #     a = int(first_multiple_input[0])

    #     b = int(first_multiple_input[1])

    #     result = squares(a, b)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
    print(squares(24, 49))
