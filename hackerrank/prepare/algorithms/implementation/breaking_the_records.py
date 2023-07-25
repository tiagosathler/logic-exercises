"""
Breaking the Records
https://www.hackerrank.com/challenges/breaking-best-and-worst-records
"""

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breaking_records(scores: list[int]) -> list[int]:
    """Breaking the records function

    Args:
        scores (list[int]): points scored per game

    Returns:
        list[int]: an array with the numbers of times she broke her records
        Index 0 is for breaking most points records,
        and index 1 is for breaking least points records.
    """

    max_score = scores[0]
    max_count = 0

    min_score = scores[0]
    min_count = 0

    for score in scores:
        if score > max_score:
            max_score = score
            max_count += 1
        if score < min_score:
            min_score = score
            min_count += 1

    return [max_count, min_count]


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # scores = list(map(int, input().rstrip().split()))

    # result = breakingRecords(scores)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
    print(breaking_records([10, 5, 20, 20, 4, 5, 2, 25, 1]))
