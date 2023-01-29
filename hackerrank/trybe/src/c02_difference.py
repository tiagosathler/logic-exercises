def difference(x: int) -> int:
    """
    Dado um número 'x', retorne a diferença entre 'x' e 10
    de forma que o resultado seja sempre um valor positivo
    """
    return abs(10 - x)


if __name__ == "__main__":
    x = 3
    result = difference(x)
    print(result)

    x = 15
    result = difference(x)
    print(result)
