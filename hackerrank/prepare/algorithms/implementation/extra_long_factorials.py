"""HackerRank
Extra Long Factorials
https://www.hackerrank.com/challenges/extra-long-factorials
"""

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#


def extra_long_factorials(number: int) -> None:
    if number <= 1:
        print(1)
        return None

    factorial = 1

    for multiplier in range(1, number+1):
        factorial *= multiplier

    print(factorial)
    return None


if __name__ == "__main__":
    # n = int(input().strip())

    extra_long_factorials(30)
