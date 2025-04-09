from __future__ import annotations
import omni.kit.viewport.window.dragdrop.scene_drop_delegate
from omni.kit.viewport.window.dragdrop.scene_drop_delegate import SceneDropDelegate
from pxr import Gf
import re as re
__all__: list = ['AudioFileDropDelegate']
class AudioFileDropDelegate(omni.kit.viewport.window.dragdrop.scene_drop_delegate.SceneDropDelegate):
    def accept_url(self, url: str) -> str:
        ...
    def accepted(self, drop_data: dict) -> bool:
        ...
    def dropped(self, drop_data: dict):
        ...
