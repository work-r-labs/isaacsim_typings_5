from __future__ import annotations
import isaacsim.core.experimental.materials.impl.visual_materials.visual_material
from isaacsim.core.experimental.materials.impl.visual_materials.visual_material import VisualMaterial
from isaacsim.core.experimental.utils import ops as ops_utils
from isaacsim.core.experimental.utils import stage as stage_utils
import omni as omni
from pxr import Sdf
from pxr import Usd
import typing
import warp as wp
__all__: list[str] = ['PreviewSurfaceMaterial', 'Sdf', 'Usd', 'VisualMaterial', 'omni', 'ops_utils', 'stage_utils', 'wp']
class PreviewSurfaceMaterial(isaacsim.core.experimental.materials.impl.visual_materials.visual_material.VisualMaterial):
    """
    High level wrapper for creating/encapsulating USD Preview Surface (``UsdPreviewSurface``) material prims.
    
        The ``UsdPreviewSurface`` is intended to model a modern physically based surface that strikes a balance between
        expressiveness and reliable interchange between engines and real-time rendering clients.
    
        .. note::
    
            This class creates or wraps (one of both) USD Preview Surface prims according to the following rules:
    
            * If the prim paths exist, a wrapper is placed over the USD Preview Surface prims.
            * If the prim paths do not exist, USD Preview Surface prims are created at each path and a wrapper is placed over them.
    
        On visual materials, the shader parameters are encoded as inputs.
        The following table summarizes the ``UsdPreviewSurface`` material shader inputs:
    
        .. list-table::
            :header-rows: 1
    
            * - Input name
              - Description
              - Shape / Length
              - Type
            * - ``"diffuseColor"``
              - Color reflected from the material surface when light hits it.
              - ``(N, 3)``
              - ``float``
            * - ``"emissiveColor"``
              - Color of the light emitted by the material.
              - ``(N, 3)``
              - ``float``
            * - ``"specularColor"``
              - Color of the highlights that appear on a surface when it reflects light.
              - ``(N, 3)``
              - ``float``
            * - ``"useSpecularWorkflow"``
              - Operation mode (specular workflow: 1, metallic workflow: 0).
              - ``(N, 1)``
              - ``int``
            * - ``"metallic"``
              - Metallic (1.0 for metallic surfaces and 0.0 for non-metallic surfaces, in between for mixed surfaces).
              - ``(N, 1)``
              - ``float``
            * - ``"roughness"``
              - Roughness (specular lobe).
              - ``(N, 1)``
              - ``float``
            * - ``"clearcoat"``
              - Clearcoat (second specular lobe amount).
              - ``(N, 1)``
              - ``float``
            * - ``"clearcoatRoughness"``
              - Clearcoat roughness (second specular lobe roughness).
              - ``(N, 1)``
              - ``float``
            * - ``"opacity"``
              - Opacity (0.0 for fully transparent, 1.0 for fully opaque, in between for translucent).
              - ``(N, 1)``
              - ``float``
            * - ``"opacityThreshold"``
              - Opacity threshold.
              - ``(N, 1)``
              - ``float``
            * - ``"ior"``
              - Index of refraction (IOR).
              - ``(N, 1)``
              - ``float``
            * - ``"normal"``
              - Normal vector.
              - ``(N, 3)``
              - ``float``
            * - ``"displacement"``
              - Displacement (in the direction of the normal).
              - ``(N, 1)``
              - ``float``
    
        Args:
            paths: Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.
    
        Raises:
            ValueError: If resulting paths are mixed or invalid.
    
        Example:
    
        .. code-block:: python
    
            >>> from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
            >>>
            >>> # given an empty USD stage with the /World Xform prim,
            >>> # create visual material at paths: /World/prim_0, /World/prim_1, and /World/prim_2
            >>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
            >>> prims = PreviewSurfaceMaterial(paths)  # doctest: +NO_CHECK
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def are_of_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array:
        """
        Check if the prims at the given paths are valid for creating material instances of this type.
        
                Backends: :guilabel:`usd`.
        
                .. warning::
        
                    Since this method is static, the output is always on the CPU.
        
                Args:
                    paths: Prim paths (or prims) to check for.
        
                Returns:
                    Boolean flags indicating if the prims are valid for creating material instances (shape ``(N, 1)``).
        
                Example:
        
                .. code-block:: python
        
                    >>> # check if the following prims at paths are valid for creating instances
                    >>> result = PreviewSurfaceMaterial.are_of_type(["/World", "/World/prim_0"])
                    >>> print(result)
                    [[False]
                     [ True]]
                
        """
    def __init__(self, paths: str | list[str]) -> None:
        ...
