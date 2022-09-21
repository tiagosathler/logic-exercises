#!/bin/python3

# import math
import os

# import random
# import re
# import sys

# Complete the catAndMouse function below.


def catAndMouse(x: int, y: int, z: int) -> str:
    """
    https://www.hackerrank.com/challenges/cats-and-a-mouse
    """
    dist_a = abs(x - z)
    dist_b = abs(y - z)

    if dist_a < dist_b:
        return "Cat A"
    elif dist_a > dist_b:
        return "Cat B"
    else:
        return "Mouse C"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + "\n")

    fptr.close()
