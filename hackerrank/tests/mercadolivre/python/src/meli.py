def numbers_generator(n: int, sum_value: int, max_digit: int) -> list[int]:
    numbers = list()

    min = int("1" * n)
    max = max_digit * min

    for number in range(min, max + 1):
        sum_of_digits = 0
        for digit in str(number):
            if int(digit) <= max_digit:
                sum_of_digits += int(digit)
        if sum_of_digits == sum_value:
            numbers.append(number)

    return numbers


if __name__ == "__main__":
    """
    Dado um input de 'maxDigit' - um dígito de 1 a 9,
    encontre todas as combinações possíveis para gerar
    números de n dígitos (n=4 -> "xxxx"), cuja soma desses
    'n' DÍGITOS seja IGUAL a 'sum' (21)
    E que todos sejam quaisquer dígitos igual ou menor que 'maxDigit'

    Se não houver solução imprima 'null'
    """

    sum = 3
    max_digit = 6
    n = 4

    numbers = numbers_generator(n, sum, max_digit)

    for number in numbers:
        print(number)

    print(len(numbers))
