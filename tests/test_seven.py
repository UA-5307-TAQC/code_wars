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
def test_series_num(seven_module, num: int, expected: str):
    """Test function."""
    result = seven_module.series_sum(num)
    assert result == expected, f"{num} is expected to be {expected}, not {result}"


@pytest.mark.parametrize(
    "arr, newavg, expected",
    [
        ([14, 30, 5, 7, 9, 11, 15], 92, 645),
        ([14, 30, 5, 7, 9, 11, 16], 90, 628),
        ([8, 6, 2, 12, 20, 5, 15], 10, 12),
        ([10, 4, 32, 2, 24, 23, 90], 100, 615),
        ([123, 20123, 30234, 4023, 23423, 2352, 3242], 16585, 49160),
    ],
)
def test_new_avg(seven_module, arr, newavg, expected):
    """Looking for a benefactor."""
    new_avg_result = seven_module.new_avg(arr, newavg)
    assert new_avg_result == expected, f"{new_avg_result} is expected to be {expected}"
