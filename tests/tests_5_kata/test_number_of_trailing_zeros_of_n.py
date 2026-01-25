"""
File: test_number_of_trailing_zeros_of_n.py
"""

import pytest

from tests.unique_loader import unique_loader


@pytest.mark.parametrize(
    "zeros",
    unique_loader("five", "zeros"),
)
def test_number_of_trailing_zeros_of_n(zeros):
    """Number of trailing zeros of N!."""
    if zeros is None:
        pytest.skip("Not implemented")
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7
    assert zeros(100) == 24
    assert zeros(1000) == 249
    assert zeros(100000) == 24999
    assert zeros(1000000000) == 249999998
