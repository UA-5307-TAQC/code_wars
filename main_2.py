"""Classes to get tasks and their work from kata for each author."""

import ast
import importlib

EXERCISE_MAP: dict[int, dict[str, str | list[str]]] = {
    1: {  # Eight
        "file": "eight",
        "functions": [
            "litres",
            "get_volume_of_cuboid",
            "converter",
            "square_or_square_root",
            "count_positives_sum_negatives",
            "string_to_number",
            "am_i_wilson",
            "two_decimal_places",
            "divide_by",
        ],
    },
    2: {  # Seven
        "file": "seven",
        "functions": [
            "new_avg",
            "series_sum",
        ],
    },
    3: {  # Six
        "file": "six",
        "functions": ["find_nb", "balance", "f", "rainfall", "nba_cup", "stock_list"],
    },
    4: {  # Five
        "file": "five",
        "functions": [
            "gap",
            "zeros",
            "perimeter",
            "solve",
            "smallest",
        ],
    },
}

FUNCTION_PARAMS = {
    "litres": [("time", int)],
    "get_volume_of_cuboid": [
        ("length", float),
        ("width", float),
        ("height", float),
    ],
    "converter": [("mpg", float)],
    "square_or_square_root": [("arr", list)],
    "count_positives_sum_negatives": [("arr", list)],
    "string_to_number": [("s", str)],
    "am_i_wilson": [("n", float)],
    "two_decimal_places": [("n", str)],
    "divisible_by": [("numbers", list), ("divisor", int)],
    "divide_by": [("numbers", list), ("divisor", int)],
    "new_avg": [("arr", list), ("new_num", int)],
    "series_sum": [("n", int)],
    "find_nb": [("m", int)],
    "balance": [("book", str)],
    "f": [("x", int)],
    "rainfall": [("town", str), ("s", str)],
    "nba_cup": [("result_sheet", str), ("to_find", str)],
    "stock_list": [("stocklist", list), ("categories", list)],
    "gap": [("g", int), ("m", int), ("n", int)],
    "zeros": [("n", int)],
    "perimeter": [("n", int)],
    "solve": [("m", float)],
    "smallest": [("n", int)],
}


class Authors:
    """Get an author's info."""

    def __init__(self):
        self.authors = self.load_authors()

    def load_authors(self):
        """Returns the hardcoded list of authors."""
        return [
            "denys_skovoronok",
            "hlib_shramko",
            "kekish",
            "kostiantyn_osypenko",
            "maxym_dvolinskyi",
            "tliubov",
            "valentyn_yehoian",
            "vitalinakliuieva",
        ]

    def show_authors(self):
        """Show all authors."""
        print("\n--- Authors List ---")
        for aid, ath in enumerate(self.authors, 1):
            print(f"{aid}. {ath}")
        print("9. Exit")

    def choose_author(self):
        """User chooses a author."""
        self.show_authors()

        while True:
            author_choice = input("\nChoose an author(1-9): ")

            if author_choice == "9":
                return None

            try:
                choice_idx = int(author_choice) - 1
                if 0 <= choice_idx < len(self.authors):
                    return self.authors[choice_idx]
                print(f"Invalid choice. Choose an author (1-{len(self.authors)}).")
            except ValueError:
                print("!Invalid input! Please enter number.")


class Tasks:
    """Get a list of tasks for a given author."""

    def __init__(self, author):
        self.author = author
        self.all_tasks = self._collect_all_tasks()

    def _collect_all_tasks(self):
        """Get all functions in one list."""
        tasks_list = []
        for cat_data in EXERCISE_MAP.values():
            file_name = cat_data["file"]
            for func_name in cat_data["functions"]:
                tasks_list.append((func_name, file_name))
        return tasks_list

    def show_tasks(self):
        """Shaw all tasks for that author."""
        print(f"\n--- All Tasks for {self.author} ---")
        for idx, (func_name, file_name) in enumerate(self.all_tasks, 1):
            print(f"{idx}. {func_name} (from {file_name})")
        print("b. Back")

    def choose_task(self):
        """User chooses a task directly."""
        self.show_tasks()

        while True:
            choice = input(f"Choose task (1-{len(self.all_tasks)}): ")

            if choice.lower() == "b":
                return None

            try:
                idx = int(choice) - 1
                if 0 <= idx < len(self.all_tasks):
                    return self.all_tasks[idx]
                print("Invalid number.")
            except ValueError:
                print("Invalid input.")

    def _parse_input(self, raw_input, param_type):
        """
        Helper method to parse input string into correct type.
        This fixes R1702 (Too many nested blocks).
        """
        if param_type == list:
            # ast.literal_eval raises ValueError or SyntaxError
            value = ast.literal_eval(raw_input)
            if not isinstance(value, list):
                raise ValueError("Not a list")
            return value

        if param_type == bool:
            return raw_input.lower() in ("true", "1", "yes", "y")

        if param_type == str:
            return raw_input.replace("\\n", "\n")

        return param_type(raw_input)

    def get_parameters(self, func_name):
        """Asks user for input based on types defined in FUNCTION_PARAMS."""
        params_config = FUNCTION_PARAMS.get(func_name, [])
        values = []

        if not params_config:
            print(f"Warning: No parameters defined for '{func_name}'.")
            return []

        print(f"\nInput parameters for '{func_name}':")
        for name, param_type in params_config:
            while True:
                try:
                    raw = input(f"Enter {name} ({param_type.__name__}): ")
                    value = self._parse_input(raw, param_type)
                    values.append(value)
                    break
                except (ValueError, SyntaxError):
                    print(f"Invalid value for {name}. " f"Expected {param_type.__name__} (Lists: [1, 2]).")

        return values

    def run_task(self, func_name, file_name):
        """Imports and runs the task."""
        module_path = f"kata.{self.author}.{file_name}"

        try:
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)

            params = self.get_parameters(func_name)

            print(f"\nRunning {func_name}...")
            result = func(*params)
            print(f"Result: {result}")
            input("\nPress Enter to continue...")

        except ModuleNotFoundError:
            print(f"Error: File '{file_name}.py' not found for author '{self.author}'.")
        except AttributeError:
            print(f"Error: Function '{func_name}' not found in '{file_name}.py'.")
        # pylint: disable=broad-exception-caught
        except Exception as e:
            print(f"Error executing: {e}")


def main():
    """Main function."""
    print("-" * 10, "Each author's kata tasks", "-" * 10)
    author_manager = Authors()

    while True:
        selected_author = author_manager.choose_author()

        if not selected_author:
            print("Exiting...")
            break

        task_manager = Tasks(selected_author)

        while True:
            print("\n")
            print("-" * 10, selected_author + "'s tasks", "-" * 10)

            selected_task = task_manager.choose_task()

            if not selected_task:
                print("Going back to authors...")
                break

            func_name, file_name = selected_task
            task_manager.run_task(func_name, file_name)


if __name__ == "__main__":
    main()
