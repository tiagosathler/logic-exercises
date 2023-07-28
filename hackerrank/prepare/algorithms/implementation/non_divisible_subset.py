"""HackerRank
Non-divisible subset
https://www.hackerrank.com/challenges/non-divisible-subset/
"""

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#


def non_divisible_subset(divisor: int, array: list[int]) -> int:
    """Non-divisible subset

    Args:
        divisor (int): the divisor
        array (list[int]): an array of integers

    Returns:
        int: the length of the longest subset of array meeting the criteria
    """

    # DISCLAIMER (1):
    #
    # The code commented below is a refactoring
    # I did of based on the code found in:
    # https://programs.programmingoneonone.com/2021/03/hackerRank-non-divisible-subset-solution.html

    # restos = [numero % divisor for numero in array]

    # freq_restos = dict.fromkeys(restos, 0)

    # for resto in restos:
    #     freq_restos[resto] += 1

    # total = 0

    # for resto, freq in freq_restos.items():
    #     if resto == 0:
    #         total += 1

    #     elif resto == divisor / 2:
    #         total += 1

    #     elif resto > divisor / 2:
    #         if divisor - resto in freq_restos:
    #             total += max([freq, freq_restos[divisor - resto]])
    #         else:
    #             total += freq

    #     elif resto < divisor / 2:
    #         if divisor - resto not in freq_restos:
    #             total += freq

    # return total

    # DISCLAIMER (2):
    # The following code is a refactoring
    # of the code commented above by AI ChatGPT-3.5
    freq_restos = [0] * divisor

    for num in array:
        freq_restos[num % divisor] += 1

    total = min(freq_restos[0], 1)

    for i in range(1, divisor // 2 + 1):
        if i != divisor / 2:
            total += max(freq_restos[i], freq_restos[divisor - i])
        else:
            total += min(freq_restos[i], 1)

    return total


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # k = int(first_multiple_input[1])

    # s = list(map(int, input().rstrip().split()))

    # result = nonDivisibleSubset(k, s)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    print(non_divisible_subset(3, [1, 7, 2, 4]))
    print(non_divisible_subset(4, [19, 10, 12, 10, 24, 25, 22]))

    print(non_divisible_subset(3, [1, 2, 3, 4, 5, 6, 7]))

    print(
        non_divisible_subset(
            7,
            [
                278,
                576,
                496,
                727,
                410,
                124,
                338,
                149,
                209,
                702,
                282,
                718,
                771,
                575,
                436,
            ],
        )
    )
