"""Tests for Files methods"""

from unittest.mock import patch

import pytest

from src.files import Files


# Files.get_parameters
@pytest.mark.parametrize(
    "func_name, inputs, expected",
    [("litres", ["5"], [5]), ("two_decimal_places", ["3.14"], ["3.14"]), ("new_avg", ["1", "5"], [1, 5])],
)
def test_get_parameters(func_name, inputs, expected):
    """Run tests for get_parameters"""

    with patch("builtins.input", side_effect=inputs):
        result = Files.get_parameters(func_name)
        assert result == expected, f"{result} is expected to be {expected}"
