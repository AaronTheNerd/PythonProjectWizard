import unittest
import unittest.mock as mock
from dataclasses import dataclass, field

from merlin.dialog.dialog import Dialog
from merlin.dialog.project_dialog import ProjectDialog
from merlin.dialog_runner.synchronous_runner import SyncRunner
from merlin.display.console import Console


@dataclass
class TestResult:
    name: str = field(init=False)


class TestDialog(Dialog[TestResult]):
    def run(self) -> TestResult:
        return TestResult()


class DialogTestSuite(unittest.TestCase):
    def test_constructor(self):
        self.assertIsInstance(ProjectDialog(SyncRunner(Console())), Dialog)

    def test_run(self):
        test_inputs = [
            "Merlin",  # Name
            "3.10",  # Version
            "Y",  # Black formatting
            "Y",  # Logging
            "N",  # Unit test
            "Y",  # Configs
            "Y",  # args
        ]
        display = Console()
        dialog = ProjectDialog(SyncRunner(display))
        with mock.patch("builtins.input", side_effect=test_inputs):
            project = dialog.run()
            self.assertEqual(project.name, "Merlin")
            self.assertEqual(project.python_version, "3.10")
            self.assertEqual(project.use_black_formatting, True)
            self.assertEqual(project.use_logging, True)
            self.assertEqual(project.use_unittest, False)
            self.assertEqual(project.use_configs, True)
            self.assertEqual(project.use_args, True)
