"""HackerRank
Chocolate Feast
https://www.hackerrank.com/challenges/chocolate-feast/
"""

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#


def chocolate_feast(money: int, price: int, packaging: int) -> int:
    """Chocolate feast

    Args:
        money (int): money in your pocket
        price (int): chocolate price
        packaging (int): packaging he gives to the store


    Returns:
        int: the total number of chocolates Brenno eats
    """
    total_chocolates = money // price

    if total_chocolates < packaging:
        return total_chocolates

    eats = total_chocolates

    bonus, remainder = divmod(total_chocolates, packaging)

    while bonus > 0:
        eats += bonus
        bonus, remainder = divmod(bonus + remainder, packaging)

    return eats

    # total_chocolates = money // price
    # eats = total_chocolates

    # while total_chocolates >= packaging:
    #     additional_chocolates, remaining_wrappers = divmod(
    #         total_chocolates, packaging
    #     )
    #     eats += additional_chocolates
    #     total_chocolates = additional_chocolates + remaining_wrappers

    # return eats


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input().strip())

    # for t_itr in range(t):
    #     first_multiple_input = input().rstrip().split()

    #     n = int(first_multiple_input[0])

    #     c = int(first_multiple_input[1])

    #     m = int(first_multiple_input[2])

    #     result = chocolateFeast(n, c, m)

    #     fptr.write(str(result) + '\n')

    # fptr.close()

    data = [
        [12, 4, 4],
        [10, 2, 5],
        [6, 2, 2],
        [16779, 1, 5886],
        [1448, 5, 178],
        [74597, 11527, 6],
    ]

    response = [
        3,
        6,
        5,
        16781,
        290,
        7,
    ]

    for arg, output in zip(data, response):
        response = chocolate_feast(arg[0], arg[1], arg[2])
        assert response == output
