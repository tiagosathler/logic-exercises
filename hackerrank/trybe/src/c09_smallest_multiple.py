import math
from typing import Set


def find_next_prime(prime_numbers: Set[int]) -> int:
    last = max(prime_numbers)

    number = last + 2

    if last % 2 == 0:
        number = last + 1

    while any([number % prime == 0 for prime in prime_numbers]):
        number += 2

    return number


def get_prime_numbers(n: int) -> Set[int]:
    prime_numbers = set([2])

    for _ in range(1, n):
        found_prime_number = find_next_prime(prime_numbers)

        if found_prime_number > n:
            break

        elif found_prime_number == n:
            prime_numbers.add(found_prime_number)
            break

        else:
            prime_numbers.add(found_prime_number)

    return prime_numbers


def is_all_multiply(multiple: int, numbers: set) -> bool:
    return all([multiple % denominator == 0 for denominator in numbers])


def smallest_multiple(n: int) -> int:
    """
    O menor número divisível por TODOS os números de 1 a 10 é 2520.
    Crie um algoritmo capaz de calcular o menor número divisível por
    TODOS os números de 1 a um dado número.
    """
    numbers = set(list(range(1, n + 1)))

    prime_numbers = get_prime_numbers(n)

    composite_numbers = numbers.difference(prime_numbers)

    prime_product = math.prod(prime_numbers)

    mod_numbers = list()

    for number in composite_numbers:
        mod = (prime_product * math.prod(mod_numbers)) % number

        if mod != 0:
            mod = int(2)

            while not is_all_multiply(
                prime_product * mod * math.prod(mod_numbers),
                list(range(1, number + 1)),
            ):
                mod += 1

            mod_numbers.append(mod)

    mod_product = math.prod(mod_numbers)
    smallest_multiple = prime_product * mod_product

    return smallest_multiple


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
