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

    # Step 1: Determine if the given "operations" is sufficient
    # to perform the required operations.
    # If "operations" is greater than the total length of "initial" and
    # "desired" combined, we can delete all characters
    # and then append the remaining characters in "desired" to initial.
    if operations >= len(initial) + len(desired):
        return "Yes"

    # Step 2: Find the common prefix between "initial" and "desired"
    common_prefix_len = 0

    for i_char, d_char in zip(initial, desired):
        if i_char == d_char:
            common_prefix_len += 1
        else:
            break

    # Step 3: Calculate the remaining characters in "initial"
    # after the common prefix
    remaining_initial = len(initial) - common_prefix_len

    # Step 4: Calculate the remaining characters in "desired"
    # after the common prefix
    remaining_desired = len(desired) - common_prefix_len

    # If operations is greater than or equal to the total
    # number of remaining characters in "initial" and "desired" combined,
    # we can delete the remaining characters in "initial" and
    # append the remaining characters in "desired".
    remaining = remaining_initial + remaining_desired
    if operations >= remaining and (operations - remaining) % 2 == 0:
        return "Yes"

    # If operations is greater than the total length of "initial" and "desired"
    # combined minus twice the common prefix length,
    # then we can delete the common prefix characters
    # and append the remaining characters in "desired".
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
