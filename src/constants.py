"""Reader runner for Kata Tasks."""

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
