"""Part 3: validating input and translating exceptions."""

from pathlib import Path
import sys

from folder_audit.data import FileInfo
from folder_audit.files import PathLike, scan_folder


class FolderAuditError(Exception):
    """Base class for errors that can be shown directly to the user."""


class FolderNotFoundError(FolderAuditError):
    """The requested path does not exist."""


class InvalidFolderError(FolderAuditError):
    """The requested path exists but is not a directory."""


class FolderAccessError(FolderAuditError):
    """The operating system refused access while scanning."""


def scan_folder_safely(folder: PathLike) -> list[str]:
    """Validate and scan a folder, translating expected OS errors.

    TODO 2:
    - call ``scan_folder`` inside try/except;
    - translate PermissionError into FolderAccessError;
    - translate other OSError instances into FolderAud  itError;
    - preserve the original exception with ``raise ... from error``;
    - do not use ``except Exception``.
    """
    try:
        return scan_folder(folder)
    except FileNotFoundError:
        print("Folder nie istnieje", file=sys.stderr)
    except SystemExit:  # bomba
        print("Bomba!", file=sys.stderr)
        return 1

