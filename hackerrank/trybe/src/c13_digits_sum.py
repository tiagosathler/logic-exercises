""""
Challenge 13 - Soma dos dígitos - digits_sum

Escreva um programa capaz de encontrar quantos números entre 0 e
1000 têm a a soma dos seus dígitos igual a um dado número 'S'.

Por exemplo, para S = 26 temos 3 números, 899, 989 e 998, cujas
somas dos algarismos é igual a S.
"""


def digits_sum(arg: int) -> int:
    """Calculate how many numbers between 0 and
    1000 has the sum of its digits equal to a given number 'arg'.

    Args:
        arg (int): any positive integer

    Returns:
        int: number of numbers that meet the criteria
    """
    occurrences = []

    for number in range(0, 1001):
        summation = sum(int(d) for d in str(number))
        if summation == arg:
            occurrences.append(number)

    return len(occurrences)


if __name__ == "__main__":
    X = 26
    RESULT = digits_sum(X)
    print(str(X) + ", quantity of numbers: " + str(RESULT))

    X = 21
    RESULT = digits_sum(X)
    print(str(X) + ", quantity of numbers: " + str(RESULT))

    X = 15
    RESULT = digits_sum(X)
    print(str(X) + ", quantity of numbers: " + str(RESULT))
