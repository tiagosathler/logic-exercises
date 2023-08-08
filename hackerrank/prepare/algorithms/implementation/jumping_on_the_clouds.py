"""HackerRank
Jumping on the Clouds
https://www.hackerrank.com/challenges/jumping-on-the-clouds
"""

# import math
# import os
# import random
# import re
# import sys


def jumping_on_clouds(clouds: list[int]) -> int:
    """Jumping on the clouds

    Args:
        clouds (list[int]): an array of binary integers

    Returns:
        int: the minimum number of jumps required
    """

    jumps = [value + 1 for value in clouds[1:-1]]

    index = 0

    while index < len(jumps) - 1:
        if jumps[index] == 1 and jumps[index + 1] == 1:
            jumps.pop(index + 1)

        elif jumps[index] == 2 and index + 1 < len(jumps) - 1:
            jumps.pop(index + 1)

        index += 1

    return max(len(jumps), 1)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nk = input().split()

    # n = int(nk[0])

    # k = int(nk[1])

    # c = list(map(int, input().rstrip().split()))

    # result = jumpingOnClouds(c, k)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    # print(jumping_on_clouds([0, 1, 0, 0, 0, 1, 0]))
    # print(jumping_on_clouds([0, 0, 1, 0, 0, 1, 0]))
    # response = jumping_on_clouds([0, 0, 0, 1, 0, 0])
    # print(response)
    # assert response == 3

    response = jumping_on_clouds([0, 0, 1, 0, 0, 1, 0])
    print(response)
    assert response == 4

    response = jumping_on_clouds([0, 0])
    print(response)
    assert response == 1

    response = jumping_on_clouds(
        [
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            0,
            1,
            0,
            1,
            0,
            0,
            0,
            1,
            0,
            0,
            1,
            0,
            0,
            0,
            1,
            0,
            1,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
            1,
            0,
            1,
            0,
            0,
        ]
    )
    print(response)
    assert response == 28
