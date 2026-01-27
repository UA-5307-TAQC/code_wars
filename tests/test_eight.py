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


WILSON_DATA = [
    (0, False),
    (1, False),
    (5, True),
    (8, False),
    (9, False),
]


@pytest.mark.parametrize("input_data, expected_result", WILSON_DATA)
def test_willson_prime(eight_module, input_data, expected_result):
    """Test each students' am_i_wilson function."""
    if not hasattr(eight_module, "am_i_wilson"):
        pytest.skip(f"Student {eight_module.__name__} does not have am_i_wilson function.")
    assert eight_module.am_i_wilson(input_data) == expected_result
