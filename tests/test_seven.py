"""Formatting decimal places tests."""

import pytest


@pytest.mark.parametrize(
    "num, expected",
    [
        (1, "1.00"),
        (2, "1.25"),
        (3, "1.39"),
        (4, "1.49"),
        (5, "1.57"),
        (10, "1.81"),
        (69, "2.45"),
        (228, "2.85"),
        (322, "2.97"),
        (10**7, "6.42"),
    ],
)
def test_series_num(seven_module, num: int, expected: int):
    """Test function."""
    result = seven_module.series_sum(num)
    assert result == expected, f"{num} is expected to be {expected}, not {result}"
