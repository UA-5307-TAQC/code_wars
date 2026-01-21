"""Kata main file. Main function."""
import kata.reader_runner


def main():
    """Main function."""
    while True:
        author = kata.reader_runner.Authors.choose_author()
        type_choice = kata.reader_runner.Files.choose_file()
        function_name = kata.reader_runner.Files.choose_function(type_choice)

        kata.reader_runner.Runner.run_exercise(author, type_choice, function_name)


if __name__ == "__main__":
    main()
