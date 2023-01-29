""""Challenge 10 - Sum square difference"""


def sum_square_difference(arg: int) -> int:
    """
    O quadrado da soma dos 'n' primeiros números e'dado por:
    square_of_sum = (1 + 2 + 3 ... + n)^2

    A soma dos quadrados dos primeiros 'n' números naturais é dada por:
    sum_of_square = (1² + 2² + 3² + ... + n^2)

    Calcule a diferença entre o quadrado da soma e a soma dos quadrados dos
    'n' primeiros números naturais

    Args:
        arg (int): any positive integer

    Returns:
        int: difference between square_of_sum and sum_of_square
    """
    numbers = list(range(1, arg + 1))

    square_of_sum = pow(sum(numbers), 2)

    sum_of_squares = sum(pow(number, 2) for number in numbers)

    return square_of_sum - sum_of_squares


if __name__ == "__main__":
    for x in range(2, 21):
        result = sum_square_difference(x)
        print(str(x) + ", " + str(result))
