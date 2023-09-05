"""HackerRank
Halloween Sale
https://www.hackerrank.com/challenges/halloween-sale/
"""

# import math
# import os
# import random
# import re
# import sys


def halloween_sale(
    price: int, discount: int, minimum_price: int, available: int
) -> int:
    """Halloween Sale function

    Args:
    price (int): the price of the first game
    discount (int): the discount from the previous game price
    minimum_price (int): the minimum cost of a game
    available (int): the starting budget

    Returns:
    int: how many games can i buy
    """
    quantity = int(0)
    available_money = available
    actual_price = price

    while available_money >= actual_price:
        quantity += 1
        available_money -= actual_price
        actual_price = (
            actual_price - discount
            if actual_price - discount >= minimum_price
            else minimum_price
        )

    return quantity


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

    response = halloween_sale(20, 3, 6, 70)
    print(response)
    assert response == 5

    response = halloween_sale(20, 3, 6, 80)
    print(response)
    assert response == 6
