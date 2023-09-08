"""HackerRank
Zig Zag Sequence
https://www.hackerrank.com/challenges/one-week-preparation-kit-zig-zag-sequence
"""


def zig_zag_sequence(a: list[int], n: int) -> None:
    """Zig Zag Sequence
    Args:
        a (list[int]): an array of n distinct integers
        n (int): the size of the array
        constraints: 1 <= a[i] < 10⁹ and 1 <= n < 10_000 (n is always odd)
    """
    a.sort()
    mid = int((n + 1) / 2 - 1)  #
    a[mid], a[n - 1] = a[n - 1], a[mid]
    st = mid + 1
    ed = n - 2  #
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1  #

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=" ")
    return


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # arr = []

    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))

    # fptr.write(str(result) + '\n')

    # fptr.close()
    array = [2, 3, 5, 1, 4]
    zig_zag_sequence([2, 3, 5, 1, 4], len(array))

    array = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    zig_zag_sequence(array, len(array))

    array = [1, 2, 3, 4, 5, 6, 7]
    zig_zag_sequence(array, len(array))
