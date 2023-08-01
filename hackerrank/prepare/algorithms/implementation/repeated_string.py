"""HackerRank
Utopian Tree
https://www.hackerrank.com/challenges/utopian-tree/
"""

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


def repeated_string(str_to_repeat: str, number: int) -> int:
    """Repeated string representation

    Args:
        str_to_repeat (str): a string to repeat
        number (int): the number of characters to consider

    Returns:
        int: the frequency of 'a' in the substring
    """
    # size_str = len(str_to_repeat)
    # frequency = [0] * size_str

    # for index, char in enumerate(str_to_repeat):
    #     if char == "a":
    #         frequency[index] += 1

    # quotient, remainder = divmod(number, size_str)
    # count = sum(frequency) * quotient

    # if remainder == 0:
    #     return count

    # for index in range(0, remainder):
    #     count += frequency[index]

    # return count

    size_str = len(str_to_repeat)
    total_a_count = str_to_repeat.count('a')

    quotient, remainder = divmod(number, size_str)
    count = total_a_count * quotient

    if remainder > 0:
        count += str_to_repeat[:remainder].count('a')

    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    # n = int(input().strip())

    # result = repeatedString(s, n)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    print(repeated_string("abcac", 10))
    print(repeated_string("aba", 10))
    print(repeated_string("a", 1_000_000_000_000))
    print(repeated_string("jdiacikk", 899491))
