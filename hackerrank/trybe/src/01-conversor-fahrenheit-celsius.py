def farenheit_to_celsius(ft: float) -> float:
    """
    Converts Farenheit to Celsius temperature
    """
    ct = (ft - 32) / 1.8
    return round(ct, 1)


if __name__ == "__main__":
    ft = 100.0
    ct = farenheit_to_celsius(ft)
    print(ct)
