"""Number generator
By ChatGPT
"""


def number_generator(
    number_of_digits: int, summation: int, max_digit: int
) -> list[int]:
    """Number generator

    Args:
        number_of_digits (int): the number of digits in a number
        summation (int): the sum of all digits of a number
        max_digit (int): the maximum digit of a number

    Returns:
        list[int]: the list of all possible numbers
    """

    def generate_numbers(
        current_number: str, remaining_digits: int, remaining_sum: int
    ) -> None:
        """Generate number recursively

        Args:
            current_number (str): the current number in the string format
            remaining_digits (int): the remaining number of digits
            remaining_sum (int): the remaining number of summation
        """
        if remaining_digits == 0:
            if remaining_sum == 0:
                valid_numbers.append(int(current_number))
            return

        for digit in range(max_digit, -1, -1):
            if remaining_sum - digit >= 0:
                generate_numbers(
                    current_number + str(digit),
                    remaining_digits - 1,
                    remaining_sum - digit,
                )

    if number_of_digits * max_digit < summation:
        return []

    valid_numbers: list[int] = []
    generate_numbers("", number_of_digits, summation)
    return sorted(valid_numbers)


if __name__ == "__main__":
    NUMBER_OF_DIGITS = 4
    SUMMATION = 21
    MAX_DIGIT = 6
    result = number_generator(NUMBER_OF_DIGITS, SUMMATION, MAX_DIGIT)
    print(result)

    NUMBER_OF_DIGITS = 4
    SUMMATION = 5
    MAX_DIGIT = 5
    result = number_generator(NUMBER_OF_DIGITS, SUMMATION, MAX_DIGIT)
    print(result)

    NUMBER_OF_DIGITS = 4
    SUMMATION = 25
    MAX_DIGIT = 6
    result = number_generator(NUMBER_OF_DIGITS, SUMMATION, MAX_DIGIT)
    print(result)
