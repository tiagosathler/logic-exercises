"""_summary_"""

from typing import List


def numbers_generator(n_dig: int, summation: int, max_digit: int) -> List[int]:
    """Gerador de números - Método da força bruta

    Args:
        n_digit (int): número de dígitos
        summation (int): restrição: soma de todos os dígitos
        max_digit (int): restrição: número máximo para cada dígito

    Returns:
        list[int]: lista com todos os números possíveis
    """
    numbers = []

    min_number = int("1" * n_dig)
    max_number = max_digit * min_number

    for number in range(min_number, max_number + 1):
        sum_of_digits = 0
        for digit in str(number):
            if int(digit) <= max_digit:
                sum_of_digits += int(digit)
        if sum_of_digits == summation:
            numbers.append(number)

    return numbers


if __name__ == "__main__":
    SUM = 21
    MAX_DIGIT = 6
    N = 4

    numbers_generated = numbers_generator(N, SUM, MAX_DIGIT)

    for number_generated in numbers_generated:
        print(number_generated)
