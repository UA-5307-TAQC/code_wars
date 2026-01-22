"""Files module."""

from src.constants import EXERCISE_MAP, FUNCTION_PARAMS


class Files:
    """Files."""

    @staticmethod
    def get_parameters(func_name):
        """Get parameters."""
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

    @staticmethod
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

    @staticmethod
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
