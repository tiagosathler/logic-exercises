"""Teste do algoritmo do desafio"""

import pytest
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
    assert result == expected


def test_numbers_generated_case_2():
    """testando para N = 4, SUM = 5, MAX_DIGIT = 5"""
    expected = [
        5,
        14,
        23,
        32,
        41,
        50,
        104,
        113,
        122,
        131,
        140,
        203,
        212,
        221,
        230,
        302,
        311,
        320,
        401,
        410,
        500,
        1004,
        1013,
        1022,
        1031,
        1040,
        1103,
        1112,
        1121,
        1130,
        1202,
        1211,
        1220,
        1301,
        1310,
        1400,
        2003,
        2012,
        2021,
        2030,
        2102,
        2111,
        2120,
        2201,
        2210,
        2300,
        3002,
        3011,
        3020,
        3101,
        3110,
        3200,
        4001,
        4010,
        4100,
        5000,
    ]

    result = numbers_generator(4, 5, 5)
    assert result == expected


def test_numbers_generator_case_3():
    """testando para N = 4, SUM = 25, MAX_DIGIT = 6"""

    result = numbers_generator(4, 25, 6)
    assert [] == result


def test_numbers_generator_n_dig_equal_to_0_raises_value_error():
    """
    testando para N = 0, SUM = 25, MAX_DIGIT = 6
    raises ValueError Exception
    """

    with pytest.raises(ValueError) as exception_info:
        numbers_generator(0, 21, 6)
    assert "'n_dig' must be an integer equal to or greater than 1" in str(
        exception_info
    )


def test_numbers_generator_n_dig_equal_to_a_raises_value_error():
    """
    testando para N = 'a', SUM = 25, MAX_DIGIT = 6
    raises ValueError exception
    """

    with pytest.raises(ValueError) as exception_info:
        numbers_generator("a", 21, 6)
    assert "'n_dig' must be an integer equal to or greater than 1" in str(
        exception_info
    )


def test_numbers_generator_n_dig_equal_to_1_dot_1_raises_value_error():
    """
    testando para N = 1.1, SUM = 25, MAX_DIGIT = 6
    raises ValueError exception
    """

    with pytest.raises(ValueError) as exception_info:
        numbers_generator(1.1, 21, 6)
    assert "'n_dig' must be an integer equal to or greater than 1" in str(
        exception_info
    )


def test_numbers_generator_summation_equal_to_0_raises_value_error():
    """
    testando para N = 1, SUM = 0, MAX_DIGIT = 6
    raises ValueError Exception
    """

    with pytest.raises(ValueError) as exception_info:
        numbers_generator(1, 0, 6)
    assert "'summation' must be integer greater than 1" in str(exception_info)


def test_numbers_generator_summation_equal_to_a_raises_value_error():
    """
    testando para N = 1, SUM = 'a'', MAX_DIGIT = 6
    raises ValueError exception
    """

    with pytest.raises(ValueError) as exception_info:
        numbers_generator(1, "a", 6)
    assert "'summation' must be integer greater than 1" in str(exception_info)


def test_numbers_generator_summation_equal_to_1_dot_1_raises_value_error():
    """
    testando para N = 1, SUM = 1.1, MAX_DIGIT = 6
    raises ValueError exception
    """

    with pytest.raises(ValueError) as exception_info:
        numbers_generator(1, 1.1, 6)
    assert "'summation' must be integer greater than 1" in str(exception_info)


def test_numbers_generator_max_digit_equal_to_0_raises_value_error():
    """
    testando para N = 1, SUM = 25, MAX_DIGIT = 0
    raises ValueError Exception
    """

    with pytest.raises(ValueError) as exception_info:
        numbers_generator(1, 21, 0)
    assert "'max_digit' must be an integer between 1 and 9" in str(
        exception_info
    )


def test_numbers_generator_max_digit_equal_to_10_raises_value_error():
    """
    testando para N = 1, SUM = 25, MAX_DIGIT = 10
    raises ValueError Exception
    """

    with pytest.raises(ValueError) as exception_info:
        numbers_generator(1, 21, 10)
    assert "'max_digit' must be an integer between 1 and 9" in str(
        exception_info
    )


def test_numbers_generator_max_digit_equal_to_a_raises_value_error():
    """
    testando para N = 1, SUM = 25, MAX_DIGIT = 'a'
    raises ValueError Exception
    """

    with pytest.raises(ValueError) as exception_info:
        numbers_generator(1, 21, "a")
    assert "'max_digit' must be an integer between 1 and 9" in str(
        exception_info
    )


def test_numbers_generator_max_digit_equal_to_1_dot_1_raises_value_error():
    """
    testando para N = 1, SUM = 25, MAX_DIGIT = 1.1
    raises ValueError Exception
    """

    with pytest.raises(ValueError) as exception_info:
        numbers_generator(1, 21, 1.1)
    assert "'max_digit' must be an integer between 1 and 9" in str(
        exception_info
    )
