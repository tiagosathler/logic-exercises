#!/bin/python3

# import os
# import random
# import re
# import sys

from typing import List

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#


class Cardinal:
    def __init__(self, s: List[List[int]]):
        self.__nw: int
        self.__n: int
        self.__ne: int

        self.__w: int
        self.__c: int
        self.__e: int

        self.__sw: int
        self.__s: int
        self.__se: int

        self.__cost: int
        self.__mean: int

        self.__calculate_means(s)
        self.__matrix_to_cardinal(s)

        self.__max = self.__c * 3
        self.__parity = self.__c % 2
        self.calculate_it = True

    def __calculate_means(self, s: List[List[int]]) -> None:
        vector = list()

        for r in range(3):
            for c in range(3):
                vector.append(s[r][c])

        self.__mean = sum(vector) // len(vector)

    def __matrix_to_cardinal(self, s: List[List[int]]) -> None:
        self.__nw = s[0][0]
        self.__n = s[0][1]
        self.__ne = s[0][2]

        self.__w = s[1][0]
        self.__c = self.__mean
        self.__e = s[1][2]

        self.__sw = s[2][0]
        self.__s = s[2][1]
        self.__se = s[2][2]

    def is_square_magic(self) -> bool:
        matrix = self.cardinal_to_matrix()
        normal_diagonal = 0
        inverted_diagonal = 0

        for r in range(3):
            row = sum(matrix[r])
            column = 0
            for c in range(3):
                column += matrix[c][r]
                if c == r:
                    normal_diagonal += matrix[r][c]
                if 3 - 1 - r == c:
                    inverted_diagonal += matrix[r][3 - 1 - r]
            if row != self.__max or column != self.__max:
                return False

        if normal_diagonal != self.__max or inverted_diagonal != self.__max:
            return False
        return True

    def check_points(self) -> None:
        matrix = self.cardinal_to_matrix()
        self.calculate_it = False
        for r in range(3):
            for c in range(3):
                if matrix[r][c] <= 0:
                    self.__mean += 1
                    self.__matrix_to_cardinal(matrix)
                    self.__max = self.__c * 3
                    self.__parity = self.__c % 2
                    self.calculate_it = True
                    return None

    def calculate_cost(self, s: List[List[int]]) -> int:
        self.__cost = 0
        matrix = self.cardinal_to_matrix()
        for i in range(3):
            for j in range(3):
                self.__cost += abs(s[i][j] - matrix[i][j])
        return self.__cost

    def cardinal_to_matrix(self) -> List[List[int]]:
        return [
            [self.__nw, self.__n, self.__ne],
            [self.__w, self.__c, self.__e],
            [self.__sw, self.__s, self.__se],
        ]

    def diagonal_analysis(self, normal: bool) -> None:
        if normal:
            result = self.__corner_analysis(self.__nw, self.__se)
            self.__nw = result[0]
            self.__se = result[1]
        else:
            result = self.__corner_analysis(self.__ne, self.__sw)
            self.__ne = result[0]
            self.__sw = result[1]

    def __corner_analysis(self, top: int, bottom: int) -> List[int]:
        if top % 2 == self.__parity:
            if bottom % 2 == self.__parity:
                diagonal = top + self.__c + bottom
                while diagonal != self.__max:
                    if diagonal < self.__max:
                        top += 1
                        bottom += 1
                    # elif top >= 3 and bottom >= 3:
                    else:
                        top -= 1
                        bottom -= 1

                    diagonal = top + self.__c + bottom
            else:
                diagonal = top + self.__c + bottom
                while diagonal != self.__max:
                    if diagonal < self.__max:
                        top += 1
                    elif top >= 3:
                        top -= 1
                    # elif bottom >= 4:
                    else:
                        bottom -= 2

                    diagonal = top + self.__c + bottom

        elif bottom % 2 == self.__parity:
            diagonal = top + self.__c + bottom
            while diagonal != self.__max:
                if diagonal < self.__max:
                    bottom += 1
                elif bottom >= 3:
                    bottom -= 1
                # elif top >= 4:
                else:
                    top -= 2

                diagonal = top + self.__c + bottom
        return [top, bottom]

    def edge_analysis(self, middle: str) -> None:
        if middle.lower() == "n":
            self.__n = self.__middle_analysis(self.__nw, self.__n, self.__ne)
        elif middle.lower() == "s":
            self.__s = self.__middle_analysis(self.__sw, self.__s, self.__se)
        elif middle.lower() == "w":
            self.__w = self.__middle_analysis(self.__nw, self.__w, self.__sw)
        else:
            self.__e = self.__middle_analysis(self.__ne, self.__e, self.__se)

    def __middle_analysis(self, first: int, middle: int, last: int) -> int:
        summation = first + middle + last
        while summation != self.__max:
            if summation < self.__max:
                middle += 1
            else:
                middle -= 1
            summation = first + middle + last
        return middle


