"""HackerRank
Tower Breakers
https://www.hackerrank.com/challenges/one-week-preparation-kit-tower-breakers-1
"""


def tower_breakers(number_of_towers: int, height: int) -> int:
    """Tower Breakers

    Args:
        number_of_towers (int): the number of towers
        height (int): the height of each tower

    Returns:
        int: the winner of the game
    """
    return 1 if number_of_towers % 2 == 1 and height != 1 else 2


if __name__ == "__main__":
    assert tower_breakers(2, 6) == 2

    assert tower_breakers(2, 2) == 2

    assert tower_breakers(1, 4) == 1

    assert tower_breakers(691094, 397662) == 2

    assert tower_breakers(100_000, 1) == 2

    assert tower_breakers(100_001, 1) == 2
