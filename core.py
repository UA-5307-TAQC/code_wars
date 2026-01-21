"""Create decorator"""

TASKS = {}


def kata(name):
    """Decorator to sava functions in dictionary"""

    def wrapper(func):
        TASKS[name] = func
        return func

    return wrapper
