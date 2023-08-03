"""HackerRank
Drawing Book
https://www.hackerrank.com/challenges/drawing-book
"""

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#


def page_count(number_of_pages: int, page: int) -> int:
    """Drawing Book

    Args:
        number_of_pages (int):  the number of pages in the book
        page (int): the page number to turn to

    Returns:
        int: the minimum number of pages to turn
    """
    if page <= number_of_pages // 2:
        return page // 2
    else:
        return number_of_pages // 2 - page // 2


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    # n = int(input().strip())

    # p = int(input().strip())

    # result = pageCount(n, p)

    # fptr.write(str(result) + "\n")
    response = page_count(5, 3)
    print(response)
    assert response == 1

    # fptr.close()
