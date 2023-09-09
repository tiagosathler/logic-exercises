"""HackerRank
Caesar's cipher
https://www.hackerrank.com/challenges/one-week-preparation-kit-caesar-cipher-1
"""

ALPHABET_SIZE = ord("Z") - ord("A") + 1


def is_it_alphabet_code(letter_code: int) -> bool:
    """Is it alphabet code?

    Args:
        letter_code (int): unicode letter code

    Returns:
        bool: true if letter_code is an alphabet code, false otherwise
    """
    return (ord("A") <= letter_code <= ord("Z")
            or ord("a") <= letter_code <= ord("z"))


def calculate_the_rotation(letter_code: int, rotation: int) -> int:
    """Calculate the rotation

    Args:
        letter_code (int): unicode letter code
        rotation (int): the alphabet rotation factor

    Returns:
        int: the rotation factor that keeps within the range
        of the letter of the alphabet (upper or lower case)
    """
    return (
        rotation
        if (letter_code <= ord("Z") and letter_code + rotation <= ord("Z"))
        or (letter_code >= ord("a") and letter_code + rotation <= ord("z"))
        else (rotation - ALPHABET_SIZE)
    )


def shift_char(letter: str, rotation: int) -> str:
    """Shift a character by a given rotation

    Args:
        letter (str): a character to shift
        rotation (int): the alphabet rotation factor

    Returns:
        str: the alphabet letter shifted or non-alphabetic character
    """
    if 'a' <= letter <= 'z':
        return chr(
               ord('a') + ((ord(letter) - ord('a') + rotation) % ALPHABET_SIZE)
            )

    if 'A' <= letter <= 'Z':
        return chr(
               ord('A') + ((ord(letter) - ord('A') + rotation) % ALPHABET_SIZE)
            )

    return letter


def caesars_cipher(phrase: str, rotation: int) -> str:
    """Caesar's cipher

    Args:
        phrase (str): clear text
        rotation (int): the alphabet rotation factor

    Returns:
        str: the encrypted string
    """

    rotation = rotation % ALPHABET_SIZE

    if rotation == 0:
        return phrase

    ciphered = ""

    for char in phrase:
        # char_code = ord(char)

        # if is_it_alphabet_code(char_code):
        #     char_code += calculate_the_rotation(char_code, rotation)
        #     ciphered += chr(char_code)

        # else:
        #     ciphered += char
        ciphered += shift_char(char, rotation)

    return ciphered


if __name__ == "__main__":
    assert (
        caesars_cipher("There's-a-starman-waiting-in-the-sky", 3)
        == "Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb"
    )
    assert caesars_cipher("sky", 3) == "vnb"

    assert (
        caesars_cipher(
            "1X7T4VrCs23k4vv08D6yQ3S19G4rVP188M9ahuxB6j1tMGZs1m10ey7eUj62WV2exLT4C83zl7Q80M",
            27,
        )
        == "1Y7U4WsDt23l4ww08E6zR3T19H4sWQ188N9bivyC6k1uNHAt1n10fz7fVk62XW2fyMU4D83am7R80N"
    )

    assert (
        caesars_cipher(
            "6DWV95HzxTCHP85dvv3NY2crzt1aO8j6g2zSDvFUiJj6XWDlZvNNr",
            87,
        )
        == "6MFE95QigCLQY85mee3WH2laic1jX8s6p2iBMeODrSs6GFMuIeWWa"
    )
