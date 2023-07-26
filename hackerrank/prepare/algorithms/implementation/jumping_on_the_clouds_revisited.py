"""HackerRank
Jumping on the Clouds: Revisited
https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited
"""

# import math
# import os
# import random
# import re
# import sys


def jumping_on_clouds(clouds: list[int], jump_length: int) -> int:
    """Jumping on the clouds

    Args:
        clouds (list[int]): the cloud types along the path
        jump_length (int): the length of one jump

    Returns:
        int: the energy level remaining
    """
    energy = 100
    index = 0
    cloud_count = len(clouds)

    while True:
        index = (index + jump_length) % cloud_count

        energy -= 1 + 2 * clouds[index]

        if index == 0:
            break

    return energy


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nk = input().split()

    # n = int(nk[0])

    # k = int(nk[1])

    # c = list(map(int, input().rstrip().split()))

    # result = jumpingOnClouds(c, k)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    print(jumping_on_clouds([0, 0, 1, 0, 0, 1, 1, 0], 2))
    print(jumping_on_clouds([1, 1, 1, 0, 1, 1, 0, 0, 0, 0], 3))
