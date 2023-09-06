"""HackerRank
Time Conversion
https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum
"""


def time_conversion(time: str) -> str:
    """Time Conversion function

    Args:
        array (list[int]): an array of integers
    """
    separated_time = time.split(":")
    hour = int(separated_time[0])
    minute = int(separated_time[1])
    second = int(separated_time[2][:2])
    midday = separated_time[2][2:]

    if midday.upper() == "PM" and hour < 12:
        hour += 12
    elif midday.upper() == "AM" and hour >= 12:
        hour -= 12

    return f"{hour:0>2d}:{minute:0>2d}:{second:0>2d}"


if __name__ == "__main__":
    assert time_conversion("12:01:00PM") == "12:01:00"
    assert time_conversion("12:01:00AM") == "00:01:00"
    assert time_conversion("04:15:20AM") == "04:15:20"
    assert time_conversion("04:25:35PM") == "16:25:35"
    assert time_conversion("12:00:00PM") == "12:00:00"
    assert time_conversion("12:00:00AM") == "00:00:00"
