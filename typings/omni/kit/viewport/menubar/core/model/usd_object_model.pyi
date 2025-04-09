from __future__ import annotations
import omni as omni
from omni.kit.viewport.menubar.core.utils.usd_watch import subscribe as usd_watch_subscribe
from omni import ui
import pxr.Sdf
from pxr import Sdf
import pxr.Usd
from pxr import Usd
__all__: list = ['USDObjectModel']
class USDObjectModel(omni.ui._ui.AbstractValueModel):
    """
    A base-class model to watch changes on a UsdObject (UsdPrim, UsdProperty, UsdAttribute, UsdRelationship).
    """
    draggable: bool
    def __init__(self, stage: pxr.Usd.Stage, path: pxr.Sdf.Path, time: pxr.Usd.TimeCode = None, draggable: bool = False):
        ...
    def _get_value(self) -> typing.Any:
        """
        Get the value directly from USD
        """
    def _on_usd_changed(self):
        """
        Called by UsdWatch
        """
    def begin_edit(self):
        """
        
                Reimplemented from the base class.
                Called when the user starts editing.
                
        """
    def destroy(self):
        ...
    def end_edit(self):
        """
        
                Set value when the user finishes editing.
                
        """
    def get_value_as_bool(self) -> bool:
        ...
    def get_value_as_float(self) -> float:
        ...
    def get_value_as_int(self) -> int:
        ...
    def get_value_as_string(self) -> str:
        ...
    def set_value(self, value: typing.Any):
        """
        Set the value directly to USD
        """
    @property
    def path(self):
        ...
    @property
    def stage(self):
        ...
    @property
    def time(self):
        ...
