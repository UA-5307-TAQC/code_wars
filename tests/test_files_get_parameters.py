"""Tests for Files methods"""

from unittest.mock import patch

import pytest

from src.files import Files


# Files.get_parameters
@pytest.mark.parametrize(
    "func_name, inputs, expected",
    [("litres", ["5"], [5]), ("two_decimal_places", ["3.14"], [3.14]), ("new_avg", ["1", "5"], [1, 5])],
)
def test_get_parameters(func_name, inputs, expected):
    """Run tests for get_parameters"""

    with patch("builtins.input", side_effect=inputs):
        result = Files.get_parameters(func_name)
        assert result == expected, f"{result} is expected to be {expected}"


@pytest.mark.parametrize(
    "func_name, inputs, expected",
    [
        ("litres", ["5"], [5]),
        ("get_volume_of_cuboid", ["1", "2", "2"], [1, 2, 2]),
        ("converter", ["10"], [10]),
        ("square_or_square_root", ["[4, 3, 9, 7, 2, 1]"], [[4, 3, 9, 7, 2, 1]]),
        (
            "count_positives_sum_negatives",
            ["[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]"],
            [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]],
        ),
        ("string_to_number", ["1234"], ["1234"]),
        ("am_i_wilson", ["0"], [0]),
        ("two_decimal_places", ["4.659725356"], [4.659725356]),
        ("divisible_by", ["[1, 2, 3, 4, 5, 6]", "2"], [[1, 2, 3, 4, 5, 6], 2]),
    ],
)
def test_get_parameters_8_kyu_positive(monkeypatch, func_name, inputs, expected):
    """Test cases for the get_parameters method based on 8 kyu functions."""
    inputs_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs_iter))
    assert Files.get_parameters(func_name) == expected
