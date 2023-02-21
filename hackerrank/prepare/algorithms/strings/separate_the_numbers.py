"""Separate the Numbers
https://www.hackerrank.com/challenges/separate-the-numbers/
"""

# from typing import List, Tuple
# import math


# def get_zeros(all_zeros_positions: List[int]) -> List[Tuple[int, int]]:
#     """Finds the first occurrences of greater repetitions of zeros
#     among the positions of the zeros found.
#     The result is a list of tuples, where the first pair the tuple indicates
#     the zero position and the second the number of zeros

#     Args:
#         all_zeros_positions (List[int]): all zero positions found

#     Returns:
#         List[Tuple[int, int]]: List of tuples, where the first pair the tuple
#         indicates the zero position and the second the number of zeros
#     """
#     zeros: list[tuple[int, int]] = []

#     number_of_zeros = int(1)
#     first_repetition_pos = int(-1)
#     max_number_of_zeros = int(-1)
#     forward_pos = int(0)

#     for index, current_pos in enumerate(all_zeros_positions):
#         try:
#             forward_pos = all_zeros_positions[index + 1]
#         except IndexError:
#             forward_pos = current_pos

#         if forward_pos - current_pos == 1:
#             number_of_zeros += 1

#             if first_repetition_pos == -1:
#                 first_repetition_pos = current_pos

#         else:
#             if number_of_zeros > max_number_of_zeros:
#                 max_number_of_zeros = number_of_zeros

#                 if first_repetition_pos != -1:
#                     zeros.append((first_repetition_pos, number_of_zeros))
#                 else:
#                     zeros.append((current_pos, number_of_zeros))

#             number_of_zeros = int(1)
#             first_repetition_pos = int(-1)

#     return zeros


# def separate_the_numbers(arg: str) -> None:
#     """Verifica se os números na string 'arg' podem ser representados
#     em uma lista crescente e imprime 'Yes' e o menor número da lista,
#     caso contrário 'No'

#     Args:
#         arg (str): uma string contendo números

#     Returns:
#         None
#     """

#     all_zeros_positions = [
#         index for index, value in enumerate(arg) if value == "0"
#     ]

#     if 0 in all_zeros_positions:
#         print("No")
#         return None

#     truthful = bool(True)
#     min_number = math.inf

#     if len(all_zeros_positions) > 0:
#         zeros_positions = get_zeros(all_zeros_positions)

#         for index, (pos, order) in enumerate(zeros_positions):
#             start = pos - 1

#             left = arg[0:start]

#             found = int(arg[start:pos + order])

#             right = arg[pos + order:]

#             if found < min_number:
#                 min_number = found

#             if index == 0 and len(left) > 0:
#                 ref = start - order
#                 number = found - 1
#                 limit = pow(10, order - 1)
#                 while ref >= 0 and number >= limit:
#                     test = int(left[ref:ref + order])
#                     if number != test:
#                         truthful = False
#                         break
#                     min_number = number
#                     ref -= order
#                     number -= 1

#             if len(right) > 0:
#                 ref = 0
#                 number = found + 1
#                 limit = pow(10, order + 1)
#                 while ref < len(right) and number < limit:
#                     test = int(right[ref:ref + order + 1])
#                     if number != test:
#                         truthful = False
#                         break
#                     ref += order + 1
#                     number += 1

#             # print(
#             #     " - left: "
#             #     + left[pos - 5:]
#             #     + " - found: "
#             #     + found
#             #     + " - right: "
#             #     + right[:15]
#             # )
#         print(zeros_positions)

#         if not truthful:
#             print("No")
#             return

#         print("Yes " + str(min_number))


# Solução de 'lambdadelta_':
# https://www.hackerrank.com/challenges/separate-the-numbers/forum/comments/1242056
def separate_the_numbers(arg: str) -> None:

    length = len(arg)

    max_step = length // 2

    for step in range(1, max_step + 1):
        min_num = int(arg[:step])

        next_number = min_num
        position = 0

        while position < length:
            size = len(str(next_number))

            current_number = int(arg[position:position + size])

            if next_number != current_number:
                break

            next_number += 1
            position += size

        else:
            print(f"YES {min_num}")
            break

    else:
        print("NO")


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    # result = camelcase(s)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    # STRING = "111111121113111411151116111711181119"
    # separate_the_numbers(STRING)

    # STRING = "91011"

    # separate_the_numbers(STRING)

    STRING = "9899100101102103104"

    separate_the_numbers(STRING)

    STRING = "99910001001"

    separate_the_numbers(STRING)

    STRING = "100101102103"

    separate_the_numbers(STRING)

    STRING = "101103"

    separate_the_numbers(STRING)

    STRING = "010203"

    separate_the_numbers(STRING)

    STRING = "999100010001"

    separate_the_numbers(STRING)

    STRING = "".join([str(d) for d in range(0, 1000001)])

    separate_the_numbers(STRING)
