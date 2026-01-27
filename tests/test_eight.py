"""Formatting decimal places tests."""

import pytest


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
