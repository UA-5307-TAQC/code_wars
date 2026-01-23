"""Tests for volume_of_cuboid"""

from kata.anzhela_maliarevych import eight as anzhela_maliarevych_volume_of_cuboid
from kata.denys_sidorov import eight as denys_sidorov_volume_of_cuboid
from kata.denys_skovoronok import eight as denys_skovoronok_volume_of_cuboid
from kata.hlib_shramko import eight as hlib_shramko_volume_of_cuboid
from kata.kekish import eight as kekish_volume_of_cuboid
from kata.kostiantyn_osypenko import eight as kostiantyn_osypenko_volume_of_cuboid
from kata.maxym_dvolinskyi import eight as maxym_dvolinskyi_volume_of_cuboid
from kata.tliubov import eight as tliubov_volume_of_cuboid
from kata.valentyn_yehoian import eight as valentyn_yehoian_volume_of_cuboid
from kata.vitalinakliuieva import eight as vitalinakliuieva_volume_of_cuboid


def test_anzhela_maliarevych_volume_of_cuboid():
    """Test anzhela_maliarevych_volume_of_cuboid"""
    assert anzhela_maliarevych_volume_of_cuboid.get_volume_of_cuboid(1, 2, 2) == 4
    assert anzhela_maliarevych_volume_of_cuboid.get_volume_of_cuboid(6.3, 2, 5) == 63
    assert anzhela_maliarevych_volume_of_cuboid.get_volume_of_cuboid(6.3, 0, 5) == 0

def test_denys_sidorov_volume_of_cuboid():
    """Test denys_sidorov_volume_of_cuboid"""
    assert denys_sidorov_volume_of_cuboid.get_volume_of_cuboid(1, 2, 2) == 4
    assert denys_sidorov_volume_of_cuboid.get_volume_of_cuboid(6.3, 2, 5) == 63
    assert denys_sidorov_volume_of_cuboid.get_volume_of_cuboid(6.3, 0, 5) == 0

def test_denys_skovoronok_volume_of_cuboid():
    """Test denys_skovoronok_volume_of_cuboid"""
    assert denys_skovoronok_volume_of_cuboid.get_volume_of_cuboid(1, 2, 2) == 4
    assert denys_skovoronok_volume_of_cuboid.get_volume_of_cuboid(6.3, 2, 5) == 63
    assert denys_skovoronok_volume_of_cuboid.get_volume_of_cuboid(6.3, 0, 5) == 0

def test_hlib_shramko_volume_of_cuboid():
    """Test hlib_shramko_volume_of_cuboid"""
    assert hlib_shramko_volume_of_cuboid.get_volume_of_cuboid(1, 2, 2) == 4
    assert hlib_shramko_volume_of_cuboid.get_volume_of_cuboid(6.3, 2, 5) == 63
    assert hlib_shramko_volume_of_cuboid.get_volume_of_cuboid(6.3, 0, 5) == 0

def test_kekish_volume_of_cuboid():
    """Test kekish_volume_of_cuboid"""
    assert kekish_volume_of_cuboid.get_volume_of_cuboid(1, 2, 2) == 4
    assert kekish_volume_of_cuboid.get_volume_of_cuboid(6.3, 2, 5) == 63
    assert kekish_volume_of_cuboid.get_volume_of_cuboid(6.3, 0, 5) == 0

def test_kostiantyn_osypenko_volume_of_cuboid():
    """Test kostiantyn_osypenko_volume_of_cuboid"""
    assert kostiantyn_osypenko_volume_of_cuboid.get_volume_of_cuboid(1, 2, 2) == 4
    assert kostiantyn_osypenko_volume_of_cuboid.get_volume_of_cuboid(6.3, 2, 5) == 63
    assert kostiantyn_osypenko_volume_of_cuboid.get_volume_of_cuboid(6.3, 0, 5) == 0

def test_maxym_dvolinskyi_volume_of_cuboid():
    """Test maxym_dvolinskyi_volume_of_cuboid"""
    assert maxym_dvolinskyi_volume_of_cuboid.get_volume_of_cuboid(1, 2, 2) == 4
    assert maxym_dvolinskyi_volume_of_cuboid.get_volume_of_cuboid(6.3, 2, 5) == 63
    assert maxym_dvolinskyi_volume_of_cuboid.get_volume_of_cuboid(6.3, 0, 5) == 0

def test_tliubov_volume_of_cuboid():
    """Test tliubov_volume_of_cuboid"""
    assert tliubov_volume_of_cuboid.get_volume_of_cuboid(1, 2, 2) == 4
    assert tliubov_volume_of_cuboid.get_volume_of_cuboid(6.3, 2, 5) == 63
    assert tliubov_volume_of_cuboid.get_volume_of_cuboid(6.3, 0, 5) == 0

def test_valentyn_yehoian_volume_of_cuboid():
    """Test valentyn_yehoian_volume_of_cuboid"""
    assert valentyn_yehoian_volume_of_cuboid.get_volume_of_cuboid(1, 2, 2) == 4
    assert valentyn_yehoian_volume_of_cuboid.get_volume_of_cuboid(6.3, 2, 5) == 63
    assert valentyn_yehoian_volume_of_cuboid.get_volume_of_cuboid(6.3, 0, 5) == 0

def test_vitalinakliuieva_volume_of_cuboid():
    """Test vitalinakliuieva_volume_of_cuboid"""
    assert vitalinakliuieva_volume_of_cuboid.get_volume_of_cuboid(1, 2, 2) == 4
    assert vitalinakliuieva_volume_of_cuboid.get_volume_of_cuboid(6.3, 2, 5) == 63
    assert vitalinakliuieva_volume_of_cuboid.get_volume_of_cuboid(6.3, 0, 5) == 0