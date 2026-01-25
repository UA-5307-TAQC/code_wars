"""Tests for find_the_smallest"""

import pytest

from tests.unique_loader import unique_loader


@pytest.mark.parametrize(
    "divisible_by",
    unique_loader("eight", "divisible_by"),
)
def test_divisible_by(divisible_by):
    """Find numbers which are divisible by given number."""
    if divisible_by is None:
        pytest.skip("Not implemented")
    assert divisible_by([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]
    assert divisible_by([1, 2, 3, 4, 5, 6], 3) == [3, 6]
    assert divisible_by([0, 1, 2, 3, 4, 5, 6], 4), [0, 4]
    assert divisible_by([0], 4) == [0]
    assert divisible_by([1, 3, 5], 2) == []
    assert divisible_by([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
