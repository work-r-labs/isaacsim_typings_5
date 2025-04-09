from __future__ import annotations
from pxr import Usd
from pxr import UsdUtils
__all__ = ['Usd', 'UsdStageHelper', 'UsdUtils']
class UsdStageHelper:
    """
    Keeps the stage ID or returns the stage from the current context
    """
    def __init__(self, stage: typing.Optional[pxr.Usd.Stage] = None, context_name: typing.Optional[str] = None):
        ...
    def _get_context(self) -> typing.Optional[ForwardRef('omni.usd.context')]:
        ...
    def _get_stage(self) -> typing.Optional[pxr.Usd.Stage]:
        """
        Get staved stage
        """
    def _set_stage(self, stage: typing.Optional[pxr.Usd.Stage] = None, context_name: typing.Optional[str] = None):
        """
        Save stage ID or context name
        """
