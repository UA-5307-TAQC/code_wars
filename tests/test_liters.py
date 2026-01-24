"""Test first eight kuy task: Keep hydrated."""

import pytest

from tests.utils_for_tests import get_authors, import_authors_kuy_file


@pytest.mark.parametrize("author", get_authors())
@pytest.mark.parametrize(
    "num, expected",
    [
        (0, 0),
        (1, 0),
        (2, 1),
        (3, 1),
        (4, 2),
        (10, 5),
    ],
)
def test_liters(author: str, num: int, expected: int):
    """Test function."""
    eight = import_authors_kuy_file(author, "eight")
    assert eight.litres(num) == expected
