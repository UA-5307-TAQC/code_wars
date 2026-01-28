"""Gap in primes tests."""

import pytest


@pytest.mark.parametrize(
    "num, expected",
    [
        (2, 0.5),
        (4, 0.6096117967977924),
        (5, 0.641742430504416),
        (6, 0.6666666666666666),
        (10, 0.7298437881283576),
        (100, 0.904875078027496),
        (10000, 0.9900498750007813),
    ],
)
def test_solve(five_module, num, expected):
    """Run tests."""

    result = five_module.solve(num)
    assert result == expected, f"{num} is expected to be {expected}, not {result}"


@pytest.mark.parametrize(
    "gap, start, end, expected",
    [
        (2, 100, 110, [101, 103]),
        (4, 100, 110, [103, 107]),
        (6, 100, 110, None),
        (8, 300, 400, [359, 367]),
        (10, 300, 400, [337, 347]),
        (2, 100, 103, [101, 103]),
    ],
)
def test_gap(five_module, gap, start, end, expected):
    """Run tests."""

    result = five_module.gap(gap, start, end)
    assert result == expected, f"{gap}, {start}, {end} is expected to be {expected}"
