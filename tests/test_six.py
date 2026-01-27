"""Easy Balance Checking."""

import pytest


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
