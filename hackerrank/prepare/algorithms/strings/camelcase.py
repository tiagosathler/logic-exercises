#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def camelcase(s: str) -> int:
    """
    https://www.hackerrank.com/challenges/camelcase
    """
    count = 1
    for char in s:
        if char.isupper():
            count += 1
    return count


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    # result = camelcase(s)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    s = "saveChangesInTheEditor"

    result = camelcase(s)

    print(result)
