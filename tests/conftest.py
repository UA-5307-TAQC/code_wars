"""Pytest configuration file to create fixtures for kata modules."""

import importlib
import os
from typing import List, Literal, TypeAlias

import pytest

ModuleName: TypeAlias = Literal["five", "six", "seven", "eight"]


def get_module_paths(module: ModuleName) -> list[str]:
    """Create a list with module paths."""

    modules = []
    for package in os.listdir("kata"):
        if package not in ("__pycache__", "__init__.py"):
            modules.append(f"kata.{package}.{module}")
    return modules


def _create_module_fixture(module_name: ModuleName):
    """Create a fixture for the given module name."""

    @pytest.fixture(name=f"{module_name}_module", params=get_module_paths(module_name))
    def fixture(request):
        """Import the module."""
        try:
            module = importlib.import_module(request.param)
        except ModuleNotFoundError:
            pytest.skip(f"Module {request.param} not found.")
        return module

    return fixture


module_names: List[ModuleName] = ["five", "six", "seven", "eight"]
for mod_name in module_names:
    globals()[f"fixture_import_{mod_name}"] = _create_module_fixture(mod_name)
