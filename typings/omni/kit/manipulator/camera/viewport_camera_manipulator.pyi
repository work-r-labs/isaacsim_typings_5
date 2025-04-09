from __future__ import annotations
import carb as carb
import math as math
import omni as omni
from omni.kit.manipulator.camera.model import CameraManipulatorModel
from omni.kit.manipulator.camera.model import _flatten_matrix
from omni.kit.manipulator.camera.model import _optional_bool
from omni.kit.manipulator.camera.model import _optional_int
from omni.kit.manipulator.camera.usd_camera_manipulator import UsdCameraManipulator
from omni.kit.manipulator.camera.usd_camera_manipulator import _compute_local_transform
from omni.ui import scene as sc
from pxr import Gf
from pxr import Sdf
from pxr import Usd
import pxr.Usd
from pxr import UsdGeom
import pxr.UsdGeom
import time as time
import typing
__all__: list = ['ViewportCameraManipulator']
class ViewportCameraManipulator(omni.kit.manipulator.camera.usd_camera_manipulator.UsdCameraManipulator):
    def __init__(self, viewport_api, bindings: dict = None, *args, **kwargs):
        """
        
                Constructor.
        
                Args:
                    viewport_api (:obj:'ViewportAPI'): The viewport's api interface class.
                    bindings (dict): Dictionary that maps a gesture name to a button name..
                
        """
    def _on_began(self, model: omni.kit.manipulator.camera.model.CameraManipulatorModel, mouse):
        ...
    def destroy(self):
        """
         Destroys the manipulator instance. 
        """
class ZoomEvents:
    _ZoomEvents__instances: typing.ClassVar[set] = set()
    @staticmethod
    def get_instance(viewport_api):
        ...
    def _ZoomEvents__mark_time(self):
        ...
    def _ZoomEvents__on_event(self, e: carb.events._events.IEvent):
        ...
    def _ZoomEvents__time_since_last(self):
        ...
    def __init__(self, viewport_api):
        ...
    def destroy(self):
        ...
    def update(self, x, y):
        ...
def _check_for_camera_forwarding(imageable: pxr.UsdGeom.Imageable):
    ...
def _setup_center_of_interest(model: omni.ui_scene._scene.AbstractManipulatorModel, prim: pxr.Usd.Prim, time: pxr.Usd.TimeCode, object_centric: int = 0, viewport_api = None, mouse = None):
    ...
def _zoom_operation(x, y, viewport_api):
    ...
KIT_CAMERA_LOCK_ATTRIBUTE: str = 'omni:kit:cameraLock'
KIT_COI_ATTRIBUTE: str = 'omni:kit:centerOfInterest'
KIT_LOOKTHROUGH_ATTRIBUTE: str = 'omni:kit:viewport:lookThrough:target'
