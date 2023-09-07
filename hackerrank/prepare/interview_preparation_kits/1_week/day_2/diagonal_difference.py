"""HackerRank
Diagonal Difference
https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference
"""


def diagonal_difference(matrix: list[list[int]]) -> int:
    """Diagonal Difference

    Args:
        matrix (list[list[int]]): an matrix of integers

    Returns:
        int: the absolute diagonal difference
    """
    size = len(matrix)
    sum_of_the_main_diagonal = int(0)
    sum_of_the_secondary_diagonal = int(0)

    for i in range(size):
        for j in range(size):
            if i == j:
                sum_of_the_main_diagonal += matrix[i][j]
            if i == size - 1 - j:
                sum_of_the_secondary_diagonal += matrix[i][j]

    return abs(sum_of_the_main_diagonal - sum_of_the_secondary_diagonal)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # arr = []

    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))

    # fptr.write(str(result) + '\n')

    # fptr.close()
    MATRIX = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]

    assert diagonal_difference(MATRIX) == 2
