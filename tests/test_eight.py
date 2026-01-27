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


# Count_positives_sum_negatives
@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], [10, -65]),
        ([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14], [8, -50]),
        ([1], [1, 0]),
        ([-1], [0, -1]),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0]),
        ([], []),
    ],
)
def test_count_positives_sum_negatives(eight_module, arr, expected):
    """Run tests for count_positives_sum_negatives."""

    result = eight_module.count_positives_sum_negatives(arr)
    assert result == expected, f"{result} is expected to be {expected}"
