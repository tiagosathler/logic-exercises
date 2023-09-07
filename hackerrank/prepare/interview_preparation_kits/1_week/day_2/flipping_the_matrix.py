"""HackerRank
Flipping The Matrix - Mock test
"""


def flipping_the_matrix(matrix: list[list[int]]) -> int:
    """Flipping The Matrix
    Args:
        matrix (list[int]): an matrix of integers
    """
    half_size = len(matrix) // 2

    sub_matrix = [[0 for _ in range(half_size)] for _ in range(half_size)]

    for i in range(half_size):
        for j in range(half_size):
            sub_matrix[i][j] = max(
                matrix[i][j],
                matrix[2 * half_size - i - 1][j],
                matrix[i][2 * half_size - j - 1],
                matrix[2 * half_size - i - 1][2 * half_size - j - 1],
            )

    max_sum = sum(sum(row) for row in sub_matrix)

    return max_sum


if __name__ == "__main__":
    Q = 1
    N = 2
    matrix_1 = [
        [112, 42, 83, 119],
        [56, 125, 56, 49],
        [15, 78, 101, 43],
        [62, 98, 114, 108],
    ]

    response = flipping_the_matrix(matrix_1)
    print(response)
    assert response == 414

    matrix_2 = [
        [112, 110, 91, 99, 100, 119],
        [56, 87, 109, 96, 56, 49],
        [58, 63, 86, 112, 104, 98],
        [99, 63, 87, 98, 105, 111],
        [15, 78, 101, 87, 101, 106],
        [62, 98, 100, 79, 108, 114]
    ]

    response = flipping_the_matrix(matrix_2)
    print(response)
    assert response == 973
