"""HackerRank
Subarray Division / The Birthday Bar
https://www.hackerrank.com/challenges/the-birthday-bar/
"""

# import math
# import random
# import re
# import sys
# import os

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#


def the_birthday_bar(numbers: list[int], day: int, month: int) -> int:
    """The birthday bar

    Args:
        numbers (list[int]): the numbers on each of the squares of chocolate
        day (int): Ron's birth day
        month (int): Ron's birth month

    Returns:
        int: the number of ways the bar can be divided
    """
    quantity_of_chocolate_squares = len(numbers)

    if quantity_of_chocolate_squares < month:
        return 0

    count = 0

    for index in range(quantity_of_chocolate_squares - month + 1):
        sub_numbers = numbers[index: index + month]

        if sum(sub_numbers) == day:
            count += 1

    return count


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # s = list(map(int, input().rstrip().split()))

    # first_multiple_input = input().rstrip().split()

    # d = int(first_multiple_input[0])

    # m = int(first_multiple_input[1])

    # result = birthday(s, d, m)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    array = [2, 2, 1, 3, 2]
    RESPONSE = the_birthday_bar(array, 4, 2)
    print(RESPONSE)
    assert RESPONSE == 2

    array = [1, 2, 1, 3, 2]
    RESPONSE = the_birthday_bar(array, 3, 2)
    print(RESPONSE)
    assert RESPONSE == 2

    array = [1, 1, 1, 1, 1, 1]
    RESPONSE = the_birthday_bar(array, 3, 2)
    print(RESPONSE)
    assert RESPONSE == 0

    array = [1, 2, 1, 3, 1]
    RESPONSE = the_birthday_bar(array, 4, 3)
    print(RESPONSE)
    assert RESPONSE == 1
