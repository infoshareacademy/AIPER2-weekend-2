"""Part 4: command-line interface for the folder audit."""

import argparse
import os
import sys
from pathlib import Path

from folder_audit.data import AuditSummary, build_summary
from folder_audit.errors import FolderAuditError, scan_folder_safely
from folder_audit.files import save_json_report


def positive_integer(value: str) -> int:
    """Convert an argparse value to a positive integer.

    TODO 1: return the converted value or raise ``argparse.ArgumentTypeError``
    with a readable message when it is not a positive integer.
    """
    raise NotImplementedError


def build_parser() -> argparse.ArgumentParser:
    """Create the argument parser.

    TODO 2: add these arguments:
    - positional ``folder`` converted to Path;
    - ``--top`` using ``positive_integer``, with a default of 5;
    - optional ``--json`` destination converted to Path;
    - ``--include-hidden`` as a boolean flag.

    Include a short program description and useful help text.
    """
    raise NotImplementedError


def format_bytes(size: int) -> str:
    """Format a byte count as B, KB, MB, or GB.

    TODO 3: divide by 1024 while moving between units. Use no decimal places
    for bytes and one decimal place for larger units.

    Examples: ``800 -> "800 B"`` and ``1536 -> "1.5 KB"``.
    """
    raise NotImplementedError


def print_summary(summary: AuditSummary) -> None:
    """Print file count, total size, extensions, and largest files.

    TODO 4:
    - use ``format_bytes`` for sizes;
    - sort extension names alphabetically;
    - print one largest-file record per line;
    - produce useful output for an empty folder too.
    """
    raise NotImplementedError


def main() -> None:
    """Run the CLI and return its exit code.

    TODO 5:
    - parse arguments;
    - scan with ``scan_folder_safely``;
    - build and print the summary;
    - when ``--json`` is present, call ``save_json_report`` and print the
      report destination;
    - catch FolderAuditError and report it on stderr;
    - catch OSError from writing the report separately;
    """
    folder = sys.argv[1]
    for plik in scan_folder_safely(folder):
        print(plik, os.path.getsize(folder + "/" + plik))

