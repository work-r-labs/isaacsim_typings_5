from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.viewport.menubar.lighting.utility import _get_rig_name
from omni.kit.viewport.menubar.lighting.utility import _get_rig_names_and_paths
from omni.kit.viewport.menubar.lighting.utility import _make_light_mode_setting_key
from pxr import Sdf
from pxr import Tf
import pxr.Usd
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdLux
import typing
__all__: list = ['register_actions', 'deregister_actions']
class RegisteredActions:
    _ACTION_TAG: typing.ClassVar[str] = 'Viewport Lighting Menu Actions'
    def __del__(self):
        ...
    def __init__(self, extension_id: str):
        ...
    def destroy(self):
        ...
def _add_rig_reference(light_rig_prim: pxr.Usd.Prim, rig_path: str):
    ...
def _clear_usd_references(stage: pxr.Usd.Stage, prim_path: str):
    ...
def _import_light_rig(path_to: typing.Optional[str] = None, usd_context_name: str = '', exclusive_select: bool = True):
    ...
def _set_lighting_mode(lighting_mode: typing.Union[str, int, NoneType] = None, usd_context: typing.Optional[omni.usd._usd.UsdContext] = None, viewport = None, *args, **kwargs):
    ...
_g_light_rig_hid_vp_lights: bool = False
