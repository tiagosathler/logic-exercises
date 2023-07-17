"""HackerRank
Designer PDF Viewer
https://www.hackerrank.com/challenges/designer-pdf-viewer/
"""

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#


def designer_pdf_viewer(heights: list[int], word: str) -> int:
    offset = ord("a")
    max_height = 0
    word = word.lower()

    for letter in word:
        if heights[ord(letter) - offset] > max_height:
            max_height = heights[ord(letter) - offset]

    return max_height * len(word)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # h = list(map(int, input().rstrip().split()))

    # word = input()

    heights_values = [
        1,
        3,
        1,
        3,
        1,
        4,
        1,
        3,
        2,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        7,
    ]

    word_value = str("zaba")

    result = designer_pdf_viewer(heights_values, word_value)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
