"""Unit tests for choose_author method from Authors class."""

import pytest

from src.authors import Authors

POSITIVE_TEST_CASES = [
    ("1", "denys_skovoronok"),
    ("2", "denys_sidorov"),
    ("3", "hlib_shramko"),
    ("4", "kekish"),
    ("5", "kostiantyn_osypenko"),
    ("6", "maxym_dvolinskyi"),
    ("7", "tliubov"),
    ("8", "valentyn_yehoian"),
    ("9", "vitalinakliuieva"),
]


NEGATIVE_TEST_CASES = [
    ("0", "Invalid choice. minimum is 1, maximum is 9"),
    ("-1", "Invalid choice. minimum is 1, maximum is 9"),
    ("10", "Invalid choice. minimum is 1, maximum is 9"),
    ("11", "Invalid choice. minimum is 1, maximum is 9"),
    ("abc", "Please enter a valid number."),
    ("$", "Please enter a valid number."),
    ("1.0", "Please enter a valid number."),
]


@pytest.mark.parametrize("value, expected", POSITIVE_TEST_CASES)
def test_positive_choose_author(monkeypatch, value, expected):
    """Positive tests for choose_author method."""
    monkeypatch.setattr("builtins.input", lambda _: value)
    assert Authors.choose_author() == expected


@pytest.mark.parametrize("value, expected", NEGATIVE_TEST_CASES)
def test_negative_choose_author(value, expected, monkeypatch, capsys):
    """Negative tests for choose_author method."""
    input_iterator = iter([value])
    monkeypatch.setattr("builtins.input", lambda _: next(input_iterator))

    with pytest.raises(StopIteration):
        Authors.choose_author()

    captured: str = capsys.readouterr().out
    last_captured_line = captured.splitlines()[-1]

    assert last_captured_line == expected
