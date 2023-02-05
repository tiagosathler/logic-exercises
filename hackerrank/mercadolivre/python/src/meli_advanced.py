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

    return numbers


if __name__ == "__main__":
    SUM = 5
    MAX_DIGIT = 5
    N = 4

    numbers_generated = numbers_generator(N, SUM, MAX_DIGIT)

    for number_generated in numbers_generated:
        print(number_generated)
