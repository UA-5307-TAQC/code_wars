"""Runner.run_exercise tests."""

from unittest.mock import Mock, patch
from src.runner import Runner
from src.constants import EXERCISE_MAP


@patch("src.runner.importlib.import_module")
@patch("src.runner.Files.get_parameters")
@patch.dict(EXERCISE_MAP, {1: {"file": "fake_module"}}, clear=True)
def test_run_exercise_success(mock_get_parameters, mock_import, capsys):
    """Check that run_exercise prints the correct result."""

    mock_module = Mock()
    fake_func = Mock(return_value=[5, 7])
    setattr(mock_module, "fake_func", fake_func)
    mock_import.return_value = mock_module
    mock_get_parameters.return_value = [2, 5, 7]

    Runner.run_exercise("someone", 1, "fake_func")

    captured = capsys.readouterr()
    assert "Running function..." in captured.out
    assert "Result: [5, 7]" in captured.out


@patch("src.runner.importlib.import_module")
def test_run_exercise_module_not_found(mock_import, capsys):
    """Check that run_exercise prints the correct error message."""

    mock_import.side_effect = ModuleNotFoundError

    Runner.run_exercise("someone", 1, "fake_func")

    captured = capsys.readouterr()
    assert "Module does not exist." in captured.out
