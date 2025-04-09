from __future__ import annotations
import omni as omni
from omni import ui
from pxr import Usd
from pxr import UsdGeom
__all__: list = ['VisibilityModel']
class VisibilityModel(omni.ui._ui.AbstractValueModel):
    def __init__(self, stage_item):
        ...
    def _get_prim_visibility(self, prim):
        ...
    def destroy(self):
        ...
    def get_value_as_bool(self) -> bool:
        """
        Reimplemented get bool
        """
    def set_value(self, value: bool):
        """
        Reimplemented set bool
        """
    @property
    def stage_item(self):
        ...
