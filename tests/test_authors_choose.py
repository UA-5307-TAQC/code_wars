"""Tests for choose_author method from Authors class."""

import pytest

from src.authors import Authors


@pytest.mark.parametrize(
    "value, expected",
    [
        ("1", "denys_skovoronok"),
        ("2", "denys_sidorov"),
        ("3", "hlib_shramko"),
        ("4", "kekish"),
        ("5", "kostiantyn_osypenko"),
        ("6", "maxym_dvolinskyi"),
        ("7", "tliubov"),
        ("8", "valentyn_yehoian"),
        ("9", "vitalinakliuieva"),
    ],
)
def test_choose_author_positive(monkeypatch, value, expected):
    """Positive test cases for choose_author method."""
    monkeypatch.setattr("builtins.input", lambda _: value)
    assert Authors.choose_author() == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("0", "Invalid choice. minimum is 1, maximum is 10"),
        ("-1", "Invalid choice. minimum is 1, maximum is 10"),
        ("11", "Invalid choice. minimum is 1, maximum is 10"),
        ("abc", "Please enter a valid number."),
        ("$", "Please enter a valid number."),
        ("1.0", "Please enter a valid number."),
    ],
)
def test_choose_author_negative(monkeypatch, capsys, value, expected):
    """Negative test cases for choose_author method."""
    input_iter = iter([value])
    monkeypatch.setattr("builtins.input", lambda _: next(input_iter))

    with pytest.raises(StopIteration):
        Authors.choose_author()

    captured: str = capsys.readouterr().out
    assert expected in captured
