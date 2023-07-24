"""HackerRank
Circular Array Rotation
https://www.hackerrank.com/challenges/circular-array-rotation
"""

from collections import deque


#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#


def circular_array_rotation(
    array: list[int], rotations: int, queries: list[int]
) -> list[int]:
    """Circular Array Rotation
    Print the elements in an array after 'k'
    right circular rotation operations.

    Args:
        array (list[int]): the array to rotate
        rotations (int): the rotation count
        queries (list[int]): the indices to report

    Returns:
        list[int]:  the values in the rotated array as requested in queries
    """
    queue = deque(array)

    queue.rotate(rotations)

    return [queue[query] for query in queries]


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # k = int(first_multiple_input[1])

    # q = int(first_multiple_input[2])

    # a = list(map(int, input().rstrip().split()))

    # queries = []

    # for _ in range(q):
    #     queries_item = int(input().strip())
    #     queries.append(queries_item)

    # result = circularArrayRotation(a, k, queries)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()

    print(circular_array_rotation([1, 2, 3], 2, [0, 1, 2]))
