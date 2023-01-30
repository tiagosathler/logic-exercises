"""
Challenge 05 - Números pares da série de Fibonacci - even_fibonacci_numbers

Uma série de Fibonacci iniciando com os números 1 e 2, do terceiro
elemento em diante calcula-se o próximo elemento como a soma do dois
anteriores, sucessivamente.

Dessa forma, os 10 primeiros elementos dessa série são:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89.

A soma dos números pares menores que 100 dessa série é 44.

Calcule a soma dos números pares entre os elementos dessa série
que sejam menores que um dado número.

* Algumas referências apontam a série de Fibonacci começando em 0.
Nesse caso a serie seria: 0, 1, 1, 2, 3, 5, ...
Para efeito dessa atividade considere a série iniciando em "1, 2".
"""


def even_fibonacci_numbers(arg: int) -> int:
    """Calcula a soma de todos os números pares da série de Fibonacci
    que vai até 'arg'.
    Considere a série de Fibonacci começando com "1, 2, ...."

    Args:
        arg (int): the highest number in the series

    Returns:
        int: the sum of all even numbers
    """
    fibonacci = [1, 2]

    element = 0
    index = len(fibonacci)

    while element <= arg:
        element = fibonacci[index - 2] + fibonacci[index - 1]
        index += 1
        if element <= arg:
            fibonacci.append(element)

    fibonacci_even_numbers = [
        number for number in fibonacci if number % 2 == 0
    ]

    sum_of_fibonacci_even_numbers = sum(fibonacci_even_numbers)
    return sum_of_fibonacci_even_numbers


if __name__ == "__main__":
    X = 100
    result = even_fibonacci_numbers(X)
    print(result)

    X = 3000000
    result = even_fibonacci_numbers(X)
    print(result)
