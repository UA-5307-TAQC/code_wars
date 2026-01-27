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


VOLUME_OF_CUBOID = [
    (1, 2, 2, 4),
    (6.3, 2, 5, 63),
    (6.3, 2, 0, 0)
]

@pytest.mark.parametrize("input_length, input_width, input_height, expected_result", VOLUME_OF_CUBOID)
def test_get_volume_of_cuboid(eight_module, input_length, input_width, input_height, expected_result):
    """Test each students' get_volume_of_cuboid function."""
    if not hasattr(eight_module, "stock_list"):
        pytest.skip(f"Student {eight_module.__name__} does not have get_volume_of_cuboid function.")
    assert eight_module.get_volume_of_cuboid(input_length, input_width, input_height) == expected_result