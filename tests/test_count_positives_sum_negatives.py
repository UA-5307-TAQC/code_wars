"""Tests for count_positives_sum_negatives."""

import importlib
from pathlib import Path

import pytest


def load_functions():
    """Load functions for count_positives_sum_negatives."""
    base_path = Path("kata")
    funcs = []

    for author_dir in base_path.iterdir():
        if author_dir.is_dir():
            try:
                module = importlib.import_module(f"kata.{author_dir.name}.eight")
                funcs.append((author_dir.name, module.count_positives_sum_negatives))
            except (ModuleNotFoundError, AttributeError):
                continue
    return funcs


test_cases = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], [10, -65]),
    ([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14], [8, -50]),
    ([1], [1, 0]),
    ([-1], [0, -1]),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0]),
    ([], []),
]


@pytest.mark.parametrize("author, func", load_functions())
@pytest.mark.parametrize("arr, expected", test_cases)
def test_count_positives_sum_negatives(author, func, arr, expected):
    """Run tests for count_positives_sum_negatives."""
    result = func(arr)
    assert result == expected, f"Author {author} failed for input {arr}"
