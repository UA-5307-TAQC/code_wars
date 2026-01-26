"""Integration tests for functions in console app."""

import re

import pytest

from main import main
from tests.test_floating import TEST_CASES as F_TEST_CASES
from tests.test_square import TEST_CASES as SQUARE_TEST_CASES

AUTHOR_INDEX = ("1", "2", "3", "4", "5", "6", "7", "8", "9")


@pytest.mark.parametrize("author_index", AUTHOR_INDEX)
@pytest.mark.parametrize("arr, expected", SQUARE_TEST_CASES)
def test_square_integration(author_index, arr, expected, monkeypatch, capsys):
    """Tests for square_or_square_root function of all authors in console app."""
    input_values_iter = iter([author_index, "1", "4", str(arr)])
    monkeypatch.setattr("builtins.input", lambda _: next(input_values_iter))

    with pytest.raises(StopIteration):
        main()

    captured: str = capsys.readouterr().out
    assert str(expected) in captured


@pytest.mark.parametrize("author_index", AUTHOR_INDEX)
@pytest.mark.parametrize("x, expected", F_TEST_CASES)
def test_f_integration(author_index, x, expected, monkeypatch, capsys):
    """Tests for f function of all authors in console app."""
    input_values_iter = iter([author_index, "3", "3", str(x)])

    monkeypatch.setattr("builtins.input", lambda _: next(input_values_iter))

    with pytest.raises(StopIteration):
        main()

    captured: str = capsys.readouterr().out

    match = re.search(r"Result: ([\d\.eE\-\+]+)", captured)
    assert match is not None, f"Result is not found {captured}"

    result_str = match.group(1)
    assert float(result_str) == pytest.approx(expected, rel=1e-12)
