"""Tests for solutions of eight kyu module."""

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
