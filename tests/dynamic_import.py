"""File to import all students and their files."""

import importlib.util
import os
import sys


def import_all_from_folder(path):
    """Import all students and their files."""
    imported_modules = {}

    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(".py") and filename != "__init__.py":
                filepath = os.path.join(dirpath, filename)

                relative_path = os.path.relpath(filepath, path)
                module_name = relative_path.replace(os.sep, "_").replace(".py", "")

                spec = importlib.util.spec_from_file_location(module_name, filepath)
                if spec and spec.loader:
                    module = importlib.util.module_from_spec(spec)
                    sys.modules[module_name] = module
                    spec.loader.exec_module(module)

                    imported_modules[module_name] = module
    return imported_modules
