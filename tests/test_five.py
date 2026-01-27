"""Gap in primes tests."""

import importlib
import os

import pytest


def get_module_paths(module: str = "five"):
    """Create a list with module paths."""

    modules = []
    for package in os.listdir("kata"):
        if package != "__pycache__":
            modules.append(f"kata.{package}.{module}")
    return modules


@pytest.fixture(name="import_five", params=get_module_paths())
def import_fifth_module(request):
    """Import the fifth module."""

    module = importlib.import_module(request.param)
    return module


@pytest.mark.parametrize(
    "gap, start, end, expected",
    [
        (2, 100, 110, [101, 103]),
        (4, 100, 110, [103, 107]),
        (6, 100, 110, None),
        (8, 300, 400, [359, 367]),
        (10, 300, 400, [337, 347]),
        (2, 100, 103, [101, 103]),
    ],
)
def test_gap(import_five, gap, start, end, expected):
    """Run tests."""

    result = import_five.gap(gap, start, end)
    assert result == expected, f"{gap}, {start}, {end} is expected to be {expected}"
