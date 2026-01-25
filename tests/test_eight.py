"""Formatting decimal places tests."""

import importlib
import os

import pytest


def get_module_paths():
    """Create a list with module paths."""

    modules = []
    for package in os.listdir("kata"):
        if package != "__pycache__":
            modules.append(f"kata.{package}.eight")
    return modules


@pytest.fixture(name="import_eight", params=get_module_paths())
def import_eighth_module(request):
    """Import the eighth module."""

    module = importlib.import_module(request.param)
    return module


@pytest.mark.parametrize(
    "value, expected",
    [
        (1.231, 1.23),
        (1.365, 1.36),
        (1.375, 1.38),
        (2.987, 2.99),
        (-1.987, -1.99),
        (-1.231, -1.23),
        (3, 3),
        (173735326.3783732637948948, 173735326.38),
        (1.99, 1.99),
    ],
)
def test_two_decimal_places(import_eight, value, expected):
    """Run tests."""

    result = import_eight.two_decimal_places(value)
    assert result == expected, f"{result} is expected to be {expected}"
