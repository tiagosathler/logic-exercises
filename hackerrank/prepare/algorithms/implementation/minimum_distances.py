"""HackerRank
Minimum Distances
https://www.hackerrank.com/challenges/minimum-distances/
"""


def minimum_distances(array: list[int]) -> int:
    """Minimum distances between two array values.

    Args:
        array (list[int]): an array of integers

    Returns:
        int: the minimum distance found or -1 if there are no matching elements
    """
    minimum_distance = len(array)

    index_of_value: dict[int, int] = {}

    for index, value in enumerate(array):
        if value in index_of_value:
            previous_index = index_of_value[value]
            minimum_distance = min(minimum_distance, index - previous_index)
        index_of_value[value] = index

    return minimum_distance if minimum_distance != len(array) else -1


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # a = list(map(int, input().rstrip().split()))

    # result = minimumDistances(a)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    response = minimum_distances([7, 1, 3, 4, 1, 7])
    print(response)
    assert response == 3

    response = minimum_distances([3, 2, 1, 2, 3])
    print(response)
    assert response == 2
