from __future__ import annotations
import carb as carb
import math as math
import omni as omni
from omni.kit import commands
from omni.kit.manipulator.camera.manipulator import CameraManipulatorBase
from omni.kit.manipulator.camera.manipulator import adjust_center_of_interest
from omni.kit.manipulator.camera.model import _flatten_matrix
from omni.kit.manipulator.camera.model import _optional_bool
from omni.kit import undo
import pxr.Gf
from pxr import Gf
import pxr.Sdf
from pxr import Sdf
from pxr import Tf
from pxr import Usd
import pxr.Usd
from pxr import UsdGeom
import pxr.UsdGeom
__all__: list = ['UsdCameraManipulator']
class ExternalUsdCameraChange:
    @staticmethod
    def _ExternalUsdCameraChange__object_changed(*args, **kwds):
        ...
    def __del__(self):
        ...
    def __init__(self, time: pxr.Usd.TimeCode):
        ...
    def destroy(self):
        ...
    def pause_tracking(self):
        ...
    def start_tracking(self):
        ...
    def update(self, model, usd_context_name: str, prim_path: pxr.Sdf.Path):
        ...
class SRTDecomposer:
    @staticmethod
    def _SRTDecomposer__find_best_euler_angles(old_rot_vec: pxr.Gf.Vec3d, new_rot_vec: pxr.Gf.Vec3d, rotation_order: pxr.Gf.Vec3i) -> pxr.Gf.Vec3d:
        ...
    @staticmethod
    def _SRTDecomposer__generate_compatible_euler_angles(euler: pxr.Gf.Vec3d, rotation_order: pxr.Gf.Vec3i) -> typing.List[pxr.Gf.Vec3d]:
        ...
    @staticmethod
    def _SRTDecomposer__repeat(t: float, length: float) -> float:
        ...
    def __init__(self, prim: pxr.Usd.Prim, time: pxr.Usd.TimeCode = None):
        ...
    def update(self, xform: pxr.Gf.Matrix4d):
        ...
    @property
    def rotation(self):
        ...
    @property
    def start_rotation(self):
        ...
    @property
    def start_translation(self):
        ...
    @property
    def translation(self):
        ...
class UsdCameraManipulator(omni.kit.manipulator.camera.manipulator.CameraManipulatorBase):
    """
    Base Usd camera manipulator implementation that will set model's value back to Usd data via kit-commands.
    """
    @staticmethod
    def _UsdCameraManipulator__vp1_cooperation(*args, **kwds):
        ...
    @staticmethod
    def on_model_updated(*args, **kwds):
        """
        
                Called whenever the model changes.
        
                Args:
                    item (omni.ui.scene.AbstractManipulatorItem): Identify which item in the model has changed.
                
        """
    def __init__(self, bindings: dict = None, usd_context_name: str = '', prim_path: pxr.Sdf.Path = None, *args, **kwargs):
        """
        
                Constructor.
        
                Args:
                    bindings (dict): Set the bindings for the class.
                    usd_context_name (str): Set the name of the usd context.
                    prim_path (Sdf.Path): Set the camera prim path.
                
        """
    def _on_began(self, model, *args, **kwargs):
        ...
    def _set_context(self, usd_context_name: str, prim_path: pxr.Sdf.Path):
        ...
def _compute_local_transform(imageable: pxr.UsdGeom.Imageable, time: pxr.Usd.TimeCode):
    ...
def _get_context_stage(usd_context_name: str):
    ...
KIT_CAMERA_LOCK_ATTRIBUTE: str = 'omni:kit:cameraLock'
KIT_COI_ATTRIBUTE: str = 'omni:kit:centerOfInterest'
KIT_LOOKTHROUGH_ATTRIBUTE: str = 'omni:kit:viewport:lookThrough:target'
