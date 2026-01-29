import pytest
import importlib
from pathlib import Path


def get_all_functions(MODULE_NAME, FUNCTION_NAME):
    KATA_DIR = Path(__file__).parents[1] / "kata"
    cases = []

    for dev_dir in KATA_DIR.iterdir():
        if not dev_dir.is_dir():
            continue

        module_path = f"kata.{dev_dir.name}.{MODULE_NAME}"

        try:
            module = importlib.import_module(module_path)
        except ImportError:
            cases.append(
                pytest.param(
                    dev_dir.name,
                    None,
                    marks=pytest.mark.xfail(reason="module not found"),
                )
            )
            continue

        if not hasattr(module, FUNCTION_NAME):
            cases.append(
                pytest.param(
                    dev_dir.name,
                    None,
                    marks=pytest.mark.xfail(reason="function not found"),
                )
            )
            continue

        cases.append((dev_dir.name, getattr(module, FUNCTION_NAME)))

    return cases

def get_one_function(MODULE_NAME, CLASS_NAME, FUNCTION_NAME):
    module_path = f"src.{MODULE_NAME}"

    try:
        module = importlib.import_module(module_path)
    except ImportError:
        return [
            pytest.param(
                None,
                marks=pytest.mark.xfail(reason="module not found"),
            )
        ]

    if not hasattr(module, CLASS_NAME):
        return [
            pytest.param(
                None,
                marks=pytest.mark.xfail(reason="class not found"),
            )
        ]

    cls = getattr(module, CLASS_NAME)

    if not hasattr(cls, FUNCTION_NAME):
        return [
            pytest.param(
                None,
                marks=pytest.mark.xfail(reason="function not found"),
            )
        ]

    return [(getattr(cls, FUNCTION_NAME))]


@pytest.mark.parametrize(
    "developer, function",
    get_all_functions("eight", "string_to_number"),
    ids=lambda x: x if isinstance(x, str) else None
)

def test_string_to_number(developer, function):
    assert function("27") == 27
    assert function("-1") == -1
    with pytest.raises(ValueError):
        function("abc")

@pytest.mark.parametrize(
    "developer, function",
    get_all_functions("six", "nba_cup"),
    ids=lambda x: x if isinstance(x, str) else None
)

def test_nba_cup(developer, function):
    assert function("Los Angeles Clippers 104 Dallas Mavericks 88,New York Knicks 101 Atlanta Hawks 112,Indiana Pacers 103 Memphis Grizzlies 112,  Los Angeles Clippers 100 Boston Celtics 120", "Los Angeles Clippers") == "Los Angeles Clippers:W=1;D=0;L=1;Scored=204;Conceded=208;Points=3"
    assert function(
        "Los Angeles Clippers 104 Dallas Mavericks 88,New York Knicks 101 Atlanta Hawks 112,Indiana Pacers 103 Memphis Grizzlies 112,  Los Angeles Clippers 100 Boston Celtics 120",
        "") == ""
    assert function(
        "Los Angeles Clippers 104 Dallas Mavericks 88,New York Knicks 101 Atlanta Hawks 112,Indiana Pacers 103 Memphis Grizzlies 112,  Los Angeles Clippers 100 Boston Celtics 120",
        "Boston Celt") == "Boston Celt:This team didn't play!"

@pytest.mark.parametrize(
    "function",
    get_one_function("files", "Files", "choose_file"),
)

def test_choose_file(function, monkeypatch):
    inputs = iter(["abc", "9", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert function() == 2