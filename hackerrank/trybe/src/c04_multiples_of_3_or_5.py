"""
Challenge 04 - Múltiplos de 3 ou 5 - multiples_of_3_or_5

Construa um algoritmo que encontre a soma de todos os números
naturais múltiplos de 3 ou 5 menores que um dado número.

Exemplo:
Quando listamos todos os números naturais menores que 10
que são múltiplos de 3 ou 5 temos: 3, 5, 6 e 9.
A soma desses números é 3 + 5 + 6 + 9 = 23
"""


def multiples_of_3_or_5(arg: int) -> int:
    """Calcula a soma de todos os números naturais
    múltiplos de 3 ou 5 menores que um dado número 'arg'.

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
