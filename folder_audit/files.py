"""Part 2: scanning directories and writing files.

Use only the standard library. Let operating-system errors propagate for now;
they will be translated into friendly errors in Part 3.
"""

import os
from pathlib import Path

from folder_audit.data import AuditSummary


PathLike = str | Path
NO_EXTENSION = "[no extension]"


def scan_folder(folder: PathLike) -> list[str]:
    """Recursively collect information about regular files in ``folder``.
    """
    return os.listdir(folder)


def save_json_report(summary: AuditSummary, destination: PathLike) -> None:
    """Write ``summary`` as readable UTF-8 JSON.

    TODO 2:
    - create the destination's parent directories when needed;
    - use ``json.dump`` with an indentation of two spaces;
    - add a final newline to the file.
    """
    raise NotImplementedError
