"""HackerRank in a String
https://www.hackerrank.com/challenges/hackerrank-in-a-string/
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


def hackerrank_in_string(arg: str) -> str:
    """Verifica se a string 'arg' contém a palavra 'hackerrank' sequencialmente

    Args:
        arg (str): uma string qualquer

    Returns:
        str: 'YES' or 'NO'
    """
    word = list("hackerrank")

    for letter in arg.lower():
        if len(word) > 0 and letter == word[0]:
            word.pop(0)

    if len(word) == 0:
        return "YES"

    return "NO"


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    # result = camelcase(s)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    STRING = "hereiamstackerrank"

    RESULT = hackerrank_in_string(STRING)

    print(RESULT)

    STRING = "hackerworld"

    RESULT = hackerrank_in_string(STRING)

    print(RESULT)
