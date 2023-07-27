"""HackerRank
Append and Delete
https://www.hackerrank.com/challenges/append-and-delete
"""


# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING initial
#  2. STRING desired
#  3. INTEGER operations
#


def append_and_delete(initial: str, desired: str, operations: int) -> str:
    """Append and delete

    Args:
        initial (str): the initial string
        desired (str): the desired string
        operations (int): the exact number of operations to be performed

    Returns:
        str: either “Yes” or “No”
    """

    if operations >= len(initial) + len(desired):
        return "Yes"

    common_prefix_len = 0

    for i_char, d_char in zip(initial, desired):
        if i_char == d_char:
            common_prefix_len += 1
        else:
            break

    moves = len(initial) + len(desired) - 2 * common_prefix_len

    if operations >= moves and (operations - moves) % 2 == 0:
        return "Yes"

    return "No"


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    # t = input()

    # k = int(input().strip())

    # result = appendAndDelete(s, t, k)

    # fptr.write(result + '\n')

    # fptr.close()
    print(append_and_delete("hackerhappy", "hackerrank", 9))  # Output: "Yes"
    print(append_and_delete("aba", "aba", 7))  # Output: "Yes"
    print(append_and_delete("ashley", "ash", 2))  # Output: "No"
    print(append_and_delete("y", "yu", 2))  # Output: "No"
    print(append_and_delete("abcd", "abcdert", 10))  # Output: "No"
