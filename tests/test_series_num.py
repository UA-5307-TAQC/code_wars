"""Test eleventh task from seven kuy: Sum of the first nth term of Series."""

import pytest

from tests.utils_for_tests import get_authors, import_authors_kuy_file


@pytest.mark.parametrize("author", get_authors())
@pytest.mark.parametrize(
    "num, expected",
    [
        (1, "1.00"),
        (2, "1.25"),
        (3, "1.39"),
        (4, "1.49"),
        (5, "1.57"),
        (10, "1.81"),
        (69, "2.45"),
        (228, "2.85"),
        (322, "2.97"),
        (10**7, "6.42"),
    ],
)
def test_series_num(author: str, num: int, expected: str):
    """Test function."""
    seven = import_authors_kuy_file(author, "seven")
    assert seven.series_sum(num) == expected
