"""HackerRank
Climbing the Leaderboard
https://www.hackerrank.com/challenges/climbing-the-leaderboard
"""

import math


def search(numbers: list[int], target: int, index: int) -> int:
    """Find the index of the nearest value

    Args:
        numbers (list[int]): the unique scores list
        target (int): value to search
        index (int): the current index

    Returns:
        int: the nearest index
    """
    if target == numbers[index]:
        return index

    if target < numbers[index]:
        return index + 1

    start = 0
    end = index

    while start <= end:
        mid = (start + end) // 2

        if numbers[mid] == target:
            return mid

        if numbers[mid + 1] <= target < numbers[mid]:
            return mid + 1

        if target > numbers[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1


def climbing_leaderboard(ranked: list[int], player: list[int]) -> list[int]:
    """Climbing leaderboard

    Args:
        ranked (list[int]): the leaderboard scores
        player (list[int]): the player's scores

    Returns:
        list[int]: the player's rank after each new score
    """
    last_value = math.inf
    ranked_list: int = []

    for value in ranked:
        if value < last_value:
            ranked_list.append(value)
            last_value = value

    player_rank: int = []
    index = len(ranked_list) - 1

    for pos, value in enumerate(player):
        index = search(ranked_list, value, index)
        if index == len(ranked_list):
            player_rank.append(index + 1)
            index -= 1
        elif 0 <= index < len(ranked_list):
            player_rank.append(index + 1)
        else:
            for _ in range(pos, len(player)):
                player_rank.append(1)
            break

    return player_rank


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    # result = superReducedString(s)

    # fptr.write(result + '\n')

    # fptr.close()

    ranked_data = [100, 100, 50, 40, 40, 20, 10]
    player_data = [5, 25, 50, 120]
    result_data = climbing_leaderboard(ranked_data, player_data)
    print(result_data)

    ranked_data = [100, 90, 90, 80, 75, 60]
    player_data = [50, 65, 77, 90, 102]
    result_data = climbing_leaderboard(ranked_data, player_data)
    print(result_data)
