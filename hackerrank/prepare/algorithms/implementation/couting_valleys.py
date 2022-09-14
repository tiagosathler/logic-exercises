#!/bin/python3

# import math

# import random
# import re
# import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps: int, path: str) -> int:
    """
    https://www.hackerrank.com/challenges/counting-valleys
    """
    valleys = 0
    level = 0
    for step in path:
        if step == "U":
            level += 1
        else:
            level -= 1
        if level == 0 and step == "U":
            valleys += 1
    return valleys


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    # steps = int(input().strip())
    steps = 8

    # path = input()
    path = 'UDDDUDUU'

    result = countingValleys(steps, path)

    # fptr.write(str(result) + "\n")
    print(result)
    # fptr.close()
