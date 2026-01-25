"""Pre test element"""

import importlib

import pytest

from src.authors import Authors


def unique_loader(module_name: str, function_name: str):
    """Function for dynamic import all authors from named module."""
    cases = []

    for author in Authors.get_authors():
        module_path = f"kata.{author}.{module_name}"

        try:
            module = importlib.import_module(module_path)
            func = getattr(module, function_name)
            cases.append(pytest.param(func, id=author))

        except ModuleNotFoundError:
            cases.append(
                pytest.param(
                    None,
                    id=author,
                    marks=pytest.mark.xfail(reason="missing module"),
                )
            )

        except AttributeError:
            cases.append(
                pytest.param(
                    None,
                    id=author,
                    marks=pytest.mark.xfail(reason="missing function"),
                )
            )

    return cases
