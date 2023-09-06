"""HackerRank
The Time in Words
https://www.hackerrank.com/challenges/the-time-in-words/
"""

# import math
# import os
# import random
# import re
# import sys


def numb2str(num: int) -> str:
    num_dictionary = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
    }
    if num <= 20:
        return num_dictionary[num]

    tens = 10 * (num // 10)
    ones = num - tens

    return (
        num_dictionary[tens]
        if ones == 0
        else num_dictionary[tens] + " " + num_dictionary[ones]
    )


def the_time_in_words(hour: int, minute: int) -> str:
    if minute == 0:
        return numb2str(hour) + " o' clock"
    if minute == 1:
        return numb2str(minute) + " minute past " + numb2str(hour)
    if minute < 30 and minute != 15:
        return numb2str(minute) + " minutes past " + numb2str(hour)
    if minute == 15:
        return "quarter past " + numb2str(hour)
    if minute == 30:
        return "half past " + numb2str(hour)
    if minute < 60 and minute != 45:
        return numb2str(60 - minute) + " minutes to " + numb2str(hour + 1)
    if minute == 45:
        return "quarter to " + numb2str(hour + 1)

    raise ValueError("Invalid minute")


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nk = input().split()

    # n = int(nk[0])

    # k = int(nk[1])

    # c = list(map(int, input().rstrip().split()))

    # result = jumpingOnClouds(c, k)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    response = the_time_in_words(5, 47)
    print(response)
    assert response == "thirteen minutes to six"

    response = the_time_in_words(3, 0)
    print(response)
    assert response == "three o' clock"

    response = the_time_in_words(7, 15)
    print(response)
    assert response == "quarter past seven"

    response = the_time_in_words(5, 45)
    print(response)
    assert response == "quarter to six"

    assert "eleven" == numb2str(11)
    assert "thirty" == numb2str(30)
    assert "thirty one" == numb2str(31)
    assert "fifty nine" == numb2str(59)
