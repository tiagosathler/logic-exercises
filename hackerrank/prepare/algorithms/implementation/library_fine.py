"""HackerRank
Library Fine
https://www.hackerrank.com/challenges/library-fine/
"""

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#


def library_fine(d1: int, m1: int, y1: int, d2: int, m2: int, y2: int) -> int:
    """Library Fine

    Args:
        d1 (int): returned day
        m1 (int): returned month
        y1 (int): returned year
        d2 (int): due day
        m2 (int): due month
        y2 (int): due year

    Returns:
        int: the amount of the fine or 0 if there is none
    """
    if y2 > y1:
        return 0

    if y1 > y2:
        return 10_000
    if m1 > m2 and y1 == y2:
        return (m1 - m2) * 500
    if d1 > d2 and m1 == m2:
        return (d1 - d2) * 15

    return 0


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # d1 = int(first_multiple_input[0])

    # m1 = int(first_multiple_input[1])

    # y1 = int(first_multiple_input[2])

    # second_multiple_input = input().rstrip().split()

    # d2 = int(second_multiple_input[0])

    # m2 = int(second_multiple_input[1])

    # y2 = int(second_multiple_input[2])

    # result = libraryFine(d1, m1, y1, d2, m2, y2)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    print(library_fine(9, 6, 2015, 6, 6, 2015))
    print(library_fine(6, 6, 2015, 9, 6, 2016))
    print(library_fine(2, 7, 1014, 1, 1, 1015))
    print(library_fine(15, 7, 2014, 1, 7, 2015))
