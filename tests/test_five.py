"""Gap in primes tests."""

import pytest

FIND_THE_SMALLEST = [
    (261235, [126235, 2, 0]),
    (209917, [29917, 0, 1]),
    (285365, [238565, 3, 1])
]

@pytest.mark.parametrize(
    "gap, start, end, expected",
    [
        (2, 100, 110, [101, 103]),
        (4, 100, 110, [103, 107]),
        (6, 100, 110, None),
        (8, 300, 400, [359, 367]),
        (10, 300, 400, [337, 347]),
        (2, 100, 103, [101, 103]),
    ],
)
def test_gap(five_module, gap, start, end, expected):
    """Run tests."""

    result = five_module.gap(gap, start, end)
    assert result == expected, f"{gap}, {start}, {end} is expected to be {expected}"


@pytest.mark.parametrize("input_n, expected_result", FIND_THE_SMALLEST)
def test_smallest(five_module, input_n, expected_result):
    """Test each students' smallest function."""
    if not hasattr(five_module, "smallest"):
        pytest.skip(f"Student {five_module.__name__} does not have smallest function.")
    assert five_module.smallest(input_n) == expected_result

@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 0),
        (6, 1),
        (30, 7),
        (100, 24),
        (1000, 249),
        (100000, 24999),
        (1000000000, 249999998),
    ],
)
def test_number_of_trailing_zeros_of_n(five_module, value, expected):
    """Number of trailing zeros of N!."""

    result = five_module.zeros(value)
    assert result == expected, f" {value} is expected to be {expected}"
