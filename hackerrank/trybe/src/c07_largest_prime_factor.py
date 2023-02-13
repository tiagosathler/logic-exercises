"""
Challenge 07 - Maior divisor primo - largest_prime_factor

Números primos são aqueles que são divisíveis exclusivamente
por 1 e eles mesmos.

Os divisores primos de 13195, por exemplo, são 5, 7, 13 e 29.

Encontre o maior divisor primo de um dado número.
"""

import math
from typing import Set


def find_next_prime(prime_numbers: Set[int]) -> int:
    """Find the next prime number of a given set of prime numbers

    Args:
        prime_numbers (Set[int]): set of prime numbers

    Returns:
        int: next prime number of the given set
    """
    number = max(prime_numbers)

    if number % 2 == 0:
        number += 1

    while any(number % element == 0 for element in prime_numbers):
        number += 2

    return number


def largest_prime_factor(arg: int) -> int:
    """Encontra o maior divisor primo de um dado número.

    Args:
        arg (int): any positive integer prime

    Returns:
        int: largest integer prime factor
    """
    square_root_of_number = math.floor(math.sqrt(arg))

    prime_numbers = set([2])

    actual_prime_number = int(3)
    largest_prime_divisor = int(1)

    while actual_prime_number < square_root_of_number:
        actual_prime_number = find_next_prime(prime_numbers)
        prime_numbers.add(actual_prime_number)
        if arg % actual_prime_number == 0:
            largest_prime_divisor = actual_prime_number
    return largest_prime_divisor


if __name__ == "__main__":
    N = 13195
    result = largest_prime_factor(N)
    print(result)

    N = 26789
    result = largest_prime_factor(N)
    print(result)

    N = 3003289
    result = largest_prime_factor(N)
    print(result)
