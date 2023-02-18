"""Weighted Uniform Strings
https://www.hackerrank.com/challenges/weighted-uniform-string/
"""

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

from typing import List, Set


def weighted_uniform_strings(arg: str, queries: List[int]) -> List[str]:
    """Verifica se os inteiros da 'queries' estão nos pesos das string 'arg'

    Args:
        arg (str): uma string qualquer
        queires (List[int]): um lista de inteiros positivos

    Returns:
        List[str]: 'YES' ou 'NO' para inteiro corresponde da 'queries'
    """
    offset_unicode = int(96)
    weighted_uniform_list: Set[int] = set()

    last = arg[0]
    count = int(0)

    for letter in arg.lower():
        if letter == last:
            count += 1

        else:
            last = letter
            count = int(1)

        weighted_uniform_list.add((ord(letter) - offset_unicode) * count)

    response = [
        "Yes"
        if code in weighted_uniform_list
        else "No"
        for code in queries
    ]

    return response


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    # result = camelcase(s)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    STRING = "abccddde"
    QUERIES = [1, 3, 12, 5, 9, 10]

    RESULT = weighted_uniform_strings(STRING, QUERIES)

    print(RESULT)

    STRING = "aaabbbbcccddd"
    QUERIES = [9, 7, 8, 12, 5]

    RESULT = weighted_uniform_strings(STRING, QUERIES)

    print(RESULT)
