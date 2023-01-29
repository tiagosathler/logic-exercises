""""
Challenge 15 - Poligramas - polygram

Duas palavras A e B são anagramas entre si se podemos transformar a
palavra A na palavra B apenas trocando de posição as letras da palavra
A.
Por exemplo, 'duetos' e 'estudo' são anagramas entre si. Um outro
exemplo é 'bba' e 'bab'.

Vamos chamar de poligrama uma palavra que consiste na
concatenação de duas ou mais palavras que são anagramas entre si.
A primeira dessas palavras é chamada de raiz do poligrama.
Por exemplo, a palavra 'bbabab' é um poligrama com raiz 'bba', pois
ela é a concatenação dos anagramas 'bba' e 'bab'.

Dada uma palavra, escreva um programa que determine se ela é um
poligrama.

Caso a palavra seja um poligrama, o programa deve retornar a raiz
dele.

Caso contrário deve retornar uma string vazia.
"""


def polygram(arg: str) -> str:
    """Determine if the string 'arg' is a polygram and return its root

    Args:
        arg (str): compound word to be checked

    Returns:
        str: returns the root of the polygram or otherwise an empty string
    """
    if len(arg) % 2 != 0:
        return ""

    compound_word = arg.lower()

    half_index = int(len(arg) / 2)

    first_word = list(compound_word[:half_index])
    second_word = list(compound_word[half_index:])

    first_word.sort()
    second_word.sort()

    if "".join(first_word) == "".join(second_word):
        return arg[:half_index]

    return ""


if __name__ == "__main__":
    X = str("bbabab")
    RESULT = polygram(X)
    print(str(X) + ", polygram root: " + str(RESULT))

    X = str("duetosestudo")
    RESULT = polygram(X)
    print(str(X) + ", polygram root: " + str(RESULT))

    X = str("polidoli")
    RESULT = polygram(X)
    print(str(X) + ", polygram root: " + str(RESULT))
