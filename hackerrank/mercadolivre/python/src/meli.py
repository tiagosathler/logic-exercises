"""_summary_"""


def numbers_generator(n_dig: int, summation: int, max_digit: int) -> list[int]:
    """Gerador de números - Método da força bruta

    Args:
        n_dig (int): número de dígitos: n_dig >= 1
        summation (int): soma de todos os dígitos: summation >= 1
        max_digit (int): número máximo para cada dígito: 9 <= max_digit <= 1

    Returns:
        list[int]: lista com todos os números possíveis
    """
    if not (isinstance(n_dig, int) and n_dig >= 1):
        raise ValueError(
            "'n_dig' must be an integer equal to or greater than 1"
        )

    if not (isinstance(summation, int) and summation > 1):
        raise ValueError("'summation' must be integer greater than 1")

    if not (isinstance(max_digit, int) and 1 <= max_digit <= 9):
        raise ValueError("'max_digit' must be an integer between 1 and 9")

    if summation > max_digit * n_dig:
        return []

    numbers: list[int] = []

    min_number = int(1)
    max_number = int(str(max_digit) * n_dig)

    for number in range(min_number, max_number + 1):
        if any(
            int(d) > max_digit or int(d) > summation for d in list(str(number))
        ):
            continue

        if summation == sum(int(d) for d in list(str(number))):
            numbers.append(number)

    return numbers


if __name__ == "__main__":
    SUM = 21
    MAX_DIGIT = 6
    N = 4

    numbers_generated = numbers_generator(N, SUM, MAX_DIGIT)

    for number_generated in numbers_generated:
        print(number_generated)
