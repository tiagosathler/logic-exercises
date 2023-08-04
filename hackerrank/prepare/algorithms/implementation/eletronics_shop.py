"""HackerRank
Electronics Shop
https://www.hackerrank.com/challenges/electronics-shop/
"""

# import os
# import math
# import sys


def get_money_spent(
    keyboards: list[int], drives: list[int], budget: int
) -> int:
    """Get Money Spent

    Args:
        keyboards (list[int]): the keyboard prices
        drives (list[int]): the drive prices
        budget (int): the budget

    Returns:
        int: the maximum that can be spent, or -1
        if it is not possible to buy both items
    """
    max_spent = -1

    for keyboard in keyboards:
        for drive in drives:
            total_spent = keyboard + drive
            if max_spent < total_spent <= budget:
                max_spent = total_spent

    return max_spent


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    # bnm = input().split()

    # b = int(bnm[0])

    # n = int(bnm[1])

    # m = int(bnm[2])

    # keyboards = list(map(int, input().rstrip().split()))

    # drives = list(map(int, input().rstrip().split()))

    # moneySpent = getMoneySpent(keyboards, drives, b)

    # fptr.write(str(moneySpent) + "\n")

    # fptr.close()
    k_arr = [3, 1]
    d_arr = [5, 2, 8]
    RESPONSE = get_money_spent(k_arr, d_arr, 10)
    print(RESPONSE)
    assert RESPONSE == 9
