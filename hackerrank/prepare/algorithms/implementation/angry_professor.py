"""HackerRank
Angry Professor
https://www.hackerrank.com/challenges/angry-professor
"""

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#


def angry_professor(threshold: int, arrival_times: list[int]) -> str:
    """Angry Professor

    Args:
        threshold (int):  the threshold number of students
        arrival_times (list[int]): the arrival times of the n students

    Returns:
        str: either YES or NO
    """
    arriving_on_time = 0
    for arrival in arrival_times:
        if arrival <= 0:
            arriving_on_time += 1
        if arriving_on_time >= threshold:
            return "NO"

    if arriving_on_time < threshold:
        return "YES"

    return "NO"


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input().strip())

    # for t_itr in range(t):
    #     first_multiple_input = input().rstrip().split()

    #     n = int(first_multiple_input[0])

    #     k = int(first_multiple_input[1])

    #     a = list(map(int, input().rstrip().split()))

    #     result = angryProfessor(k, a)

    #     fptr.write(result + '\n')

    # fptr.close()

    print(angry_professor(3, [-1, -3, 4, 2]))
    print(angry_professor(2, [0, -1, 2, 1]))
