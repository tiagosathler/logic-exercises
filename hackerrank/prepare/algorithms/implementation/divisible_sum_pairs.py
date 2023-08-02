"""HackerRank
Divisible Sum Pairs
 https://www.hackerrank.com/challenges/divisible-sum-pairs/
 """

import math

# import os
# import random
# import re
# import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#


def divisible_sum_pairs(
    _len_array: int, divisor: int, array: list[int]
) -> int:
    """Divisible Sum Pairs of array

    Args:
        len_array (int):  the length of array
        divisor (int): an array of integers
        array (list[int]): the integer divisor

    Returns:
        int: the number of pairs
    """
    # num_of_pairs = 0
    # for i in range(_len_array - 1):
    #     for j in range(i + 1, _len_array):
    #         if (array[i] + array[j]) % divisor == 0:
    #             num_of_pairs += 1
    # return num_of_pairs

    remainders_frequency = [0] * divisor

    for number in array:
        remainders_frequency[number % divisor] += 1

    number_of_pairs = math.comb(remainders_frequency[0], 2)

    for remainder in range(1, divisor // 2 + 1):
        if remainder != divisor / 2:
            number_of_pairs += (
                remainders_frequency[remainder]
                * remainders_frequency[divisor - remainder]
            )
        else:
            number_of_pairs += math.comb(remainders_frequency[remainder], 2)

    return number_of_pairs


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # k = int(first_multiple_input[1])

    # ar = list(map(int, input().rstrip().split()))

    arrays = [
        [1, 3, 2, 6, 1, 2],
        [1, 2, 3, 4, 5, 6],
        [5, 9, 10, 7, 4],
        [29, 97, 52, 86, 27, 89, 77, 19, 99, 96],
        [
            43,
            95,
            51,
            55,
            40,
            86,
            65,
            81,
            51,
            20,
            47,
            50,
            65,
            53,
            23,
            78,
            75,
            75,
            47,
            73,
            25,
            27,
            14,
            8,
            26,
            58,
            95,
            28,
            3,
            23,
            48,
            69,
            26,
            3,
            73,
            52,
            34,
            7,
            40,
            33,
            56,
            98,
            71,
            29,
            70,
            71,
            28,
            12,
            18,
            49,
            19,
            25,
            2,
            18,
            15,
            41,
            51,
            42,
            46,
            19,
            98,
            56,
            54,
            98,
            72,
            25,
            16,
            49,
            34,
            99,
            48,
            93,
            64,
            44,
            50,
            91,
            44,
            17,
            63,
            27,
            3,
            65,
            75,
            19,
            68,
            30,
            43,
            37,
            72,
            54,
            82,
            92,
            37,
            52,
            72,
            62,
            3,
            88,
            82,
            71,
        ],
        [
            50,
            44,
            77,
            66,
            70,
            58,
            9,
            59,
            74,
            82,
            87,
            15,
            10,
            95,
            10,
            81,
            2,
            4,
            87,
            85,
            28,
            96,
            76,
            18,
            86,
            91,
            94,
            59,
            19,
            58,
            98,
            48,
            38,
            70,
            36,
            38,
            66,
            9,
            72,
            54,
            23,
            23,
            17,
            18,
            8,
            16,
            9,
            56,
            12,
            59,
            73,
            31,
            10,
            62,
            83,
            84,
            28,
            91,
            29,
            22,
            73,
            22,
            3,
            75,
            26,
            31,
            93,
            57,
            15,
            32,
            46,
            74,
            99,
            10,
            15,
            58,
            60,
            53,
            41,
            49,
            71,
            59,
            4,
            20,
            38,
            78,
            1,
            94,
            76,
            5,
            70,
            68,
            42,
            34,
            77,
            28,
            19,
            25,
            20,
            15,
        ],
    ]

    divisors = [
        3,
        5,
        2,
        3,
        22,
        66,
    ]

    expected_values = [
        5,
        3,
        4,
        15,
        216,
        69,
    ]

    for array, divisor, expected in zip(arrays, divisors, expected_values):
        response = divisible_sum_pairs(len(array), divisor, array)
        print(expected, response)
        if response != expected:
            response = divisible_sum_pairs(len(array), divisor, array)
        assert response == expected

    # fptr.write(str(result) + "\n")

    # fptr.close()
