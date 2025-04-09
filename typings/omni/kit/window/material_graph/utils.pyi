from __future__ import annotations
import omni as omni
from pxr import Sdr
import pxr.Usd
from pxr import Usd
from pxr import UsdShade
__all__ = ['Sdr', 'USD_PREVIEW_SURFACE_SHADERS', 'Usd', 'UsdShade', 'can_connect', 'isUsdPreviewSurfaceShader', 'omni']
def can_connect(model, source_attr: pxr.Usd.Attribute, target_attr: pxr.Usd.Attribute):
    """
    Return if it's possible to connect source_attr to target_attr
    """
def isUsdPreviewSurfaceShader(prim: pxr.Usd.Prim):
    ...
USD_PREVIEW_SURFACE_SHADERS: list = ['UsdPreviewSurface', 'UsdPrimvarReader_int', 'UsdPrimvarReader_float', 'UsdPrimvarReader_float2', 'UsdPrimvarReader_float3', 'UsdPrimvarReader_float4', 'UsdPrimvarReader_matrix', 'UsdPrimvarReader_normal', 'UsdPrimvarReader_point', 'UsdPrimvarReader_string', 'UsdPrimvarReader_vector', 'UsdTransform2d', 'UsdUVTexture']
