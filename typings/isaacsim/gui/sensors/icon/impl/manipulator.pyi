from __future__ import annotations
import asyncio as asyncio
import carb as carb
import functools as functools
import omni as omni
from omni.kit.viewport import utility as vpUtil
from omni import ui
from omni.ui import scene as sc
from pxr import Gf
import pxr.Sdf
from pxr import Sdf
__all__: list = ['IconManipulator', 'PreventOthers']
class IconManipulator(omni.ui_scene._scene.Manipulator):
    def __init__(self, icon_scale: float = 1.0, **kwargs):
        ...
    def _icon_clicked(self, prim_path: pxr.Sdf.Path, shape: omni.ui_scene._scene.AbstractShape):
        """
        Handle click gestures on the icon image.
        """
    def build_icon_by_path(self, prim_path, need_check):
        """
        Build the UI elements for a single icon at the given path.
        """
    def check_viewport_pos(self, position):
        """
        Check if the world position is within the viewport screen space.
        """
    def on_build(self):
        ...
    def on_model_updated(self, item):
        """
        Callback when the model signals an item has changed.
        """
    def rebuild_icons(self, need_check = False):
        ...
    def update_icon_position(self, prim_path):
        """
        Update the transform of an existing icon UI element.
        """
class PreventOthers(omni.ui_scene._scene.GestureManager):
    """
    
        Prevent other gestures from hiding the icon click gesture.
        
    """
    def __init__(self):
        ...
    def can_be_prevented(self, gesture):
        ...
    def should_prevent(self, gesture, preventer):
        ...
SHOW_TITLE_PATH: str = 'exts/omni.kit.prim.icon/showTitle'
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
