"""HackerRank
Find Digits
https://www.hackerrank.com/challenges/find-digits/
"""

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def find_digits(number: int) -> int:
    """Find Digits

    Args:
        number (int): the value to analyze

    Returns:
        int: the number of digits in number that are divisors of number
    """
    # count = 0
    # for digit in str(number):
    #     digit = int(digit)
    #     if digit != 0 and number % digit == 0:
    #         count += 1

    # return count
    count = sum(
        1
        for digit in str(number)
        if int(digit) != 0 and number % int(digit) == 0
    )
    return count


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input().strip())

    # for t_itr in range(t):
    #     n = int(input().strip())

    #     result = findDigits(n)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
    print(find_digits(1012))
