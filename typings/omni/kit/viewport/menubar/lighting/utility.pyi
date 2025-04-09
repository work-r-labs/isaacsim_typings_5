from __future__ import annotations
import carb as carb
import omni as omni
from pathlib import Path
import pxr.Sdf
from pxr import Sdf
import pxr.Usd
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdUtils
import typing
__all__: list = ['VisibilityEdit', 'RefCountedUsdContextSub', 'stage_has_prim_type']
class RefCountedUsdContextSub:
    """
    Create a single stage-open callback for multiple instance attaching to a single omni.usd.USdContext
    """
    _RefCountedUsdContextSub__g_usd_stage_subs: typing.ClassVar[dict] = {}
    def __del__(self):
        ...
    def __init__(self, usd_context_name: typing.Optional[str] = None, usd_context_opened: typing.Optional[typing.Callable] = None, setting_path: typing.Optional[str] = None, setting_changed: typing.Optional[typing.Callable] = None):
        ...
    def destroy(self):
        ...
class VisibilityEdit:
    @staticmethod
    def _VisibilityEdit__gather_prims(*args, **kwds):
        ...
    @staticmethod
    def _VisibilityEdit__get_prim_iterator(*args, **kwds):
        ...
    @staticmethod
    def _VisibilityEdit__hide_prims(*args, **kwds):
        ...
    def _VisibilityEdit__get_visibility(self, prim: pxr.Usd.Prim, prim_path: pxr.Sdf.Path):
        ...
    def _VisibilityEdit__is_hidden_in_stage_window(self, usd_prim: pxr.Usd.Prim):
        ...
    def __init__(self, stage, types_to_show: typing.Optional[typing.Callable] = None, types_to_hide: typing.Optional[typing.Callable] = None, types_for_prune: typing.Optional[typing.Sequence[str]] = None, api_types_for_prune: typing.Optional[typing.Sequence[str]] = None):
        ...
    def run(self):
        ...
    @property
    def predicate(self):
        ...
def _get_light_rig_setting_key(extension_id: str):
    ...
def _get_rig_name(light_rig: typing.Union[pathlib.Path, str]):
    ...
def _get_rig_names_and_paths(extension_id: str):
    ...
def _get_usd_rt_stage(stage: pxr.Usd.Stage):
    ...
def _make_light_mode_setting_key(usd_context: omni.usd._usd.UsdContext) -> str:
    ...
def _sort_rigs_paths(light_rigs: typing.Sequence[pathlib.Path]) -> typing.Sequence[pathlib.Path]:
    ...
def stage_has_api_type(*args, **kwds) -> bool:
    """
    Return if the stage has any Usd.Prims of type given
    """
