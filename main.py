"""Choose task"""

import ast
import importlib
import inspect
import os

from core import TASKS

PATH = "./kata/"


def show_authors(dictionary):
    """Display info about all authors"""

    authors_lsit = os.listdir(PATH)
    counter = 1
    print("Choose author:")

    for i in authors_lsit:
        print(f"{counter}.{i}")
        dictionary[counter] = i
        counter += 1

    print()
    return dictionary


def is_number(choice, length):
    """Check if it's possible convert value to int"""
    if not choice.isdigit():
        raise ValueError("Enter a number")

    if not 1 <= int(choice) <= length:
        raise ValueError("Wrong value")


def display_kata_levels(author):
    """User pick kata level"""

    author_path = os.path.join(PATH, author)
    files = [f for f in os.listdir(author_path) if f.endswith(".py")]

    display_instruction = [s[:-3].capitalize() for s in files]  # get file names and convert to kata levels

    for i, name in enumerate(display_instruction, start=1):
        print(f"{i}. {name}")

    while True:
        picked_kata = input("Choose kata: ")

        try:
            is_number(picked_kata, len(files))
        except ValueError as e:
            print(e)
            continue

        index = int(picked_kata)

        load_tasks(files[index - 1], f"kata.{author}")
        display_tasks()
        break


def load_tasks(kata_file, package):
    """Load tasks from file"""
    module_name = kata_file[:-3]
    importlib.import_module(f"{package}.{module_name}")


def run_task(func):
    """Get methods from loaded file"""

    sig = inspect.signature(func)
    params = sig.parameters

    values = []

    for name in params:
        while True:
            raw = input(f"Enter {name}: ")

            try:
                value = ast.literal_eval(raw)
                values.append(value)
                break
            except ValueError:
                print("Invalid value, try again")

    result = func(*values)
    print("Result:", result)


def display_tasks():
    """Choose task"""

    tasks = list(TASKS.items())

    print("Choose task:")
    for i, (name, _) in enumerate(tasks, start=1):
        print(f"{i}. {name}")

    while True:
        choice = input("Write number to pick task: ")

        try:
            is_number(choice, len(tasks))
        except ValueError as e:
            print(e)
            continue

        index = int(choice)

        _, task_func = tasks[index - 1]
        run_task(task_func)
        break


if __name__ == "__main__":

    print(
        """
    ***************************
    Welcome in program solution
    ***************************
    """
    )

    authors_dict = {}
    show_authors(authors_dict)

    while True:
        user_input = input("Write number to pick author: ")

        if user_input == "authors":
            show_authors(authors_dict)

        elif user_input.isdigit() and int(user_input) in authors_dict:
            display_kata_levels(authors_dict[int(user_input)])

        elif user_input == "q":
            break

        else:
            print("Wrong number, write authors if you forgot author list")

    print(
        """
    ******************
         FINISH
    ******************
    """
    )
