from __future__ import annotations
import carb as carb
from pxr import Gf
from pxr import Kind
from pxr import Sdf
from pxr import Tf
import pxr.Usd
from pxr import Usd
from pxr import UsdGeom
import typing
__all__: list = ['init_settings', 'save_implicit_cameras']
class SelectionSettings:
    _g_inited: typing.ClassVar[bool] = True
    @staticmethod
    def init(isettings):
        ...
class StageAxis:
    """
    Utility class to update implcit cameras when the Usd.Stage up-axis changes
    """
    @staticmethod
    def _StageAxis__get_adjustment_matrix(current_up, previous_up):
        ...
    @staticmethod
    def update(*args, **kwds):
        ...
    def __init__(self, stage: pxr.Usd.Stage, up_axis: str = None):
        ...
def _build_viewport_cameras(*args, **kwds):
    ...
def _init_viewport_cameras(*args, **kwds):
    ...
def _report_error():
    ...
def _run_viewport_auto_frame(*args, **kwds):
    ...
def _support_legacy_viewport():
    ...
def init_settings(*args, **kwds):
    ...
def save_implicit_cameras(*args, **kwds):
    ...
