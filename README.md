# Linux Security & System Hardening Lab

A small, defensive Python lab that audits file permissions in a directory you own or are authorized to inspect. It reports world-writable files and directories, skips symbolic links, and prints a summary. It does not change permissions or modify files.

## Features
- Audits a selected directory recursively.
- Flags paths where the “others write” permission bit is enabled.
- Skips symbolic links to avoid following links outside the selected tree.
- Includes a hardening checklist and automated tests.

## Requirements
- Python 3.9 or newer
- No third-party packages

## Run
From this folder, run:

```bash
python audit_permissions.py .
```

You can also specify a directory you own or are authorized to inspect:

```bash
python audit_permissions.py ./demo_directory
```

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Important limitations
- This is a learning tool, not a complete Linux security scanner.
- Permission behavior varies by operating system and filesystem.
- The script only reports findings; review them before making any changes.
- Only scan directories you own or have permission to inspect.
