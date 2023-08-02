"""HackerRank
Day of the Programmer
https://www.hackerrank.com/challenges/day-of-the-programmer
"""

# import math
# import os
import datetime

# import random
# import re
# import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#


def day_of_programmer(year: int) -> str:
    """Day of Programmer

    Args:
        year (int): an integer

    Returns:
        str: the full date of Day of the Programmer
        during year in the format dd.mm.yyyy
    """
    days = 255
    date = datetime.datetime(year, 1, 1)

    if year < 1919 and year % 4 == 0 and year % 400 != 0 and year % 100 == 0:
        days -= 1

    elif year == 1918:
        days += 13

    date = date + datetime.timedelta(days=days)

    return date.strftime("%d.%m.%Y")


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # year = int(input().strip())
    years = [
        1700,
        1800,
        1820,
        1916,
        1836,
        1872,
        1832,
        1880,
        1812,
        1820,
        1918,
    ]

    expected_values = [
        "12.09.1700",
        "12.09.1800",
        "12.09.1820",
        "12.09.1916",
        "12.09.1836",
        "12.09.1872",
        "12.09.1832",
        "12.09.1880",
        "12.09.1812",
        "12.09.1820",
        "26.09.1918",
    ]

    for year_value, expected in zip(years, expected_values):
        response = day_of_programmer(year_value)
        print(response)
        assert response == expected

    # fptr.write(result + '\n')

    # fptr.close()
