from __future__ import annotations
import carb as carb
import omni as omni
from pxr import Gf
from pxr import Kind
from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdLux
from pxr import UsdShade
from pxr import Vt
__all__ = ['DefaultStage', 'Gf', 'Kind', 'Sdf', 'Usd', 'UsdGeom', 'UsdLux', 'UsdShade', 'Vt', 'carb', 'omni']
class DefaultStage:
    def __del__(self):
        ...
    def __init__(self):
        ...
    def new_stage(self, rootname, usd_context_name):
        ...
