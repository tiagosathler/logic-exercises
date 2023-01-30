"""
Challenge 02 - Diferença - difference

Dado um número X, retorne a diferença entre X e 10
de forma que o resultado seja sempre um valor positivo.

Isto é:
* se X < 10, faça 10 - X, ex: X = 3 -> 7 (10 - 3)
* se X > 10, faça X - 10, ex: X = 15 -> 5 (15 - 10)
"""


def difference(arg: int) -> int:
    """Dado um número 'x', retorne a diferença entre 'x' e 10
    de forma que o resultado seja sempre um valor positivo

    Args:
        arg (int): any integer

    Returns:
        int: absolute difference between x and 10
    """
    return abs(10 - arg)


if __name__ == "__main__":
    X = 3
    result = difference(X)
    print(result)

    X = 15
    result = difference(X)
    print(result)
