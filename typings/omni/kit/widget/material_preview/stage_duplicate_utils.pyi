from __future__ import annotations
from omni.usd.commands.stage_helper import UsdStageHelper
import pathlib
from pathlib import Path
from pxr import Sdf
import pxr.Usd
from pxr import Usd
__all__: list = ['copy_meta', 'copy_property', 'copy_prim']
def copy_meta(object: pxr.Usd.Object, object_to: pxr.Usd.Object):
    ...
def copy_prim(prim: pxr.Usd.Prim, stage_to: pxr.Usd.Stage, context_name: str):
    """
    Copies prim and its children to the given stage
    """
def copy_property(property: pxr.Usd.Object, stage_to: pxr.Usd.Stage, context_name: str):
    """
    Copies property to the given stage
    """
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.material_preview-1.0.16/omni/kit/widget/material_preview')
DATA_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.material_preview-1.0.16/data')
