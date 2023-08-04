"""HackerRank
Sales by Match / Sock Merchant
https://www.hackerrank.com/challenges/sock-merchant/
"""

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sock_merchant(_number: int, colors: list[int]) -> int:
    """Sock Merchant

    Args:
        _number (int): the number of socks in the pile
        (not used in the function)
        colors (list[int]): the colors of each sock

    Returns:
        int: the number of pairs
    """

    colors_count = dict.fromkeys(colors, 0)

    for color in colors:
        colors_count[color] += 1

    pairs = 0

    for count in colors_count.values():
        pairs += count // 2

    return pairs


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    # n = int(input().strip())

    # ar = list(map(int, input().rstrip().split()))

    # result = sockMerchant(n, ar)

    # fptr.write(str(result) + "\n")

    # fptr.close()
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    n = len(ar)
    response = sock_merchant(n, ar)
    print(response)
    assert response == 3
