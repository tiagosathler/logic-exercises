#!/bin/python3

import math

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

        self.__matrix_to_cardinal(s)

        self.__max = self.__c * 3
        self.__parity = self.__c % 2
        # self.calculate = True

    def restart(self, s: List[List[int]]) -> None:
        self.__matrix_to_cardinal(s)
        self.__max = self.__c * 3
        self.__parity = self.__c % 2

    def calculate_cost(self, s: List[List[int]]) -> int:
        self.__cost = 0
        matrix = self.cardinal_to_matrix()
        print(matrix)
        for i in range(3):
            for j in range(3):
                self.__cost += abs(s[i][j] - matrix[i][j])
        return self.__cost

    def increase_center(self) -> None:
        # matrix = selcardinal_to_matrix()
        # for i in range(3):
        #     for j in range(3):
        #         matrix[i][j] += 1
        self.__c += 1
        self.__max = self.__c * 3
        self.__parity = self.__c % 2

    def decrease_center(self) -> None:
        # matrix = selcardinal_to_matrix()
        # for i in range(3):
        #     for j in range(3):
        #         matrix[i][j] += 1
        self.__c -= 1
        self.__max = self.__c * 3
        self.__parity = self.__c % 2

    def try_increase_points(self, s: List[List[int]]) -> int:
        new_cost = 0
        matrix = self.cardinal_to_matrix()
        for i in range(3):
            for j in range(3):
                matrix[i][j] += 1
                new_cost += abs(s[i][j] - matrix[i][j])
        return new_cost

    def try_decrease_points(self, s: List[List[int]]) -> int:
        new_cost = 0
        matrix = self.cardinal_to_matrix()
        for i in range(3):
            for j in range(3):
                matrix[i][j] -= 1
                new_cost += abs(s[i][j] - matrix[i][j])
        return new_cost

    def __matrix_to_cardinal(self, s: List[List[int]]) -> None:
        self.__nw = s[0][0]
        self.__n = s[0][1]
        self.__ne = s[0][2]

        self.__w = s[1][0]
        self.__c = s[1][1]
        self.__e = s[1][2]

        self.__sw = s[2][0]
        self.__s = s[2][1]
        self.__se = s[2][2]

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
    cardinal = Cardinal(s)

    # # analyzing the diagonals
    # cardinal.diagonal_analysis(True)  # normal diagonal
    # cardinal.diagonal_analysis(False)  # inverted diagonal

    # # analyzing the middle of the edges
    # cardinal.edge_analysis("n")
    # cardinal.edge_analysis("s")
    # cardinal.edge_analysis("w")
    # cardinal.edge_analysis("e")

    # cost = cardinal.calculate_cost(s)
    # current_cost = cardinal.try_increase_points(s)
    current_cost = -math.inf
    cost = 0
    print(s)

    while current_cost < cost:
        # analyzing the diagonals

        cardinal.diagonal_analysis(True)  # normal diagonal

        cardinal.diagonal_analysis(False)  # inverted diagonal

        # analyzing the middle of the edges
        cardinal.edge_analysis("n")
        cardinal.edge_analysis("s")
        cardinal.edge_analysis("w")
        cardinal.edge_analysis("e")

        cost = cardinal.calculate_cost(s)

        # trying increase points
        cost_for_increased_points = cardinal.try_increase_points(s)
        cost_for_decreased_points = cardinal.try_decrease_points(s)

        if (
            cost_for_increased_points < cost
            and cost_for_increased_points < cost_for_decreased_points
        ):
            cardinal.increase_center()
            current_cost = cost_for_increased_points
        elif cost_for_decreased_points < cost:
            cardinal.decrease_center()
        else:
            current_cost = cost

        # s_result = cdinal.cardinal_to_matrix()

        # print(s_result)
        # print(cardinal.cost)

    return cost


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")
    # s = []

    # case 2 - problem
    # s = [
    #     [2, 9, 8],
    #     [4, 2, 7],
    #     [5, 6, 7],
    # ]
    # cost == 21 != 22

    # case 3 - ok
    # s = [
    #     [4, 4, 7],
    #     [3, 1, 5],
    #     [1, 7, 9],
    # ]
    # cost == 20

    # case 4 -
    s = [
        [2, 2, 7],
        [8, 6, 4],
        [1, 2, 9],
    ]
    # cost == 16

    # for _ in range(3):
    #     s.append(list(map(int, input().rstrip().__split())))

    result = formingMagicSquare(s)
    print(result)

    # fptr.__write(str(result) + "\n")

    # fptr.close()


# def corner_analyses(
#     s: List[List[int]],
#     parity: int,
#     center: int,
#     corner: List[List[int]],
# ) -> List:

#     max = 3 * center
#     top_x = corner[0][0]
#     top_y = corner[0][1]

#     bottom_x = corner[1][0]
#     bottom_y = corner[1][1]

