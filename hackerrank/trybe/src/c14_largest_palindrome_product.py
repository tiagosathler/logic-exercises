""""
Challenge 14 - Maior Produto Palíndromo - largest_palindrome_product

Um número palíndromo tem a o mesmo valor sendo ser lido da direita
para a esquerda ou da esquerda para direita, por exemplo: 11, 212,
3773, 1034301..

O maior número palíndromo resultado do produto de dois números
de 2 dígitos é 9009 (91 x 91)

Encontre o maior número palíndromo resultado do produto de dois
números com um determinado número de dígitos.
"""


def is_palindrome(arg: int) -> bool:
    """Checks whether a given number is a palindrome

    Args:
        arg (int): any positive integer

    Returns:
        bool: True if is palindrome, False otherwise
    """
    number = list(str(arg))

    return "".join(number) == "".join(reversed(number))


def largest_palindrome_product(digits: int) -> int:
    """Calculate how many numbers between 0 and
    1000 has the sum of its digits equal to a given number 'arg'.

    Args:
        digits (int): number of digits in a number

    Returns:
        int: the largest palindrome formed by numbers with n 'digits'
    """
    min_number = int(str("9" * (digits - 1)))
    max_number = int(str("9" * digits))

    occurrences = []

    for number_a in range(max_number + 1, min_number, -1):
        for number_b in reversed(range(number_a, max_number + 1)):
            multiply = number_a * number_b
            if is_palindrome(multiply):
                occurrences.append(multiply)

    return max(occurrences)


if __name__ == "__main__":
    X = 2
    RESULT = largest_palindrome_product(X)
    print(str(X) + ", the largest palindrome formed: " + str(RESULT))

    X = 3
    RESULT = largest_palindrome_product(X)
    print(str(X) + ", the largest palindrome formed: " + str(RESULT))

    X = 4
    RESULT = largest_palindrome_product(X)
    print(str(X) + ", the largest palindrome formed: " + str(RESULT))
