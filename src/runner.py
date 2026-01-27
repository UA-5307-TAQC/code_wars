"""Runner of the exercise module."""

import importlib

from src.constants import EXERCISE_MAP
from src.files import Files


class Runner:  # pylint: disable=too-few-public-methods
    """Runner of the exercise."""

    @staticmethod
    def run_exercise(author, type_choice, function_name):
        """Run the exercise."""
        try:
            file_name = EXERCISE_MAP[type_choice]["file"]
            module_path = f"kata.{author}.{file_name}"
            module = importlib.import_module(module_path)
            func = getattr(module, function_name)
            params = Files.get_parameters(function_name)
            print("\nRunning function...\n")
            result = func(*params)
            if result is not None:
                print("Result:", result)
        except ModuleNotFoundError:
            print("Module does not exist.")
