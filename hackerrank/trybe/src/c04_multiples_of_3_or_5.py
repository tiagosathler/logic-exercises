def multiples_of_3_or_5(x: int) -> int:
    """
    Construa um algoritmo que encontre a soma de todos os números naturais
    múltiplos de 3 ou 5 menores que um dado número 'x'.
    """
    sum = 0
    for n in range(0, x):
        if n % 3 == 0 or n % 5 == 0:
            sum += n
    return sum


if __name__ == "__main__":
    x = 10
    result = multiples_of_3_or_5(x)
    print(result)

    x = 50
    result = multiples_of_3_or_5(x)
    print(result)
