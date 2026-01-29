"""Tests for solutions of eight kyu module."""

import pytest

WILSON_DATA = [
    (0, False),
    (1, False),
    (5, True),
    (8, False),
    (9, False),
]


VOLUME_OF_CUBOID = [(1, 2, 2, 4), (6.3, 2, 5, 63), (6.3, 2, 0, 0)]


@pytest.mark.parametrize(
    "value, expected",
    [
        (1.231, 1.23),
        (1.365, 1.36),
        (1.375, 1.38),
        (2.987, 2.99),
        (-1.987, -1.99),
        (-1.231, -1.23),
        (3, 3),
        (173735326.3783732637948948, 173735326.38),
        (1.99, 1.99),
    ],
)
def test_two_decimal_places(eight_module, value, expected):
    """Run tests."""

    result = eight_module.two_decimal_places(value)
    assert result == expected, f"{result} is expected to be {expected}"


@pytest.mark.parametrize(
    "numbers, divisor, expected",
    [
        ([1, 2, 3, 4, 5, 6], 2, [2, 4, 6]),
        ([1, 2, 3, 4, 5, 6], 3, [3, 6]),
        ([0, 1, 2, 3, 4, 5, 6], 4, [0, 4]),
        ([0], 4, [0]),
        ([1, 3, 5], 2, []),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ],
)
def test_divisible_by(eight_module, numbers, divisor, expected):
    """Find numbers which are divisible by given number."""

    result = eight_module.divisible_by(numbers, divisor)
    assert result == expected, f"{result} is expected to be {expected}"


@pytest.mark.parametrize("input_data, expected_result", WILSON_DATA)
def test_wilson_prime(eight_module, input_data, expected_result):
    """Test each students' am_i_wilson function."""
    if not hasattr(eight_module, "am_i_wilson"):
        pytest.skip(f"Student {eight_module.__name__} does not have am_i_wilson function.")
    assert eight_module.am_i_wilson(input_data) == expected_result


@pytest.mark.parametrize(
    "mpg, expected",
    [
        (10, 3.54),
        (20, 7.08),
        (30, 10.62),
        (0, 0.00),
        (1, 0.35),
    ],
)
def test_converter(eight_module, mpg, expected):
    """Miles per gallon to kilometers per liter."""

    result = eight_module.converter(mpg)
    assert result == expected, f"{result} is expected to be {expected}"


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([4, 3, 9, 7, 2, 1], [2, 9, 3, 49, 4, 1]),
        ([100, 101, 5, 5, 1, 1], [10, 10201, 25, 25, 1, 1]),
        ([1, 2, 3, 4, 5, 6], [1, 4, 9, 2, 25, 36]),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], [1.0, 4.0, 9.0, 2.0, 25.0, 36.0]),
    ],
)
def test_square_or_square_root(eight_module, arr, expected):
    """Tests for square_or_square_root function of all authors."""
    square_result = eight_module.square_or_square_root(arr)
    assert square_result == expected, f"{square_result} is expected to be {expected}"
