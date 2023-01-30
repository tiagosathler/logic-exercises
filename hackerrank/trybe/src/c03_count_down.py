"""
Challenge 03 - Contagem regressiva - count_down

Dado um número X construa um programa que retorne
a contagem regressiva no formato X...X-1...X-2...0!!!

Exemplo:
* X = 10 -> 10...9...8...7...6...5...4...3...2...1...0!!!
"""


def count_down(arg: int) -> str:
    """Retorna a contagem regressiva no formato "x...x-1...x-2...0!!!

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
