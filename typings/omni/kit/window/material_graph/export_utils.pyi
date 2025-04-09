from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.widget.stage.export_utils import ExportPrimUSD
from omni.kit.window.material_graph.mdl_node_tree_model import MdlNodeItem
import os as os
from pathlib import Path
from pxr import Sdf
import pxr.Usd
from pxr import Usd
from pxr import UsdShade
import pxr.UsdShade
from pxr import UsdUI
from pxr import UsdUtils
__all__: list = ['export', 'Export']
class Export(omni.kit.widget.stage.export_utils.ExportPrimUSD):
    def _Export__get_compound_dir(self) -> str:
        """
        Return the workspace file
        """
    def __init__(self):
        ...
def copy_input_metadata(source: pxr.UsdShade.Input, target: pxr.UsdShade.Input):
    """
    Copy metadata from input to input
    """
def export(path: str, prim: pxr.Usd.Prim):
    """
    Export prim to external USD file
    """
