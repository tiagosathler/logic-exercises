"""Challenge 05 - Sum of all Even Fibonacci numbers"""

from typing import List


def even_fibonacci_numbers(arg: int) -> List[int]:
    """
    Dado um número inteiro positivo 'x', construa a série de
    Fibonacci até igual ou menor que 'x' e calcule o somatório de todos
    os números pares da série.
    Considere a série de Fibonacci começando com "1, 2, ...."
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
