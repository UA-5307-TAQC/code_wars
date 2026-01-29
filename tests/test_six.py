"""Tests for solutions of six kyu module."""

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

RAINFALL_DATA = """Rome:Jan 81.2,Feb 63.2,Mar 70.3,Apr 55.7,May 53.0,Jun 36.4,Jul 17.5,Aug 27.5,\
Sep 60.9,Oct 117.7,Nov 111.0,Dec 97.9
London:Jan 48.0,Feb 38.9,Mar 39.9,Apr 42.2,May 47.3,Jun 52.1,Jul 59.5,Aug 57.2,Sep 55.4,Oct 62.0,Nov 59.0,Dec 52.9
Beijing:Jan 3.9,Feb 4.7,Mar 8.2,Apr 18.4,May 33.0,Jun 78.1,Jul 224.3,Aug 170.0,Sep 58.4,Oct 18.0,Nov 9.3,Dec 2.7
"""


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


@pytest.mark.parametrize(
    "x, expected",
    [
        (2.6e-08, 1.29999999155e-08),
        (1.4e-09, 6.999999997549999e-10),
        (5.0e-06, 2.499996875007812e-06),
        (2.4e-07, 1.1999999280000085e-07),
        (2.1e-11, 1.0499999999944874e-11),
        (0.00017, 8.499638780702988e-05),
        (1.9e-07, 9.499999548750044e-08),
        (1.8e-08, 8.999999959500001e-09),
        (4.2e-08, 2.0999999779500002e-08),
        (7.0e-05, 3.499938752143656e-05),
    ],
)
def test_f(six_module, x, expected):
    """Tests for f function of all authors."""
    f_result = six_module.f(x)
    assert f_result == pytest.approx(expected, rel=1e-12)


@pytest.mark.parametrize(
    "town, data, expected",
    [
        ("London", RAINFALL_DATA, 51.199999999999996),
        ("Beijing", RAINFALL_DATA, 52.416666666666664),
    ],
)
def test_mean(six_module, town, data, expected):
    """Run tests for mean"""

    result = six_module.mean(town, data)
    assert result == expected, f"{result} is expected to be {expected}"


@pytest.mark.parametrize(
    "town, data, expected",
    [
        ("London", RAINFALL_DATA, 57.42833333333374),
        ("Beijing", RAINFALL_DATA, 4808.37138888889),
    ],
)
def test_variance(six_module, town, data, expected):
    """Run tests for variance"""

    result = six_module.variance(town, data)
    assert result == pytest.approx(expected, rel=1e-2), f"{result} is expected to be {expected}"
