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


FIND_NB = [
    (4, -1),
    (16, -1),
    (4183059834009, 2022),
    (24723578342962, -1),
    (135440716410000 , 4824),
    (40539911473216, 3568)
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