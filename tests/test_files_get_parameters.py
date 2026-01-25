"""Test Files.get_parameters."""

from unittest.mock import patch

import pytest

# pylint: disable=import-error
from src.files import Files


@pytest.mark.parametrize(
    "func_name, inputs, expected",
    [
        ("sum_numbers", ["3", "5"], [3, 5]),
        ("concat_strings", ["hello", "world"], ["hello", "world"]),
    ],
)
def test_get_parameters(func_name, inputs, expected):
    """Test Files.get_parameters with mocked input and constants."""

    fake_params = {"sum_numbers": [("a", int), ("b", int)], "concat_strings": [("s1", str), ("s2", str)]}

    with patch("builtins.input", side_effect=inputs):
        with patch.dict("src.files.FUNCTION_PARAMS", fake_params):
            result = Files.get_parameters(func_name)

    assert result == expected
