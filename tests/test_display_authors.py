"""Authors.display_authors tests."""

from src.authors import Authors


def test_display_authors(capsys):
    """Test display_authors function."""

    Authors.display_authors()
    out = capsys.readouterr().out

    assert "1. denys_skovoronok" in out
    assert "10. anzhela_maliarevych" in out
