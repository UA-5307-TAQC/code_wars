"""Module to run each author's tasks."""

import importlib.util
import inspect
import json
from pathlib import Path

BASE_DIR = Path("./kata")


def get_authors():
    """Get a list of all authors."""
    return [a.name for a in BASE_DIR.iterdir()]


def get_tasks(author):
    """Get a list of all tasks for a given author."""
    author_path = BASE_DIR / author
    module_files = list(author_path.glob("*.py"))

    all_tasks = {}
    for file_path in module_files:
        module_name = file_path.stem
        menu_name = ""

        try:
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            for name, func in inspect.getmembers(module, inspect.isfunction):
                if not name.startswith("_") and func.__module__ == module.__name__:
                    if func.__doc__:
                        menu_name = func.__doc__.rstrip()
                    else:
                        menu_name = func.__name__.replace("_", " ").capitalize()

                all_tasks[menu_name] = func

        except Exception as e:  # pylint: disable=broad-exception-caught
            print(f"Some problem with {file_path.name}: {e}")

    return all_tasks


def run_function_smartly(func):
    """Get data for required amount of arguments for the function."""
    sig = inspect.signature(func)  # Inspect how many arguments does the function take
    args_values = []

    for param_name, param in sig.parameters.items():
        param_type = param.annotation

        if param_type == inspect.Parameter.empty:
            param_type = str

        while True:
            try:
                user_input = input(f"Enter the {param_name} ({param_type.__name__}): ")

                converted_value = None

                if param_type == int:
                    converted_value = int(user_input)
                elif param_type == float:
                    converted_value = float(user_input)
                elif param_type == bool:
                    converted_value = user_input.lower() in ["true", "1", "t", "y", "yes"]

                elif param_type in (list, dict):
                    converted_value = json.loads(user_input)
                    if not isinstance(converted_value, param_type):
                        raise ValueError(f"It is not {param_type.__name__}")

                else:
                    converted_value = user_input

                args_values.append(converted_value)
                break
            except ValueError:
                print(f"Error! Expected type {param_type.__name__}. Please try again.\n ")

    print("-" * 20)
    try:
        result = func(*args_values)
        print(f"Result: {result}")
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"Some problem with {func.__name__}: {e}")


def main():
    """Main function."""
    print("-" * 10 + "Kata tasks" + "-" * 10)

    authors = get_authors()

    while True:
        for id_a, name in enumerate(authors, 1):
            print(f"{id_a}. {name}")
        print("9. Exit")

        author_choice = input("Enter your choice(1-9): ")

        if author_choice == "9":
            break

        try:
            selected_author = authors[int(author_choice) - 1]

        except (IndexError, ValueError):
            print("Invalid choice. Please try again.\n")
            continue

        while True:
            tasks_dict = get_tasks(selected_author)

            if not tasks_dict:
                print("This author don't have any tasks yet!")
                input("Press any key to continue...")
                continue

            print("-" * 10 + selected_author + "'s tasks" + "-" * 10)

            list_tasks = list(tasks_dict.items())

            for idt, (name, _) in enumerate(list_tasks, 1):
                print(f"{idt}. {name}")
            print("b. back")

            task_choice = input("Enter your choice of task: ")

            if task_choice == "b":
                break

            try:
                choice_idt = int(task_choice) - 1
                if 0 <= choice_idt < len(list_tasks):
                    task_name, task_func = list_tasks[choice_idt]
                    print(f"{task_name}.....")
                    try:
                        run_function_smartly(task_func)
                    except Exception as e:  # pylint: disable=broad-exception-caught
                        print(f"file problem: {e}")
                    input("Press any key to continue...")
                else:
                    print("Invalid choice. Please try again.\n")
            except ValueError:
                print("Invalid input. Please try again.\n")


if __name__ == "__main__":
    main()
