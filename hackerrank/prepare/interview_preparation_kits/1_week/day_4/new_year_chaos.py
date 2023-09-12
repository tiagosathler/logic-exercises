"""HackerRank
New Year Chaos - Minimum Bribes
https://www.hackerrank.com/challenges/one-week-preparation-kit-new-year-chaos
"""


def minimum_bribes(people_queue: list[int]) -> None:
    bribes = 0

    for i, person_position in enumerate(people_queue):
        # Check if the person at position i bribed more than two people
        if person_position - (i + 1) > 2:
            print("Too chaotic")
            return

        # Count the number of bribes made by the person at position i
        for j in range(max(0, person_position - 2), i):
            if people_queue[j] > person_position:
                bribes += 1

    print(bribes)


if __name__ == "__main__":
    minimum_bribes([1, 2, 3, 5, 4, 6, 7, 8])  # prints '1'

    minimum_bribes([4, 1, 2, 3])  # prints 'Too chaotic'

    minimum_bribes([2, 1, 5, 3, 4])  # prints '3'

    minimum_bribes([2, 5, 1, 3, 4])  # prints 'Too chaotic'

    minimum_bribes([5, 1, 2, 3, 7, 8, 6, 4])  # prints 'Too chaotic'

    minimum_bribes([1, 2, 5, 3, 7, 8, 6, 4])  # prints 7
