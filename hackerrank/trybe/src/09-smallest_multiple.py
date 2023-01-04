from typing import List


def find_next_prime(prime_numbers: List[int]) -> int:
    last = prime_numbers[len(prime_numbers) - 1]

    number = last + 2

    while any(number % element == 0 for element in prime_numbers):
        number += 2

    return number


def get_prime_numbers(n: int) -> int:
    prime_numbers = [2, 3]

    for _ in range(2, n):
        found_prime_number = find_next_prime(prime_numbers)
        if found_prime_number <= n:
            prime_numbers.append(found_prime_number)
        else:
            break
    # print(prime_numbers)
    return prime_numbers


# MINHA SOLUÇÃO DIFERE DO GABARITO A PARTIR DE n = 16:
def smallest_multiple(n: int) -> int:
    """
    O menor número divisível por TODOS os números de 1 a 10 é 2520.
    Crie um algoritmo capaz de calcular o menor número divisível por
    TODOS os números de 1 a um dado número.
    """
    prime_numbers = get_prime_numbers(n)

    prime_number_multiplication = 1

    for number in prime_numbers:
        prime_number_multiplication *= number

    smallest_multiple = prime_number_multiplication

    remnants_of_division = set([1])

    for number in range(1, n + 1):
        mod = prime_number_multiplication % number
        if mod != 0:
            remnants_of_division.add(mod)
            # phrase = (
            #     str(prime_number_multiplication)
            #     + " mod "
            #     + str(number)
            #     + " = "
            #     + str(mod)
            # )
            # print(phrase)

    # print(remnants_of_division)
    remnants_of_division_multiplication = 1
    for value in remnants_of_division:
        remnants_of_division_multiplication *= value

    smallest_multiple = (
        prime_number_multiplication * remnants_of_division_multiplication
    )

    return smallest_multiple


# GABARITO:
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
    for x in range(3, 21):
        result = smallest_multiple(x)
        print(str(x) + ", " + str(result))
