"""Tests for solutions of six kyu module."""

import pytest


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
