import os
import stat
import tempfile
import unittest
from pathlib import Path

from audit_permissions import audit_directory


class AuditPermissionsTests(unittest.TestCase):
    def test_detects_world_writable_file(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            target = root / "review_me.txt"
            target.write_text("sample", encoding="utf-8")
            target.chmod(0o666)
            self.assertIn(target, audit_directory(root))

    def test_ignores_file_without_world_write(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            target = root / "private.txt"
            target.write_text("sample", encoding="utf-8")
            target.chmod(0o644)
            self.assertNotIn(target, audit_directory(root))

    def test_detects_world_writable_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            target = root / "shared"
            target.mkdir()
            target.chmod(0o777)
            self.assertIn(target, audit_directory(root))

    def test_rejects_file_as_root(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "file.txt"
            target.write_text("sample", encoding="utf-8")
            with self.assertRaises(NotADirectoryError):
                audit_directory(target)


if __name__ == "__main__":
    unittest.main()
