"""Tests for six kata."""

import pytest

# Rainfall
DATA = """Rome:Jan 81.2,Feb 63.2,Mar 70.3,Apr 55.7,May 53.0,Jun 36.4,Jul 17.5,Aug 27.5,\
Sep 60.9,Oct 117.7,Nov 111.0,Dec 97.9
London:Jan 48.0,Feb 38.9,Mar 39.9,Apr 42.2,May 47.3,Jun 52.1,Jul 59.5,Aug 57.2,Sep 55.4,Oct 62.0,Nov 59.0,Dec 52.9
Beijing:Jan 3.9,Feb 4.7,Mar 8.2,Apr 18.4,May 33.0,Jun 78.1,Jul 224.3,Aug 170.0,Sep 58.4,Oct 18.0,Nov 9.3,Dec 2.7
"""


@pytest.mark.parametrize(
    "town, data, expected",
    [
        ("London", DATA, 51.199999999999996),
        ("Beijing", DATA, 52.416666666666664),
    ],
)
def test_mean(six_module, town, data, expected):
    """Run tests for mean"""
    result = six_module.mean(town, data)
    assert result == expected, f"{result} is expected to be {expected}"


@pytest.mark.parametrize(
    "town, data, expected",
    [
        ("London", DATA, 57.42833333333374),
        ("Beijing", DATA, 4808.37138888889),
    ],
)
def test_variance(six_module, town, data, expected):
    """Run tests for variance"""
    result = six_module.variance(town, data)
    assert result == pytest.approx(result, rel=1e-2), f"{result} is expected to be {expected}"
