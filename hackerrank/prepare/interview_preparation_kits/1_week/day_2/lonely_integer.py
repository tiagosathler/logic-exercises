"""HackerRank
Lonely Integer
https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer
"""


def lonely_integer(array: list[int]) -> int | None:
    """Lonely Integer function

    Args:
        array (list[int]): an array of integers
    """
    frequency: dict[int, int] = {element: 0 for element in array}

    for element in array:
        frequency[element] += 1

    for element, quantity in frequency.items():
        if quantity == 1:
            return element

    return None


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # a = list(map(int, input().rstrip().split()))
    assert lonely_integer([1, 2, 3, 4, 3, 2, 1]) == 4
