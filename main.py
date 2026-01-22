"""Kata main file. Main function."""

from src.authors import Authors
from src.files import Files
from src.runner import Runner


def main():
    """Main function."""
    while True:
        author = Authors.choose_author()
        type_choice = Files.choose_file()
        function_name = Files.choose_function(type_choice)

        Runner.run_exercise(author, type_choice, function_name)


if __name__ == "__main__":
    main()
