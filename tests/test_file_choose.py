"""Files.choose_file test."""

import pytest

from src.files import Files


@pytest.fixture
def mocker_exercise_map(mocker):
    """Work before every test, where it was called."""
    mock_map = {1: {"functions": ["test_func_one", "test_func_two"]}}
    mocker.patch("src.files.EXERCISE_MAP", mock_map)
    return mock_map


@pytest.mark.usefixtures("mocker_exercise_map")
def test_choose_function(mocker):
    """Mock test valid inputs for function."""
    mocker.patch("builtins.input", return_value="1")
    result = Files.choose_function(1)
    assert result == "test_func_one"


@pytest.mark.usefixtures("mocker_exercise_map")
def test_choose_invalid_then_valid(mocker):
    """Mock test invalid inputs for function."""
    mocker.patch("builtins.input", side_effect=["99", "hi", "1"])
    result = Files.choose_function(1)
    assert result == "test_func_one"
