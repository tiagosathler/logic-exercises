import math
from typing import List


def find_next_prime(prime_numbers: List[int]) -> int:
    last = prime_numbers[len(prime_numbers) - 1]

    number = last + 2

    while any(number % element == 0 for element in prime_numbers):
        number += 2

    return number


def largest_prime_factor(n: int) -> int:
    """
    Números primos são aqueles que são divisíveis exclusivamente
    por 1 e por eles mesmos. Ex: 2, 3, 5, 7, 11, 13, 17, 19...
    Os divisores primos de 13195, por exemplo, são 5, 7, 13, 29.
    Encontre o maior divisor primo de um dado número.
    """
    square_root_of_number = math.floor(math.sqrt(n))

    prime_numbers = [2, 3]

    actual_prime_number = 3
    largest_prime_divisor = 1

    while actual_prime_number < square_root_of_number:
        actual_prime_number = find_next_prime(prime_numbers)
        prime_numbers.append(actual_prime_number)
        if n % actual_prime_number == 0:
            largest_prime_divisor = actual_prime_number
    return largest_prime_divisor


if __name__ == "__main__":
    n = 13195
    result = largest_prime_factor(n)
    print(result)

    n = 26789
    result = largest_prime_factor(n)
    print(result)

    n = 3003289
    result = largest_prime_factor(n)
    print(result)
