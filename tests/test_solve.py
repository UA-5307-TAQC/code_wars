"""Test twenty-first task from five kuy: Which x for that sum."""

import pytest

from tests.utils_for_tests import get_authors, import_authors_kuy_file


@pytest.mark.parametrize("author", get_authors())
@pytest.mark.parametrize(
    "num, expected",
    [
        (2, 0.5),
        (4, 0.6096117967977924),
        (5, 0.641742430504416),
        (6, 0.6666666666666666),
        (10, 0.7298437881283576),
        (100, 0.904875078027496),
        (10000, 0.9900498750007813),
    ],
)
def test_solve(author: str, num: float, expected: float):
    """Test function."""
    five = import_authors_kuy_file(author, "five")
    assert five.solve(num) == expected
