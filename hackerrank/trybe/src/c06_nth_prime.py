from typing import List


def find_next_prime(prime_numbers: List[int]) -> int:
    last = prime_numbers[len(prime_numbers) - 1]

    number = last + 2

    while any(number % element == 0 for element in prime_numbers):
        number += 2

    return number


def nth_prime(n: int) -> int:
    """
    Um número primo é um número natural que é divisível exclusivamente
    por 1 e por ele mesmo. Construa um algoritmo capaz de calcular o
    enésimo número primo para um dado número 'n', sendo n >= 2
    Por exemplo, para n = 6, tem-se os 6 primeiros números primos:
    (2, 3, 5, 7, 11, 13), onde 13 é o sexto número primo.
    """

    prime_numbers = [2, 3]

    for _ in range(2, n):
        found_prime_number = find_next_prime(prime_numbers)
        prime_numbers.append(found_prime_number)

    return prime_numbers[n - 1]


if __name__ == "__main__":
    n = 2
    result = nth_prime(n)
    print(result)

    n = 6
    result = nth_prime(n)
    print(result)

    n = 1001
    result = nth_prime(n)
    print(result)
