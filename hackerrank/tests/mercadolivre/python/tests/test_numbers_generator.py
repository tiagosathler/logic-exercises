"""Teste do algoritmo do desafio"""

from src.meli import numbers_generator


def test_numbers_generated_case_1():
    """testando para N = 4, SUM = 21, MAX_DIGIT = 6"""
    expected = [
        3666,
        4566,
        4656,
        4665,
        5466,
        5556,
        5565,
        5646,
        5655,
        5664,
        6366,
        6456,
        6465,
        6546,
        6555,
        6564,
        6636,
        6645,
        6654,
        6663,
    ]

    result = numbers_generator(4, 21, 6)
    for index, value in enumerate(result):
        assert value == expected[index]
