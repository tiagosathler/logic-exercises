def solveMeFirst(a: int, b: int) -> int:
    """
    https://www.hackerrank.com/challenges/solve-me-first
    """
    return a + b


if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    res = solveMeFirst(num1, num2)
    print(res)
