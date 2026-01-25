"""Unit tests for to square or not to square problem."""

import pytest

from tests.util import AUTHORS, get_function

TEST_CASES = [
    ([4, 3, 9, 7, 2, 1], [2, 9, 3, 49, 4, 1]),
    ([100, 101, 5, 5, 1, 1], [10, 10201, 25, 25, 1, 1]),
    ([1, 2, 3, 4, 5, 6], [1, 4, 9, 2, 25, 36]),
    ([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], [1.0, 4.0, 9.0, 2.0, 25.0, 36.0]),
]


@pytest.mark.parametrize("author_name", AUTHORS)
@pytest.mark.parametrize("arr, expected", TEST_CASES)
def test_square_or_square_root(author_name, arr, expected):
    """Tests for square_or_square_root function of all authors."""
    square_func = get_function(author_name, "eight", "square_or_square_root")
    assert square_func(arr) == expected
