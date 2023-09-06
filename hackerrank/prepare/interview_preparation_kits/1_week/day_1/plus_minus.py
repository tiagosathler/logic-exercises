"""HackerRank
Plus Minus
https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus
"""


def plus_minus(array: list[int]) -> None:
    """Plus Minus function

    Args:
        array (list[int]): an array of integers
    """
    signal_separation: dict[str, int] = {
        "negatives": 0,
        "zeros": 0,
        "positives": 0,
    }

    for element in array:
        if element < 0:
            signal_separation["negatives"] += 1
        elif element == 0:
            signal_separation["zeros"] += 1
        else:
            signal_separation["positives"] += 1

    print(f"{signal_separation['positives'] / len(array):.6f}")
    print(f"{signal_separation['negatives'] / len(array):.6f}")
    print(f"{signal_separation['zeros'] / len(array):.6f}")


if __name__ == "__main__":
    plus_minus([1, 1, 0, -1, -1])
