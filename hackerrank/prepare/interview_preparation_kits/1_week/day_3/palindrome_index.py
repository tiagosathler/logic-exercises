"""HackerRank
Palindrome Index - Mock test
"""


def palindrome_index(string: str) -> int:
    half = len(string) // 2

    if string[0:half] == string[::-1][:half]:
        return -1

    inverse_parity = (len(string) + 1) % 2

    if string[half - inverse_parity] != string[half + 1]:
        # if string[half - 1 - inverse_parity] == string[half]:
        half -= 1

    left = half - inverse_parity
    right = half + 1

    while left >= 0 and right < len(string):
        if string[left] == string[right]:
            left -= 1
            right += 1

        else:
            if right < len(string) - 1 and string[left] == string[right + 1]:
                return right
            # if left > 0 and string[left - 1] == string[right]:
            return left

    return right if left < 0 else left


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
