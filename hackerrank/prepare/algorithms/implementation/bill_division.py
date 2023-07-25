"""
Bill Division
https://www.hackerrank.com/challenges/bon-appetit/
"""

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#


def bon_appetit(bill: list[int], do_not_eat: int, money: int) -> None:
    """Bon Appetit function

    Args:
        bill (list[int]): an array of integers representing
        the cost of each item ordered;
        do_not_eat (int): an integer representing the zero-based
        index of the item Anna doesn't eat;
        money (int): the amount of money that Anna contributed to the bill.
    """
    total = (sum(bill) - bill[do_not_eat]) / 2
    diff = money - total

    if diff == 0:
        print("Bon Appetit")
    else:
        print(int(diff))


if __name__ == "__main__":
    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # k = int(first_multiple_input[1])

    # bill = list(map(int, input().rstrip().split()))

    # b = int(input().strip())

    bon_appetit([3, 10, 2, 9], 1, 12)
