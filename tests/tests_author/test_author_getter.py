"""Test author getter"""

from src.authors import Authors


def test_author_getter():
    """Test author getter"""
    assert Authors.get_authors() == (
        "denys_skovoronok",
        "denys_sidorov",
        "hlib_shramko",
        "kekish",
        "kostiantyn_osypenko",
        "maxym_dvolinskyi",
        "tliubov",
        "valentyn_yehoian",
        "vitalinakliuieva",
    )
