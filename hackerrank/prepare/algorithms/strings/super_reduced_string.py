"""HackerRank
Super Reduced String
https://www.hackerrank.com/challenges/reduced-string/
"""


def super_reduced_string(s: str) -> str:
    """Reduce duplicates strings in a string

    Args:
        s (str): string to reduce

    Returns:
        str: the string reduced or "Empty string"
        if the string was reduced to empty string
    """
    strings = list(s)
    i = int(0)

    while i < len(strings):
        if i < len(strings) - 1 and strings[i] == strings[i + 1]:
            strings.pop(i)
            strings.pop(i)
            if i != 0:
                i -= 1
        else:
            i += 1

    if len(strings) == 0:
        return "Empty String"

    return "".join(strings)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    # result = superReducedString(s)

    # fptr.write(result + '\n')

    # fptr.close()

    s = "aaabccddd"

    result = super_reduced_string(s)

    print(result)

    s = "aa"

    result = super_reduced_string(s)

    print(result)

    s = "baab"

    result = super_reduced_string(s)

    print(result)

    s = (
        "ppffccmmssnnhhbbmmggxxaaooeeqqeennffzzaaeey"
        + "yaaggggeessvvssggbbccnnrrjjxxuuzzbbjjrruuaaccaaoommkkkkxx"
    )

    result = super_reduced_string(s)

    print(result)
