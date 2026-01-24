"""File to test tasks."""

import os

import pytest

from dynamic_import import import_all_from_folder

# from src import files

# 1. Знаходимо, де фізично лежить цей файл (kata_test.py) на диску
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Склеюємо шлях до поточної папки + "kata"
# Тепер це буде щось типу "D:/projects/.../code_wars/kata"
kata_folder_path = os.path.join(current_dir, "kata")

modules = import_all_from_folder(kata_folder_path)
students = list(modules.values())

WILSON_DATA = [
    (0, False),
    (1, False),
    (5, True),
    (8, False),
    (9, False),
]

STOCKLIST_DATA = [
    (
        ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"],
        ["A", "B", "C", "W"],
        "(A : 20) - (B : 114) - (C : 50) - (W : 0)",
    ),
    (
        ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"],
        ["A", "B", "C", "D"],
        "(A : 0) - (B : 1290) - (C : 515) - (D : 600)",
    ),
    (["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"], ["A", "B"], "(A : 200) - (B : 1140)"),
    (
        ["CBART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"],
        ["A", "B", "C", "W"],
        "(A : 0) - (B : 114) - (C : 70) - (W : 0)",
    ),
    (
        ["ROXANNE 102", "RHODODE 123", "BKWRKAA 125", "BTSQZFG 239", "DRTYMKH 060"],
        ["B", "R", "D", "X"],
        "(B : 364) - (R : 225) - (D : 60) - (X : 0)",
    ),
    ([], ["A", "B", "Q", "W"], ""),
    (["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"], [], ""),
]

FILES_DATA = [
    (1, True),
    (2, True),
    (3, True),
    (4, True),
    (5, False),
    (0, False),
    ("", False),
]


@pytest.mark.parametrize("student", students)
@pytest.mark.parametrize("input_data, expected_result", WILSON_DATA)
def test_willson_prime(student, input_data, expected_result):
    """Test each students' am_i_wilson function."""
    if not hasattr(student, "am_i_wilson"):
        pytest.skip(f"Student {student.__name__} does not have am_i_wilson function.")

    assert student.am_i_wilson(input_data) == expected_result


@pytest.mark.parametrize("student", students)
@pytest.mark.parametrize("input_stocklist, input_categories, expected_result", STOCKLIST_DATA)
def test_stocklist(student, input_stocklist, input_categories, expected_result):
    """Test each students' stock_list function."""
    if not hasattr(student, "stock_list"):
        pytest.skip(f"Student {student.__name__} does not have stock_list function.")
    assert student.stock_list(input_stocklist, input_categories) == expected_result


# @pytest.mark.parametrize('file', files)
# @pytest.mark.parametrize('input_data, expected_result', FILES_DATA)
# def test_choose_function(file, input_data, expected_result):
#     assert file.Files.choose_function(input(input_data)) == expected_result
