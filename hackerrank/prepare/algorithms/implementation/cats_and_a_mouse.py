"""
Cats And A Mouse
https://www.hackerrank.com/challenges/cats-and-a-mouse
"""

# import math
# import os
# import random
# import re
# import sys

# Complete the catAndMouse function below.


def cat_and_mouse(
    cat_a_position: int, cat_b_position: int, mouse_c_position: int
) -> str:
    """Cats and Mouse

    Args:
        cat_a_position (int): cat A's position
        cat_b_position (int): cat B's position
        mouse_c_position (int): mouse C's position

    Returns:
        str: either "Cat A", "Cat B", or "Mouse C"
    """
    dist_a = abs(cat_a_position - mouse_c_position)
    dist_b = abs(cat_b_position - mouse_c_position)

    if dist_a < dist_b:
        return "Cat A"
    if dist_a > dist_b:
        return "Cat B"
    return "Mouse C"


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    # q = int(input())

    # for q_itr in range(q):
    #     xyz = input().split()

    #     x = int(xyz[0])

    #     y = int(xyz[1])

    #     z = int(xyz[2])

    #     result = catAndMouse(x, y, z)

    #     fptr.write(result + "\n")

    # fptr.close()
    print(cat_and_mouse(1, 2, 3))
    print(cat_and_mouse(1, 3, 2))
