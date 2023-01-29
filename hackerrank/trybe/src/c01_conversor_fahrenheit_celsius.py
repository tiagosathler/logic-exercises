"""Challenge 01 - Conversor Fahrenheit to Celsius temperature"""


def fahrenheit_to_celsius(arg: float) -> float:
    """Converts Fahrenheit temperature to Celsius

    Args:
        arg (float): temperature in Fahrenheit

    Returns:
        float: temperature in Celsius
    """
    temperature_in_celsius = (arg - 32) / 1.8
    return round(temperature_in_celsius, 1)


if __name__ == "__main__":
    TEMP = 100.0
    ct = fahrenheit_to_celsius(TEMP)
    print(ct)
