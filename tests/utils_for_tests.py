"""Utils for tests."""

import importlib
from pathlib import Path

import kata


def get_authors():
    """Get a list of authors."""
    kata_dir = Path(kata.__file__).parent
    return [f.name for f in kata_dir.iterdir() if f.is_dir() and f.name[0] != "_"]


def import_authors_kuy_file(author: str, kuy_file: str):
    """Import an author's correct kuy file."""
    return importlib.import_module(f"kata.{author}.{kuy_file}")