def formingMagicSquare(s: List[List[int]]) -> int:
    """
    https://www.hackerrank.com/challenges/magic-square-forming
    """
    print(s)
    cardinal = Cardinal(s)

    while cardinal.calculate_it:
        # analyzing the diagonals
        cardinal.diagonal_analysis(True)  # normal diagonal
        cardinal.diagonal_analysis(False)  # inverted diagonal

        # analyzing the middle of the edges
        cardinal.edge_analysis("n")
        cardinal.edge_analysis("s")
        cardinal.edge_analysis("w")
        cardinal.edge_analysis("e")

        print(cardinal.cardinal_to_matrix())

        cardinal.check_points()

    cost = cardinal.calculate_cost(s)
    print(cardinal.is_square_magic())

    return cost


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")
    # s = []

    cases = [
        {
            "id": 1,
            "expected": 14,
            "s": [
                [4, 5, 8],
                [2, 4, 1],
                [1, 9, 7],
            ],
        },
        {
            "id": 2,
            "expected": 21,
            "s": [
                [2, 9, 8],
                [4, 2, 7],
                [5, 6, 7],
            ],
        },
        {
            "id": 3,
            "expected": 20,
            "s": [
                [4, 4, 7],
                [3, 1, 5],
                [1, 7, 9],
            ],
        },
        {
            "id": 4,
            "expected": 16,
            "s": [
                [2, 2, 7],
                [8, 6, 4],
                [1, 2, 9],
            ],
        },
        {
            "id": 5,
            "expected": 18,
            "s": [
                [7, 6, 5],
                [7, 2, 8],
                [5, 3, 4],
            ],
        },
        {
            "id": 6,
            "expected": 17,
            "s": [
                [6, 7, 8],
                [7, 6, 2],
                [3, 2, 3],
            ],
        },
        {
            "id": 7,
            "expected": 18,
            "s": [
                [6, 1, 2],
                [7, 2, 6],
                [5, 6, 2],
            ],
        },
        {
            "id": 8,
            "expected": 21,
            "s": [
                [4, 6, 6],
                [2, 4, 1],
                [8, 9, 8],
            ],
        },
        {
            "id": 9,
            "expected": 19,
            "s": [
                [7, 2, 9],
                [6, 6, 2],
                [5, 1, 2],
            ],
        },
        {
            "id": 10,
            "expected": 21,
            "s": [
                [4, 1, 5],
                [7, 6, 4],
                [7, 2, 2],
            ],
        },
    ]
    # for _ in range(3):
    #     s.append(list(map(int, input().rstrip().__split())))

    for case in cases:
        print("--------")
        print("case: ", case["id"])
        cost = formingMagicSquare(case["s"])
        print(
            "calculated cost: ", cost, "; expected cost: ", case["expected"]
        )
        print("Passed? ", cost == case["expected"])

    # fptr.__write(str(result) + "\n")

    # fptr.close()
