"""HackerRank
Recursive Digit Sum - Super Digit
https://www.hackerrank.com/challenges/one-week-preparation-kit-recursive-digit-sum
"""


def super_digit(number: str, k: int) -> int:
    """Recursive Digit Sum - Super Digit

    Args:
        number (str): a string representation of an integer
        k (int): the times to concatenate 'number' to make 'p'

    Returns:
        int: the super digit on 'number' repeated 'k' times

    Constraints:
        1 <= number <= 10 ** 100_000
        1 <= k <= 10 ** 5
    """
    number = str(k * sum(int(d) for d in number))

    while len(number) > 1:
        number = str(sum(int(d) for d in number))

    return int(number)


if __name__ == "__main__":
    RESPONSE = super_digit("9875", 4)
    print(RESPONSE)
    assert RESPONSE == 8
