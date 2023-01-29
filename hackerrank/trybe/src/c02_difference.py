"""Challenge 02 - Difference"""


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
