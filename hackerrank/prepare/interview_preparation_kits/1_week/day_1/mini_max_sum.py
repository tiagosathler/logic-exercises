"""HackerRank
Mini-Max Sum
https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum
"""


def mini_max_sum(array: list[int]) -> None:
    """Mini-Max Sum function

    Args:
        array (list[int]): an array of integers
    """
    array.sort()
    minimum_sum = sum(array[:len(array) - 1])
    maximum_sum = sum(array[1:])

    print(f"{minimum_sum} {maximum_sum}")


if __name__ == "__main__":
    mini_max_sum([1, 3, 5, 7, 9])
    mini_max_sum([1, 2, 3, 4, 5])
