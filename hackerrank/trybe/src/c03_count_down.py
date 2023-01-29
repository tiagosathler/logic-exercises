"""Challenge 03 - Count down"""


def count_down(arg: int) -> str:
    """Dado um número 'x', construa um programa que retorne a contagem
    regressiva no formato "x...x-1...x-2...0!!!

    Args:
        arg (int): any positive integer

    Returns:
        str: count down
    """
    result = str(arg)
    count = arg - 1
    while count > -1:
        result += "..." + str(count)
        count -= 1
    result += "!!!"
    return result


if __name__ == "__main__":
    X = 3
    RESPONSE = count_down(X)
    print(RESPONSE)

    X = 15
    RESPONSE = count_down(X)
    print(RESPONSE)
