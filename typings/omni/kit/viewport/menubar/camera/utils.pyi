from __future__ import annotations
import omni as omni
import pxr.Sdf
from pxr import Sdf
from pxr import Usd
__all__ = ['SESSION_CAMERAS', 'Sdf', 'Usd', 'get_camera_display', 'omni']
def get_camera_display(path: pxr.Sdf.Path, stage: typing.Optional[pxr.Usd.Stage] = None):
    ...
SESSION_CAMERAS: dict = {'/OmniverseKit_Persp': 'Perspective', '/OmniverseKit_Top': 'Top', '/OmniverseKit_Front': 'Front', '/OmniverseKit_Right': 'Right'}
