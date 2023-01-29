"""Challenge 06 - nth prime of any positive integer"""

from typing import Set


def find_next_prime(prime_numbers: Set[int]) -> int:
    """Find the next prime number of a given set of prime numbers

    Args:
        prime_numbers (Set[int]): list of prime numbers

    Returns:
        int: next prime number of the given set
    """
    last = max(prime_numbers)

    number = last + 2

    while any(number % element == 0 for element in prime_numbers):
        number += 2

    return number


def nth_prime(arg: int) -> int:
    """Um número primo é um número natural que é divisível exclusivamente
    por 1 e por ele mesmo. Construa um algoritmo capaz de calcular o
    enésimo número primo para um dado número 'n', sendo n >= 2
    Por exemplo, para n = 6, tem-se os 6 primeiros números primos:
    (2, 3, 5, 7, 11, 13), onde 13 é o sexto número primo.

    Args:
        arg (int): any positive integer

    Returns:
        int: nth prime number
    """

    prime_numbers = set([2, 3])

    for _ in range(2, arg):
        found_prime_number = find_next_prime(prime_numbers)
        prime_numbers.add(found_prime_number)

    return max(prime_numbers)


if __name__ == "__main__":
    N = 2
    RESULT = nth_prime(N)
    print(RESULT)

    N = 6
    RESULT = nth_prime(N)
    print(RESULT)

    N = 1001
    RESULT = nth_prime(N)
    print(RESULT)
