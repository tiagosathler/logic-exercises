"""HackerRank
Palindrome Index - Mock test
"""


def is_palindrome(string: str) -> bool:
    """Is palindrome?

    Args:
        string (str): a string to check

    Returns:
        bool: True if string is a palindrome, False otherwise
    """
    return string == string[::-1]


def palindrome_index(string: str) -> int:
    """Palindrome Index of string

    Args:
        string (str): a string to analyze

    Returns:
        int: the index of the character to remove or -1 if string is palindrome
    """
    if is_palindrome(string):
        return -1

    size = len(string)

    for i in range(size // 2):
        if string[i] != string[size - 1 - i]:
            new_string = string[:i] + string[i + 1:]
            if is_palindrome(new_string):
                return i

            new_string = string[: size - 1 - i] + string[size - i:]
            if is_palindrome(new_string):
                return size - 1 - i

    return -1  # No solution found


if __name__ == "__main__":
    RESPONSE = palindrome_index("a")
    print(RESPONSE)
    assert RESPONSE == -1

    RESPONSE = palindrome_index("aa")
    print(RESPONSE)
    assert RESPONSE == -1

    RESPONSE = palindrome_index("aba")
    print(RESPONSE)
    assert RESPONSE == -1

    RESPONSE = palindrome_index("baab")
    print(RESPONSE)
    assert RESPONSE == -1

    RESPONSE = palindrome_index("baxa")
    print(RESPONSE)
    assert RESPONSE == 0

    RESPONSE = palindrome_index("axab")
    print(RESPONSE)
    assert RESPONSE == 3

    RESPONSE = palindrome_index("ayxyab")
    print(RESPONSE)
    assert RESPONSE == 5

    RESPONSE = palindrome_index("baaba")
    print(RESPONSE)
    assert RESPONSE == 4

    RESPONSE = palindrome_index("abaab")
    print(RESPONSE)
    assert RESPONSE == 0

    RESPONSE = palindrome_index("bcbc")
    print(RESPONSE)
    assert RESPONSE == 0

    RESPONSE = palindrome_index("baa")
    print(RESPONSE)
    assert RESPONSE == 0

    RESPONSE = palindrome_index("aaab")
    print(RESPONSE)
    assert RESPONSE == 3

    RESPONSE = palindrome_index("eaaef")
    print(RESPONSE)
    assert RESPONSE == 4

    RESPONSE = palindrome_index("feaae")
    print(RESPONSE)
    assert RESPONSE == 0

    RESPONSE = palindrome_index("baeaefab")
    print(RESPONSE)
    assert RESPONSE == 5
