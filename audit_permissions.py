#!/usr/bin/env python3
"""Report world-writable files and directories without changing anything."""

import argparse
import os
import stat
from pathlib import Path


def audit_directory(root: Path) -> list[Path]:
    """Return paths with the 'others write' bit set, skipping symlinks."""
    findings: list[Path] = []
    root = root.expanduser()
    if not root.exists():
        raise FileNotFoundError(f"Path does not exist: {root}")
    if not root.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {root}")

    for current, dirs, files in os.walk(root, followlinks=False):
        current_path = Path(current)
        # Do not descend into symlinked directories.
        dirs[:] = [d for d in dirs if not (current_path / d).is_symlink()]
        for name in dirs + files:
            path = current_path / name
            try:
                if path.is_symlink():
                    continue
                mode = path.stat(follow_symlinks=False).st_mode
            except (PermissionError, FileNotFoundError, OSError):
                continue
            if mode & stat.S_IWOTH:
                findings.append(path)
    return sorted(findings, key=lambda p: str(p))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Report world-writable paths under a directory (read-only audit)."
    )
    parser.add_argument(
        "directory", nargs="?", default=".",
        help="directory to audit (default: current directory)"
    )
    args = parser.parse_args()
    root = Path(args.directory)

    try:
        findings = audit_directory(root)
    except (FileNotFoundError, NotADirectoryError) as exc:
        parser.error(str(exc))

    print(f"Permission audit: {root.resolve()}")
    if findings:
        print(f"Potential issue(s): {len(findings)} world-writable path(s) found")
        for path in findings:
            print(f"[REVIEW] {path}")
        print("Review each finding before changing permissions.")
        return 1

    print("No world-writable paths found in the scanned tree.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
