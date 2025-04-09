from __future__ import annotations
import carb as carb
from cmath import isfinite
from omni.kit.viewport.window.dragdrop.delegate import DragDropDelegate
from omni.kit.viewport.window.raycast import perform_raycast_query
from omni import ui
import omni.ui._ui
from pxr import Kind
from pxr import Sdf
import pxr.Sdf
from pxr import Usd
from pxr import UsdGeom
import traceback as traceback
__all__: list = ['DragDropHandler']
class DragDropHandler:
    @staticmethod
    def drag_drop_colors():
        ...
    @staticmethod
    def picking_mode():
        ...
    def _DragDropHandler__query_complete(self, is_drop: bool, prim_path: str, world_space_pos: typing.Sequence[float], *args):
        ...
    def _DragDropHandler__set_prim_outline(self, prim_path: pxr.Sdf.Path = None):
        ...
    def __init__(self, payload: dict):
        ...
    def _perform_query(self, ui_obj: omni.ui._ui.Widget, mouse: typing.Sequence[float], is_drop: bool = False):
        ...
    def accepted(self, ui_obj: omni.ui._ui.Widget, url_data: str):
        ...
    def cancel(self, ui_obj: omni.ui._ui.Widget):
        ...
    def dropped(self, ui_obj: omni.ui._ui.Widget, event: omni.ui._ui.WidgetMouseDropEvent):
        ...
    def get_enclosing_model(self, prim_path: str):
        ...
    def setup_outline(self, outline_color: typing.Sequence[float], shade_color: typing.Sequence[float] = (0, 0, 0, 0), sel_group: int = 254):
        ...
    @property
    def viewport_api(self):
        ...
