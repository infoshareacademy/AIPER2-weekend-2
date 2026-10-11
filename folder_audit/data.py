"""Part 1: collections and data.

Start here. These functions operate only on data already stored in memory.
Do not read directories or files in this module.
"""

from typing import TypedDict


class FileInfo(TypedDict):
    path: str
    extension: str
    size_bytes: int


class AuditSummary(TypedDict):
    file_count: int
    total_size_bytes: int
    extension_counts: dict[str, int]
    largest_files: list[FileInfo]


SAMPLE_FILES: list[FileInfo] = [
    {"path": "notes/todo.txt", "extension": ".txt", "size_bytes": 1200},
    {"path": "notes/ideas.txt", "extension": ".txt", "size_bytes": 800},
    {"path": "data/users.csv", "extension": ".csv", "size_bytes": 2500},
    {"path": "README", "extension": "[no extension]", "size_bytes": 300},
]


def unique_extensions(files: list[FileInfo]) -> set[str]:
    """Return the set of extensions found in ``files``.

    For SAMPLE_FILES the result contains ``.txt``, ``.csv``, and
    ``[no extension]``.
    """
    # TODO 1: build and return a set.
    raise NotImplementedError


def count_extensions(files: list[FileInfo]) -> dict[str, int]:
    """Return a mapping of extension to number of files.

    Expected result for SAMPLE_FILES::

        {".txt": 2, ".csv": 1, "[no extension]": 1}
    """
    # TODO 2: count values with a dictionary.
    raise NotImplementedError


def total_size(files: list[FileInfo]) -> int:
    """Return the combined size in bytes.

    The result is 4800 for SAMPLE_FILES and 0 for an empty list.
    """
    # TODO 3: sum the size_bytes values.
    raise NotImplementedError


def largest_files(files: list[FileInfo], limit: int) -> list[FileInfo]:
    """Return at most ``limit`` files, ordered from largest to smallest.

    Do not modify the input list. Return an empty list when ``limit <= 0``.
    For ``largest_files(SAMPLE_FILES, 2)``, ``data/users.csv`` comes first and
    ``notes/todo.txt`` comes second.
    """
    # TODO 4: combine sorted() with list slicing.
    raise NotImplementedError


def build_summary(files: list[FileInfo], top: int = 5) -> AuditSummary:
    """Build one JSON-serializable summary from the earlier functions."""
    # TODO 5: return all four AuditSummary fields.
    raise NotImplementedError


if __name__ == "__main__":
    print("Start with TODO 1. Expected results are documented above each task.")
