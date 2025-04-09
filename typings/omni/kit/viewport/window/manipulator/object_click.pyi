from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.viewport.window.raycast import perform_raycast_query
from omni.ui import scene as sc
from pxr import Gf
from pxr import Sdf
import typing
__all__: list = ['ObjectClickFactory']
class ObjectClickGesture(omni.ui_scene._scene.DoubleClickGesture):
    def _ObjectClickGesture__query_completed(self, prim_path: str, world_space_pos, *args):
        ...
    def __init__(self, viewport_api, mouse_button: int):
        ...
    def on_ended(self, *args):
        ...
class ObjectClickManipulator(omni.ui_scene._scene.Manipulator):
    VP_COI_SETTING: typing.ClassVar[str] = '/exts/omni.kit.viewport.window/coiDoubleClick'
    def _ObjectClickManipulator__coi_enabled_changed(self, item: carb.dictionary._dictionary.Item, event_type: carb.settings._settings.ChangeEventType):
        ...
    def __init__(self, viewport_api, mouse_button: int = 0, **kwargs):
        ...
    def destroy(self):
        ...
    def on_build(self):
        ...
    @property
    def categories(self) -> typing.Sequence:
        ...
    @property
    def name(self) -> str:
        ...
KIT_COI_ATTRIBUTE: str = 'omni:kit:centerOfInterest'
