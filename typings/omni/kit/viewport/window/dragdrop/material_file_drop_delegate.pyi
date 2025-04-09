from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni.kit.viewport.window.dragdrop.usd_prim_drop_delegate
from omni.kit.viewport.window.dragdrop.usd_prim_drop_delegate import UsdShadeDropDelegate
import os as os
import pxr.Sdf
from pxr import Sdf
import pxr.Usd
from pxr import Usd
from pxr import UsdGeom
__all__: list = ['MaterialFileDropDelegate']
class MaterialFileDropDelegate(omni.kit.viewport.window.dragdrop.usd_prim_drop_delegate.UsdShadeDropDelegate):
    def __init__(self, preview_setting: str = None, show_alert: bool = True, **kwargs):
        ...
    def accept_url(self, url: str) -> str:
        ...
    def accepted(self, drop_data: dict) -> bool:
        ...
    def dropped(self, drop_data: dict):
        ...
    def get_material_name(self, url: str, need_result: bool) -> typing.List[str]:
        ...
    def get_material_prim_location(self, stage: pxr.Usd.Stage) -> pxr.Sdf.Path:
        ...
    def reset_state(self) -> None:
        ...
    @property
    def honor_picking_mode(self):
        ...
