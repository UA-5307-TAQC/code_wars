"""Formatting decimal places tests."""

import pytest


@pytest.mark.parametrize(
    "num, expected",
    [
        (0, 0),
        (1, 0),
        (2, 1),
        (3, 1),
        (4, 2),
        (10, 5),
    ],
)
def test_liters(eight_module, num: int, expected: int):
    """Test function."""
    result = eight_module.litres(num)
    assert result == expected, f"{num} is expected to be {expected}, not {result}"


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
