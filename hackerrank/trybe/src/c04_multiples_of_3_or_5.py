"""Challenge 04 - Multiples of 3 or 5"""


def multiples_of_3_or_5(arg: int) -> int:
    """Construa um algoritmo que encontre a soma de todos os números naturais
    múltiplos de 3 ou 5 menores que um dado número 'x'.

    Args:
        arg (int): any positive integer

    Returns:
        int: the sum of all numbers less than arg that are multiples of 3 and 5
    """
    acc = 0
    for number in range(0, arg):
        if number % 3 == 0 or number % 5 == 0:
            acc += number
    return acc


if __name__ == "__main__":
    X = 10
    result = multiples_of_3_or_5(X)
    print(result)

    X = 50
    result = multiples_of_3_or_5(X)
    print(result)
