from __future__ import annotations
import enum
from enum import Enum
import typing
__all__ = ['Enum', 'TestRunStatus', 'add_test_status_report_cb', 'remove_test_status_report_cb']
class TestRunStatus(enum.Enum):
    """
    An enumeration.
    """
    FAILED: typing.ClassVar[TestRunStatus]  # value = <TestRunStatus.FAILED: 3>
    PASSED: typing.ClassVar[TestRunStatus]  # value = <TestRunStatus.PASSED: 2>
    RUNNING: typing.ClassVar[TestRunStatus]  # value = <TestRunStatus.RUNNING: 1>
    UNKNOWN: typing.ClassVar[TestRunStatus]  # value = <TestRunStatus.UNKNOWN: 0>
def _test_status_report(test_id: str, status: TestRunStatus, **kwargs):
    ...
def add_test_status_report_cb(callback: typing.Callable[[str, omni.kit.test.test_reporters.TestRunStatus, typing.Any], NoneType]):
    """
    Add callback to be called when tests start, fail, pass.
    """
def remove_test_status_report_cb(callback: typing.Callable[[str, omni.kit.test.test_reporters.TestRunStatus, typing.Any], NoneType]):
    """
    Remove callback to be called when tests start, fail, pass.
    """
_callbacks: list = list()
