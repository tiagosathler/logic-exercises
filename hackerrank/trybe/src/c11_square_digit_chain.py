""""Challenge 11 - Square digit chain"""


def is_89_chain(arg) -> bool:
    """Check if chain from 'arg' finishes with '89'

    Args:
        arg (int): any positive integer

    Returns:
        bool: True case the chain finishes with '89'
    """
    chain = [arg]
    i = 0

    while chain[i] != 89 and chain[i] != 1:
        number = str(chain[i])
        next_number = sum(pow(int(digit), 2) for digit in number)
        chain.append(next_number)
        i += 1

    return chain[i] == 89


def square_digit_chain(arg: int) -> int:
    """
    Uma cadeia de números é gerada a partir da soma dos quadrados dos
    dígitos do número anterior até ue o número formado já esteja
    presente nessa cadeia.

    Por exemplo:
    * 44 - 32 - 13 - 10 - 1 - 1 / explicação:
        4² + 4² = 32 |
        3² + 2² = 13 |
        1² + 3² = 10 |
        1² + 0² = 1 |
        1² = 1
    * 85 - 89 - 175 - 42 - 20 - 4 - 16 - 37 - 58 - 89 ...

    Qualquer cadeia que chegue a um número repetido ficará presa em
    um lopping infinito entre a primeira ocorrência desse número e a
    segunda ocorrência dele.

    No caso do 1, a partir da primeira ocorrência, todos os números serão
    1.
    No caso do 89, uma vez que ele seja atingido, a sequência será eternamente
    a mesma que até alcançar 89 novamente.

    Construa um algoritmo capaz de contar quantas cadeias terminarão em 89
    considerando cadeias que se iniciem com todos os números menores que um
    dado número N.

    Args:
        arg (int): any positive integer

    Returns:
        int: number of chains that finished with '89'
    """
    number = arg - 1
    count = int(0)

    while number > 0:
        if is_89_chain(number):
            count += 1
        number -= 1

    return count


if __name__ == "__main__":
    X = 2
    RESULT = square_digit_chain(X)
    print(str(X) + ", number of chains: " + str(RESULT))

    X = 11
    RESULT = square_digit_chain(X)
    print(str(X) + ", number of chains: " + str(RESULT))

    X = 90
    RESULT = square_digit_chain(X)
    print(str(X) + ", number of chains: " + str(RESULT))

    X = 146
    RESULT = square_digit_chain(X)
    print(str(X) + ", number of chains: " + str(RESULT))

    X = 201
    RESULT = square_digit_chain(X)
    print(str(X) + ", number of chains: " + str(RESULT))
