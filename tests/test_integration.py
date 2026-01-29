"""Integration tests for square_or_root_square and f functions in console app."""

import re

import pytest

from main import main

AUTHOR_INDEX = ("1", "2", "3", "4", "5", "6", "7", "8", "9")


@pytest.mark.parametrize("author_index", AUTHOR_INDEX)
@pytest.mark.parametrize(
    "arr, expected",
    [
        ([4, 3, 9, 7, 2, 1], [2, 9, 3, 49, 4, 1]),
        ([100, 101, 5, 5, 1, 1], [10, 10201, 25, 25, 1, 1]),
        ([1, 2, 3, 4, 5, 6], [1, 4, 9, 2, 25, 36]),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], [1.0, 4.0, 9.0, 2.0, 25.0, 36.0]),
    ],
)
def test_square_integration(monkeypatch, capsys, author_index, arr, expected):
    """Tests for square_or_square_root function of all authors in console app."""
    input_values = iter([author_index, "1", "4", str(arr)])
    monkeypatch.setattr("builtins.input", lambda _: next(input_values))

    with pytest.raises(StopIteration):
        main()

    captured: str = capsys.readouterr().out
    assert str(expected) in captured


@pytest.mark.parametrize("author_index", AUTHOR_INDEX)
@pytest.mark.parametrize(
    "x, expected",
    [
        (2.6e-08, 1.29999999155e-08),
        (1.4e-09, 6.999999997549999e-10),
        (5.0e-06, 2.499996875007812e-06),
        (2.4e-07, 1.1999999280000085e-07),
        (2.1e-11, 1.0499999999944874e-11),
        (0.00017, 8.499638780702988e-05),
        (1.9e-07, 9.499999548750044e-08),
        (1.8e-08, 8.999999959500001e-09),
        (4.2e-08, 2.0999999779500002e-08),
        (7.0e-05, 3.499938752143656e-05),
    ],
)
def test_f_integration(monkeypatch, capsys, author_index, x, expected):
    """Tests for f function of all authors in console app."""
    input_values = iter([author_index, "3", "3", str(x)])
    monkeypatch.setattr("builtins.input", lambda _: next(input_values))

    with pytest.raises(StopIteration):
        main()

    captured: str = capsys.readouterr().out
    match = re.search(r"Result: ([\d\.eE\-\+]+)", captured)
    assert match is not None

    result_str = match.group(1)
    assert float(result_str) == pytest.approx(expected, rel=1e-12)
