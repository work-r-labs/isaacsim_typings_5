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
__all__: list[str] = ['OmniGlassMaterial', 'Sdf', 'Usd', 'VisualMaterial', 'omni', 'ops_utils', 'stage_utils', 'wp']
class OmniGlassMaterial(isaacsim.core.experimental.materials.impl.visual_materials.visual_material.VisualMaterial):
    """
    High level wrapper for creating/encapsulating Omniverse Glass (``OmniGlass``) material prims.
    
        The ``OmniGlass`` is an improved physical glass model that simulates light transmission
        through thin walled and transmissive surfaces.
    
        .. note::
    
            This class creates or wraps (one of both) OmniGlass prims according to the following rules:
    
            * If the prim paths exist, a wrapper is placed over the OmniGlass prims.
            * If the prim paths do not exist, OmniGlass prims are created at each path and a wrapper is placed over them.
    
        On visual materials, the shader parameters are encoded as inputs.
        The following tables summarize the ``OmniGlass`` material shader inputs (by group):
    
        .. list-table:: Color
            :header-rows: 1
    
            * - Input name
              - Description
              - Shape / Length
              - Type
            * - ``"glass_color"``
              - Color of the glass.
              - ``(N, 3)``
              - ``float``
            * - ``"glass_color_texture"``
              - Texture to be used for the glass color.
              - ``(N,)``
              - ``str``
            * - ``"depth"``
              - Volume absorption scale (control how much light is absorbed through the surface).
              - ``(N, 1)``
              - ``float``
    
        .. list-table:: Roughness
            :header-rows: 1
    
            * - Input name
              - Description
              - Shape / Length
              - Type
            * - ``"frosting_roughness"``
              - Roughness of the glass material.
              - ``(N, 1)``
              - ``float``
            * - ``"roughness_texture_influence"``
              - Influence of the roughness texture on the glass material.
              - ``(N, 1)``
              - ``float``
            * - ``"roughness_texture"``
              - Roughness texture.
              - ``(N,)``
              - ``str``
    
        .. list-table:: Refraction
            :header-rows: 1
    
            * - Input name
              - Description
              - Shape / Length
              - Type
            * - ``"glass_ior"``
              - Glass Index of refraction (IOR).
              - ``(N, 1)``
              - ``float``
            * - ``"thin_walled"``
              - Whether the glass is thin-walled (when enabled, the material is considered thin-walled).
              - ``(N, 1)``
              - ``bool``
    
        .. list-table:: Reflection
            :header-rows: 1
    
            * - Input name
              - Description
              - Shape / Length
              - Type
            * - ``"reflection_color_texture"``
              - Reflection color texture.
              - ``(N,)``
              - ``str``
            * - ``"reflection_color"``
              - Reflection color.
              - ``(N, 3)``
              - ``float``
    
        .. list-table:: Normal
            :header-rows: 1
    
            * - Input name
              - Description
              - Shape / Length
              - Type
            * - ``"normal_map_texture"``
              - Normal map texture.
              - ``(N,)``
              - ``str``
            * - ``"normal_map_strength"``
              - Strength of the normal map.
              - ``(N, 1)``
              - ``float``
            * - ``"geometry_normal_roughness_strength"``
              - Normal map to roughness weight (enables and weights roughness induced by normal maps).
              - ``(N, 1)``
              - ``float``
            * - ``"flip_tangent_u"``
              - Flip tangent U.
              - ``(N, 1)``
              - ``bool``
            * - ``"flip_tangent_v"``
              - Flip tangent V.
              - ``(N, 1)``
              - ``bool``
    
        .. list-table:: Opacity
            :header-rows: 1
    
            * - Input name
              - Description
              - Shape / Length
              - Type
            * - ``"enable_opacity"``
              - Enable the use of cutout opacity.
              - ``(N, 1)``
              - ``bool``
            * - ``"cutout_opacity"``
              - Opacity value between 0.0 and 1.0, when opacity map is not valid.
              - ``(N, 1)``
              - ``float``
            * - ``"cutout_opacity_texture"``
              - Opacity map.
              - ``(N,)``
              - ``str``
            * - ``"cutout_opacity_mono_source"``
              - Determines how to lookup opacity from the supplied texture.
              - ``(N, 1)``
              - ``int``
            * - ``"opacity_threshold"``
              - Opacity threshold.
              - ``(N, 1)``
              - ``float``
    
        .. list-table:: UV
            :header-rows: 1
    
            * - Input name
              - Description
              - Shape / Length
              - Type
            * - ``"project_uvw"``
              - Enable Project UVW Coordinates (UV coordinates will be generated by projecting them from a coordinate system).
              - ``(N, 1)``
              - ``bool``
            * - ``"world_or_object"``
              - Enable world space (when enabled, uses world space for projection, otherwise object space is used).
              - ``(N, 1)``
              - ``bool``
            * - ``"uv_space_index"``
              - UV space index.
              - ``(N, 1)``
              - ``int``
            * - ``"texture_translate"``
              - Controls position of texture.
              - ``(N, 2)``
              - ``float``
            * - ``"texture_rotate"``
              - Rotates angle of texture (in degrees).
              - ``(N, 1)``
              - ``float``
            * - ``"texture_scale"``
              - Controls the repetition of the texture.
              - ``(N, 2)``
              - ``float``
    
        Args:
            paths: Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.
    
        Raises:
            ValueError: If resulting paths are mixed or invalid.
    
        Example:
    
        .. code-block:: python
    
            >>> from isaacsim.core.experimental.materials import OmniGlassMaterial
            >>>
            >>> # given an empty USD stage with the /World Xform prim,
            >>> # create visual material at paths: /World/prim_0, /World/prim_1, and /World/prim_2
            >>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
            >>> prims = OmniGlassMaterial(paths)  # doctest: +NO_CHECK
        
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
                    >>> result = OmniGlassMaterial.are_of_type(["/World", "/World/prim_0"])
                    >>> print(result)
                    [[False]
                     [ True]]
                
        """
    def __init__(self, paths: str | list[str]) -> None:
        ...
