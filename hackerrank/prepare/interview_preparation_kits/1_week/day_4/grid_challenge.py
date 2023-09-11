"""HackerRank
Grid Challenge
https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge
"""


def grid_challenge(grid: list[str]) -> str:
    """Grid Challenge

    Args:
        grid (list[str]): an array of strings

    Returns:
        str: either YES or NO

    Constraints:
        each string consists of lowercase letters in the range ascii[a-z]
    """
    grid = ["".join(sorted(list(string))) for string in grid]

    for i in range(len(grid) - 1):
        if any(grid[i][j] > grid[i+1][j] for j in range(len(grid[i]))):
            return "NO"

    return "YES"


if __name__ == "__main__":
    GRID = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
    RESPONSE = grid_challenge(GRID)
    print(RESPONSE)
    assert RESPONSE == "YES"

    GRID = [
        "eibjbwsp",
        "ptfxehaq",
        "jxipvfga",
        "rkefiyub",
        "kalwfhfj",
        "lktajiaq",
        "srdgoros",
        "nflvjznh",
    ]
    RESPONSE = grid_challenge(GRID)
    print(RESPONSE)
    assert RESPONSE == "NO"

    GRID = ["hcd", "awc", "shm"]
    RESPONSE = grid_challenge(GRID)
    print(RESPONSE)
    assert RESPONSE == "NO"

    GRID = ["sur", "eyy", "gxy"]
    RESPONSE = grid_challenge(GRID)
    print(RESPONSE)
    assert RESPONSE == "NO"

    GRID = ["nyx", "ynx", "xyt"]
    RESPONSE = grid_challenge(GRID)
    print(RESPONSE)
    assert RESPONSE == "YES"

    GRID = ["vpvv", "pvvv", "vzzp", "zzyy"]
    RESPONSE = grid_challenge(GRID)
    print(RESPONSE)
    assert RESPONSE == "YES"
