"""HackerRank
Sequence Equation
https://www.hackerrank.com/challenges/permutation-equation
"""

# import math
# import os
# import random
# import re
# import sys


#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutation_equation(array: list[int]) -> list[int]:
    """Permutation equation

    Args:
        array (list[int]): an array of integers

    Returns:
        list[int]: the values of y for all x in the arithmetic sequence 1 to n
    """
    # result: list[int] = []
    dictionary = {value: index + 1 for index, value in enumerate(array)}

    # for root in range(1, len(array) + 1):
    #     # pointer = array.index(root) + 1
    #     # result.append(array.index(pointer) + 1)
    #     result.append(dictionary[dictionary[root]])

    # return result
    return [dictionary[dictionary[root]] for root in range(1, len(array) + 1)]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # p = list(map(int, input().rstrip().split()))

    # result = permutationEquation(p)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
    print(permutation_equation([5, 2, 1, 3, 4]))
