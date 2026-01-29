"""Test the six.py module."""

import pytest

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


@pytest.mark.parametrize(
    "book, expected",
    [
        (
            """1000.00
125 Market 125.45
126 Hardware 34.95
127 Video 7.45
128 Book 14.32
129 Gasoline 16.10
""",
            "Original Balance: 1000.00\r\n"
            "125 Market 125.45 Balance 874.55\r\n"
            "126 Hardware 34.95 Balance 839.60\r\n"
            "127 Video 7.45 Balance 832.15\r\n"
            "128 Book 14.32 Balance 817.83\r\n"
            "129 Gasoline 16.10 Balance 801.73\r\n"
            "Total expense  198.27\r\n"
            "Average expense  39.65",
        ),
    ],
)
def test_balance(six_module, book, expected):
    """Run tests."""

    result = six_module.balance(book)
    assert result == expected, f"{result} is expected to be {expected}"


FIND_NB = [
    (4, -1),
    (16, -1),
    (4183059834009, 2022),
    (24723578342962, -1),
    (135440716410000, 4824),
    (40539911473216, 3568),
]


@pytest.mark.parametrize("input_stocklist, input_categories, expected_result", STOCKLIST_DATA)
def test_stocklist(six_module, input_stocklist, input_categories, expected_result):
    """Test each students' stock_list function."""
    if not hasattr(six_module, "stock_list"):
        pytest.skip(f"Student {six_module.__name__} does not have stock_list function.")
    assert six_module.stock_list(input_stocklist, input_categories) == expected_result


@pytest.mark.parametrize("input_m, expected_result", FIND_NB)
def test_find_nb(six_module, input_m, expected_result):
    """Test each students' find_nb function."""
    if not hasattr(six_module, "find_nb"):
        pytest.skip(f"Student {six_module.__name__} does not have find_nb function.")
    assert six_module.find_nb(input_m) == expected_result
