from __future__ import annotations
import carb as carb
from functools import partial
import omni as omni
from omni.kit.property.geometry.scripts.geometry_commands import PrimVarCommand
from omni.kit.property.geometry.scripts.geometry_commands import ToggleInstanceableCommand
from omni.kit.property.geometry.scripts.geometry_commands import TogglePrimVarCommand
from omni.kit.property.geometry.scripts.geometry_properties import GeometryPropertyExtension
from omni.kit.property.geometry.scripts.geometry_properties import get_instance
from omni.kit.property.usd.prim_selection_payload import PrimSelectionPayload
from pxr import Sdf
from pxr import Tf
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdUI
from . import geometry_commands
from . import prim_geometry_widget
from . import prim_kind_widget
__all__: list = ['PrimVarCommand', 'TogglePrimVarCommand', 'ToggleInstanceableCommand', 'PrimSelectionPayload', 'get_instance', 'GeometryPropertyExtension', 'geometry_properties']
class geometry_properties:
    @staticmethod
    def get_instance(*args, **kwargs):
        ...
