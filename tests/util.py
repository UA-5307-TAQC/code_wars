"""Utils for testing."""

import importlib

AUTHORS = (
    "denys_skovoronok",
    "denys_sidorov",
    "hlib_shramko",
    "kekish",
    "kostiantyn_osypenko",
    "maxym_dvolinskyi",
    "tliubov",
    "valentyn_yehoian",
    "vitalinakliuieva",
)


def get_function(author, level, func_name):
    """Get a function from certain author and level kyu."""
    module_path = f"kata.{author}.{level}"
    module = importlib.import_module(module_path)
    return getattr(module, func_name)
