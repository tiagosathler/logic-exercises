#!/bin/python3

import os

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#


def simpleArraySum(ar: list[int]) -> int:
    """
    https://www.hackerrank.com/challenges/simple-array-sum/
    """
    result = 0
    for value in ar:
        result += value
    return result


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + "\n")

    fptr.close()
