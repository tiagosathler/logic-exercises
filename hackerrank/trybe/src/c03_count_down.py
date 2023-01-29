def count_down(x: int) -> str:
    """
    Dado um número 'x', construa um programa que retorne a contagem
    regressiva no formato "x...x-1...x-2...0!!!
    """
    result = str(x)
    count = x - 1
    while count > -1:
        result += "..." + str(count)
        count -= 1
    result += "!!!"
    return result


if __name__ == "__main__":
    x = 3
    result = count_down(x)
    print(result)

    x = 15
    result = count_down(x)
    print(result)
