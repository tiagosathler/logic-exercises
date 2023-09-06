"""HackerRank
Find The Median - Mock test
"""


def find_the_median(array: list[int]) -> int:
    """Find the median

    Args:
        array (list[int]): an array of integers
    """
    array.sort()
    index = len(array) // 2
    return array[index]


if __name__ == "__main__":
    assert find_the_median([0, 1, 2, 4, 5, 7, 3]) == 3
    assert find_the_median([110, 10, 50, -7, 9, 11, 1, 15, 16]) == 11
