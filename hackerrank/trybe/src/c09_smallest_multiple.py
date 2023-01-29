"""Challenge 09 - Smallest multiple"""
import math
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

    if last % 2 == 0:
        number = last + 1

    while any(number % prime == 0 for prime in prime_numbers):
        number += 2

    return number


def get_prime_numbers(arg: int) -> Set[int]:
    """Get all prime numbers up to the number given by arg

    Args:
        arg (int): any positive integer

    Returns:
        Set[int]: set of all prime numbers
    """
    prime_numbers = set([2])

    for _ in range(1, arg):
        found_prime_number = find_next_prime(prime_numbers)

        if found_prime_number < arg:
            prime_numbers.add(found_prime_number)
            continue

        if found_prime_number == arg:
            prime_numbers.add(found_prime_number)
            break

        break

    return prime_numbers


def is_all_multiply(numbers: set, multiple: int) -> bool:
    """Checks if all numbers of 'numbers' are divisible by 'multiple'

    Args:
        multiple (int): any positive integer
        numbers (set): any set of positive integer

    Returns:
        bool: True if the numbers are divisible by multiple
    """
    return all(multiple % denominator == 0 for denominator in numbers)


def smallest_multiple(arg: int) -> int:
    """ O menor número divisível por TODOS os números de 1 a 10 é 2520.
    Crie um algoritmo capaz de calcular o menor número divisível por
    TODOS os números de 2 a um dado número.

    Args:
        arg (int): maximum number of a sequence >= 2

    Returns:
        int: the smallest multiple of a given string up to 'arg'
    """
    numbers = set(list(range(1, arg + 1)))

    prime_numbers = get_prime_numbers(arg)

    composite_numbers = numbers.difference(prime_numbers)

    prime_product = math.prod(prime_numbers)

    mod_numbers = []

    for number in composite_numbers:
        mod = (prime_product * math.prod(mod_numbers)) % number

        if mod != 0:
            mod = int(2)

            while not is_all_multiply(
                list(range(1, number + 1)),
                prime_product * mod * math.prod(mod_numbers),
            ):
                mod += 1

            mod_numbers.append(mod)

    return prime_product * math.prod(mod_numbers)


# GABARITO:
# (gasta-se um tempo absurdo para n = 20)
# def smallest_multiple(n: int) -> int:
#     """
#     O menor número divisível por TODOS os números de 1 a 10 é 2520.
#     Crie um algoritmo capaz de calcular o menor número divisível por
#     TODOS os números de 1 a um dado número.
#     """
#     i = n
#     number = n

#     while i > 0:
#         if number % i != 0:
#             i = n
#             number += 1
#         else:
#             i -= 1
#     return number


if __name__ == "__main__":
    for x in range(2, 21):
        result = smallest_multiple(x)
        print(str(x) + ", " + str(result))
