"""HackerRank
Picking Numbers
https://www.hackerrank.com/challenges/picking-numbers

Given an array of integers, find the longest sub_array
where the absolute difference between any two elements
is less than or equal to 1.
"""


def picking_numbers(array: list[int]) -> int:
    """Picking Numbers from a list of numbers
    Find the longest sub array where the absolute
    difference between any two elements is less than or equal to 1

    Args:
        array (list[int]): array of integers

    Returns:
        int: length of the longest sub array
    """
    # arrays: list[list[int]] = []

    # for i in range(len(array) - 1):
    #     sub_array = [array[i]]

    #     for j, number in enumerate(array):
    #         if (
    #             i != j
    #             and abs(max(sub_array) - number) <= 1
    #             and abs(min(sub_array) - number) <= 1
    #         ):
    #             sub_array.append(number)

    #     arrays.append(sub_array)

    # arrays_length = [len(sub_array) for sub_array in arrays]

    # return max(arrays_length)

    max_length = 0
    number_counts = {}

    for number in array:
        number_counts[number] = number_counts.get(number, 0) + 1

    for number, count in number_counts.items():
        max_length = max(max_length, count + number_counts.get(number + 1, 0))

    return max_length


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # a = list(map(int, input().rstrip().split()))

    # result = pickingNumbers(a)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    a = [4, 6, 5, 3, 3, 1]
    result = picking_numbers(a)
    print(result)
    assert result == 3

    a = [1, 2, 2, 3, 1, 2]
    result = picking_numbers(a)
    print(result)
    assert result == 5

    a = [
        7,
        12,
        13,
        19,
        17,
        7,
        3,
        18,
        9,
        18,
        13,
        12,
        3,
        13,
        7,
        9,
        18,
        9,
        18,
        9,
        13,
        18,
        13,
        13,
        18,
        18,
        17,
        17,
        13,
        3,
        12,
        13,
        19,
        17,
        19,
        12,
        18,
        13,
        7,
        3,
        3,
        12,
        7,
        13,
        7,
        3,
        17,
        9,
        13,
        13,
        13,
        12,
        18,
        18,
        9,
        7,
        19,
        17,
        13,
        18,
        19,
        9,
        18,
        18,
        18,
        19,
        17,
        7,
        12,
        3,
        13,
        19,
        12,
        3,
        9,
        17,
        13,
        19,
        12,
        18,
        13,
        18,
        18,
        18,
        17,
        13,
        3,
        18,
        19,
        7,
        12,
        9,
        18,
        3,
        13,
        13,
        9,
        7,
    ]
    result = picking_numbers(a)
    print(result)
    assert result == 30
