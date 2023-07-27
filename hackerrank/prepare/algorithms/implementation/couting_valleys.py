"""HackerRank
Counting Valleys
https://www.hackerrank.com/challenges/counting-valleys
"""


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


def counting_valleys(steps: int, path: str) -> int:
    """Counting the number of valleys

    Args:
        steps (int): the number of steps on the hike
        path (str): a string describing the path

    Returns:
        int: the number of valleys traversed
    """
    valleys = 0
    level = 0

    for step in range(0, steps):
        if path[step] == "U":
            level += 1
        else:
            level -= 1

        if level == 0 and path[step] == "U":
            valleys += 1

    return valleys


if __name__ == "__main__":
    # # fptr = open(os.environ["OUTPUT_PATH"], "w")

    # # steps = int(input().strip())
    # steps = 8

    # # path = input()
    # path = 'UDDDUDUU'

    # result = countingValleys(steps, path)

    # fptr.write(str(result) + "\n")
    # fptr.close()
    print(counting_valleys(8, "UDDDUDUU"))
