""""Challenge 12 - Lychrel numbers"""


def is_palindrome(arg: int) -> bool:
    """Checks whether a given number is a palindrome

    Args:
        arg (int): any positive integer

    Returns:
        bool: True if is palindrome, False otherwise
    """
    number = list(str(arg))
    reversed_number = number.copy()
    reversed_number.reverse()

    return "".join(number) == "".join(reversed_number)


def sum_with_reverse(arg: int) -> int:
    """Calculates the sum of an 'arg' number with its own reverse number

    Args:
        arg (int): any positive integer

    Returns:
        int: sum of numbers
    """
    number = list(str(arg))
    number.reverse()
    reverse_number = "".join(number)

    return arg + int(reverse_number)


def lychrel_numbers(arg: int) -> int:
    """
    Números palíndromos podem se lidos da esquerda para direita ou da
    direita para esquerda com o mesmo resultado.

    Se pegarmos o número 47 e o somarmos ao seu reverso, 74, temos
    47 + 74 = 121, que é um número palíndromo.

    Nem todos os os números geram palíndromos de forma tão rápida
    quanto 47. Por exemplo, 349:
    * 349 + 943 = 1292,
    * 1292 + 2921 = 4213
    * 4213 + 3124 = 7337 (palíndromo)
    Ou seja, 349 levou 3 interações para gerar um palíndromo pelas somas
    dos resultados com seu reverso.

    Apesar de não ser formalmente provado, acredita-se que números
    como 196 jamais gerarão um palíndromo pelas somas dos resultados de
    seus resultados como os respectivos reversos.
    Um número que não gera palíndromos a partir desse processo é
    chamado de Número de Lychrel.
    Acredita-se que para qualquer número abaixo de 10.000:
    * gerará um palíndromo a partir da soma dos resultados com seus
    reversos até a 50a iteração;
    * não será possível gerar um palíndromo nem mesmo com todo o
    poder computacional disponível do mundo.

    Construa um algoritmo capaz de identificar a quantidade de
    números de Lychrel menores que um dado número N < 10.000

    Args:
        arg (int): any positive integer less then 10000

    Returns:
        int: number of Lychrel numbers
    """
    count = int(0)
    number = arg - 1

    while number > 9:
        next_number = number
        for i in range(0, 50):
            next_number = sum_with_reverse(next_number)
            if is_palindrome(next_number):
                break
            if i == 49:
                count += 1
                break

        number -= 1

    return count


if __name__ == "__main__":
    X = 501
    RESULT = lychrel_numbers(X)
    print(str(X) + ", quantity of Lychrel numbers: " + str(RESULT))

    X = 1001
    RESULT = lychrel_numbers(X)
    print(str(X) + ", quantity of Lychrel numbers: " + str(RESULT))

    X = 5001
    RESULT = lychrel_numbers(X)
    print(str(X) + ", quantity of Lychrel numbers: " + str(RESULT))

    X = 10000
    RESULT = lychrel_numbers(X)
    print(str(X) + ", quantity of Lychrel numbers: " + str(RESULT))
