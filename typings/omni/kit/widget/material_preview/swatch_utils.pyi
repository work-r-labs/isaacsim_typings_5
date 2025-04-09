from __future__ import annotations
import pathlib
from pathlib import Path
import pxr.Sdf
from pxr import Sdf
from pxr import Usd
__all__: list = ['get_swatch_layer', 'get_default_camera']
def get_default_camera(layer: pxr.Sdf.Layer) -> typing.Optional[pxr.Sdf.Path]:
    """
    Returns the name of the default camera of the layer
    """
def get_swatch_layer(material_path: pxr.Sdf.Path, swatch_layer_path: typing.Optional[str] = None) -> pxr.Sdf.Layer:
    """
    Form the layer to send for swatch rendering
    """
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.material_preview-1.0.16/omni/kit/widget/material_preview')
SWATCH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.material_preview-1.0.16/data/swatch.usda')