#     cost = 0

#     if s[top_x][top_y] % 2 != parity:
#         if s[bottom_x][bottom_y] % 2 != parity:
#             while s[top_x][top_y] + center + s[bottom_x][bottom_y] != max:
#                 sum = s[top_x][top_y] + center + s[bottom_x][bottom_y]
#                 if sum < max:
#                     s[top_x][top_y] += 1
#                     s[bottom_x][bottom_y] += 1
#                     cost += 2
#                 elif s[top_x][top_y] >= 3 and s[bottom_x][bottom_y] >= 3:
#                     s[top_x][top_y] -= 1
#                     s[bottom_x][bottom_y] -= 1
#                     cost += 2
#                 else:
#                     print("error 1")
#                     break
#         else:
#             while s[top_x][top_y] + center + s[bottom_x][bottom_y] != max:
#                 sum = s[top_x][top_y] + center + s[bottom_x][bottom_y]
#                 if sum < max:
#                     s[top_x][top_y] += 1
#                     cost += 1
#                 elif s[top_x][top_y] >= 3:
#                     s[top_x][top_y] -= 1
#                     cost += 1
#                 elif s[bottom_x][bottom_y] >= 4:
#                     s[bottom_x][bottom_y] -= 2
#                     cost += 2
#                 else:
#                     print("error 2")
#                     break
#     elif s[bottom_x][bottom_y] % 2 != parity:
#         while s[top_x][top_y] + center + s[bottom_x][bottom_y] != max:
#             sum = s[top_x][top_y] + center + s[bottom_x][bottom_y]
#             if sum < max:
#                 s[bottom_x][bottom_y] += 1
#             elif s[bottom_x][bottom_y] >= 3:
#                 s[bottom_x][bottom_y] -= 1
#             elif s[top_x][top_y] >= 4:
#                 s[bottom_x][bottom_y] -= 2
#             else:
#                 print("error 3")
#                 break
#     return [cost, s]


# def mid_edge_analyses(
#     s: List[List[int]],
#     center: int,
# ) -> List:

#     max = 3 * center
#     a_x = corner[0][0]
#     a_y = corner[0][1]

#     b_x = corner[1][0]
#     b_y = corner[1][1]

#     cost = 0

#     while (s[a_x][a_y] + center + s[b_x][b_y] != max):
#         sum = s[a_x][a_y] + center + s[b_x][b_y]
#         if (sum < max):


# if s[0][0] % 2 != 0:
#     if s[2][2] % 2 != 0:
#         while s[0][0] + center + s[2][2] != max:
#             sum = s[0][0] + center + s[2][2]
#             if sum < max:
#                 s[0][0] += 1
#                 s[2][2] += 1
#                 cost += 2
#             elif s[0][0] >= 3 and s[2][2] >= 3:
#                 s[0][0] -= 1
#                 s[2][2] -= 1
#                 cost += 2
#             else:
#                 print("error 1")
#                 break
#     else:
#         while s[0][0] + center + s[2][2] != max:
#             sum = s[0][0] + center + s[2][2]
#             if sum < max:
#                 s[0][0] += 1
#                 cost += 1
#             elif s[0][0] >= 3:
#                 s[0][0] -= 1
#                 cost += 1
#             elif s[2][2] >= 4:
#                 s[2][2] -= 2
#                 cost += 2
#             else:
#                 print("error 2")
#                 break
# elif s[2][2] % 2 != 0:
#     while s[0][0] + center + s[2][2] != max:
#         sum = s[0][0] + center + s[2][2]
#         if sum < max:
#             s[2][2] += 1
#         elif s[2][2] >= 3:
#             s[2][2] -= 1
#         elif s[0][0] >= 4:
#             s[2][2] -= 2
#         else:
#             print("error 3")
#             break

# length = len(s[0])
# sum_normal = 0
# sum_invert = 0

# sums = [list() for _ in range(length)]

# for r in range(length):
#     sum_row = sum(s[r])
#     sum_column = 0
#     for c in range(length):
#         sum_column += s[c][r]
#         if c == r:
#             sum_normal += s[r][c]
#         if length - 1 - r == c:
#             sum_invert += s[r][length - 1 - r]
#     print(sum_row, sum_column)
#     sums[r].append((sum_row, sum_column))

#     if sum_row > max:
#         max = sum_row
#     if sum_column > max:
#         max = sum_column

# if sum_normal > max:
#     max = sum_normal
# if sum_invert > max:
#     max = sum_invert

# print('(row, column)',  sums)
# print('sum_normal: ', sum_normal, 'sum_invert: ', sum_invert)

# [
#     [5, 3, 4],
#     [1, 5, 8],
#     [6, 4, 2],

# ]
#   [(12, 12), (14, 12), (12, 14)]
#  sum_normal:  12 sum_invert:  15

#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2],

# return max
