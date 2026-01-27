"""Test the six.py module."""
import pytest

FIND_NB = [
    (4, -1),
    (16, -1),
    (4183059834009, 2022),
    (24723578342962, -1),
    (135440716410000 , 4824),
    (40539911473216, 3568)
]

@pytest.mark.parametrize("input_m, expected_result", FIND_NB)
def test_find_nb(six_module, input_m, expected_result):
    """Test each students' find_nb function."""
    if not hasattr(six_module, "find_nb"):
        pytest.skip(f"Student {six_module.__name__} does not have find_nb function.")
    assert six_module.find_nb(input_m) == expected_result