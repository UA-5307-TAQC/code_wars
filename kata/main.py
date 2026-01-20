"""Kata main file. Running functions."""
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
            "divide_by"
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
        "functions": [
            "find_nb",
            "balance",
            "f",
            "rainfall",
            "nba_cup",
            "stock_list"
        ],
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
    "litres": [
        ("time", int)
    ],
    "get_volume_of_cuboid": [
        ("length", float),
        ("width", float),
        ("height", float),
    ],
    "converter": [("mpg", float)],
    "square_or_square_root": [("arr", float)],
    "count_positives_sum_negatives": [("arr", float)],
    "string_to_number": [("s", str)],
    "am_i_wilson": [("n", float)],
    "two_decimal_places": [("n", str)],
    "divisible_by": [("numbers", list), ("divisor", int)],
    "new_avg": [("arr", int), ("new_num", int)],
    "series_sum": [("n", int)],
    "find_nb": [("m", int)],
    "balance": [("book", str)],
    "f": [("x", int)],
    "rainfall": [("town", str), ("s", str)],
    "nba_cup": [("result_sheet", str), ("to_find", str)],
    "stock_list": [("stocklist", str), ("categories", list)],
    "gap": [("g", int), ("m", int), ("n", int)],
    "zeros": [("n", int)],
    "perimeter": [("n", int)],
    "solve": [("m", int)],
    "smallest": [("n", int)],
}


def get_authors():
    """Get authors list."""
    authors = ["denys_skovoronok", "hlib_shramko", "kekish", "kostiantyn_osypenko", "maxym_dvolinskyi", "tliubov",
               "valentyn_yehoian", "vitalinakliuieva"]
    return authors


def get_exercises(type_of_exercise):
    """Get exercises list."""
    if type_of_exercise == 1:
        return ["Keep Hydrated! exercise", "Volume of a Cuboid exercise",
                "Miles per gallon to kilometers per liter exercise", "To square(root) or not to square(root) exercise",
                "Count of positives / sum of negatives exercise", "Convert a String to a Number! exercise",
                "Wilson primes exercise", "Formatting decimal places exercise",
                "Find numbers which are divisible by given number exercise"]
    if type_of_exercise == 2:
        return ["Looking for a benefactor exercise", "Sum of the first nth term of Series exercise"]
    if type_of_exercise == 3:
        return ["Build a pile of Cubes exercise", "Easy Balance Checking exercise",
                "Floating-point Approximation  exercise", "Rainfall exercise", "Ranking NBA teams exercise",
                "Help the bookseller ! exercise"]
    if type_of_exercise == 4:
        return ["Gap in Primes exercise", "Number of trailing zeros of N! exercise",
                "Perimeter of squares in a rectangle", "Which x for that sum?", "Find the smallest"]
    return None


def get_parameters(func_name):
    params = FUNCTION_PARAMS.get(func_name, [])
    values = []

    for name, param_type in params:
        while True:
            try:
                raw = input(f"Enter {name} ({param_type.__name__}): ")
                value = param_type(raw)
                values.append(value)
                break
            except ValueError:
                print(f"Invalid {name}. Expected {param_type.__name__}.")

    return values


def choose_author():
    """Choose author."""
    authors = get_authors()
    print("Choose an author:\n")

    for index, author in enumerate(authors, 1):
        print(f"{index}. {author}")

    while True:
        try:
            choice = int(input("Enter corresponding number: "))
            if 1 <= choice <= len(authors):
                return authors[choice - 1]
            raise ValueError
        except ValueError:
            print("Please enter a valid number.")


def choose_file():
    """Choose a file of the exercise."""
    print("\nChoose category:")
    print("1. Eight\n2. Seven\n3. Six\n4. Five")

    while True:
        try:
            choice = int(input("Enter corresponding number: "))
            if choice in EXERCISE_MAP:
                return choice
            raise ValueError
        except ValueError:
            print("Invalid choice.")


def choose_function(type_choice):
    """Choose a function exercise."""
    functions = EXERCISE_MAP[type_choice]["functions"]

    print("\nChoose exercise:")
    for index, func in enumerate(functions, 1):
        print(f"{index}. {func}")

    while True:
        try:
            choice = int(input("Enter corresponding number: "))
            if 1 <= choice <= len(functions):
                return functions[choice - 1]
            raise ValueError
        except ValueError:
            print("Invalid choice.")


def run_exercise(author, type_choice, function_name):
    """Run the exercise."""
    file_name = EXERCISE_MAP[type_choice]["file"]
    module_path = f"kata.{author}.{file_name}"

    module = importlib.import_module(module_path)
    func = getattr(module, function_name)

    params = get_parameters(function_name)

    print("\nRunning function...\n")
    result = func(*params)

    if result is not None:
        print("Result:", result)


def main():
    """Main function."""
    author = choose_author()
    type_choice = choose_file()
    function_name = choose_function(type_choice)

    run_exercise(author, type_choice, function_name)


if __name__ == "__main__":
    main()
