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
__all__: list[str] = ['OmniPbrMaterial', 'Sdf', 'Usd', 'VisualMaterial', 'omni', 'ops_utils', 'stage_utils', 'wp']
class OmniPbrMaterial(isaacsim.core.experimental.materials.impl.visual_materials.visual_material.VisualMaterial):
    """
    High level wrapper for creating/encapsulating Omniverse Physically-Based Rendering (``OmniPBR``) material prims.
    
        The ``OmniPBR`` is the default Physically based material available in Omniverse.
        This material can describe most opaque dielectric or non-dielectric materials.
    
        .. note::
    
            This class creates or wraps (one of both) OmniPBR prims according to the following rules:
    
            * If the prim paths exist, a wrapper is placed over the OmniPBR prims.
            * If the prim paths do not exist, OmniPBR prims are created at each path and a wrapper is placed over them.
    
        On visual materials, the shader parameters are encoded as inputs.
        The following tables summarize the ``OmniPBR`` material shader inputs (by group):
    
        .. list-table:: Albedo
            :header-rows: 1
    
            * - Input name
              - Description
              - Shape / Length
              - Type
            * - ``"diffuse_color_constant"``
              - Albedo base color.
              - ``(N, 3)``
              - ``float``
            * - ``"diffuse_texture"``
              - Albedo map.
              - ``(N,)``
              - ``str``
            * - ``"albedo_desaturation"``
              - Albedo map desaturation.
              - ``(N, 1)``
              - ``float``
            * - ``"albedo_add"``
              - Adds constant value to the diffuse color.
              - ``(N, 1)``
              - ``float``
            * - ``"albedo_brightness"``
              - Multiplier for the diffuse color.
              - ``(N, 1)``
              - ``float``
            * - ``"diffuse_tint"``
              - Color tint (when enabled, this color value is multiplied over the final albedo color).
              - ``(N, 3)``
              - ``float``
    
        .. list-table:: Reflectivity
            :header-rows: 1
    
            * - Input name
              - Description
              - Shape / Length
              - Type
            * - ``"reflection_roughness_constant"``
              - Roughness amount (Higher values lead to more blurry reflections).
              - ``(N, 1)``
              - ``float``
            * - ``"reflection_roughness_texture_influence"``
              - Roughness map influence (blends between the constant value and the lookup of the roughness texture).
              - ``(N, 1)``
              - ``float``
            * - ``"reflectionroughness_texture"``
              - Roughness map.
              - ``(N,)``
              - ``str``
            * - ``"metallic_constant"``
              - Metallic amount.
              - ``(N, 1)``
              - ``float``
            * - ``"metallic_texture_influence"``
              - Metallic map influence (blends between the constant value and the lookup of the metallic texture).
              - ``(N, 1)``
              - ``float``
            * - ``"metallic_texture"``
              - Metallic map.
              - ``(N,)``
              - ``str``
            * - ``"specular_level"``
              - Specular level (intensity) of the material.
              - ``(N, 1)``
              - ``float``
            * - ``"enable_ORM_texture"``
              - Enable ORM texture (extracts occlusion, roughness and metallic textures from the RGB channels).
              - ``(N, 1)``
              - ``bool``
            * - ``"ORM_texture"``
              - ORM map (texture that has occlusion, roughness and metallic maps stored in the RGB channels).
              - ``(N,)``
              - ``str``
    
        .. list-table:: Ambient Occlusion (AO)
            :header-rows: 1
    
            * - Input name
              - Description
              - Shape / Length
              - Type
            * - ``"ao_to_diffuse"``
              - AO to diffuse (amount of ambient occlusion multiplied against the diffuse color channel).
              - ``(N, 1)``
              - ``float``
            * - ``"ao_texture"``
              - Ambient occlusion map (texture for the material).
              - ``(N,)``
              - ``str``
    
        .. list-table:: Emissive
            :header-rows: 1
    
            * - Input name
              - Description
              - Shape / Length
              - Type
            * - ``"enable_emission"``
              - Enable emission (enables the emission of light from the material).
              - ``(N, 1)``
              - ``bool``
            * - ``"emissive_color"``
              - Emission color.
              - ``(N, 3)``
              - ``float``
            * - ``"emissive_color_texture"``
              - Emission color map.
              - ``(N,)``
              - ``str``
            * - ``"emissive_mask_texture"``
              - Emission color mask map.
              - ``(N,)``
              - ``str``
            * - ``"emissive_intensity"``
              - Emission intensity.
              - ``(N, 1)``
              - ``float``
    
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
            * - ``"opacity_texture"``
              - Opacity map.
              - ``(N,)``
              - ``str``
            * - ``"opacity_constant"``
              - Opacity amount (between 0.0 and 1.0, when opacity map is not valid).
              - ``(N, 1)``
              - ``float``
            * - ``"enable_opacity_texture"``
              - Enable or disable the usage of the opacity texture map.
              - ``(N, 1)``
              - ``bool``
            * - ``"opacity_mode"``
              - Determines how to lookup opacity from the supplied texture.
              - ``(N, 1)``
              - ``int``
            * - ``"opacity_threshold"``
              - Opacity threshold (between 0.0 and 1.0).
              - ``(N, 1)``
              - ``float``
    
        .. list-table:: Normal
            :header-rows: 1
    
            * - Input name
              - Description
              - Shape / Length
              - Type
            * - ``"geometry_normal_roughness_strength"``
              - Normal map to roughness weight (enables and weights roughness induced by normal maps).
              - ``(N, 1)``
              - ``float``
            * - ``"bump_factor"``
              - Normal strength.
              - ``(N, 1)``
              - ``float``
            * - ``"normalmap_texture"``
              - Normal map.
              - ``(N,)``
              - ``str``
            * - ``"detail_bump_factor"``
              - Detail normal strength.
              - ``(N, 1)``
              - ``float``
            * - ``"detail_normalmap_texture"``
              - Detail normal map.
              - ``(N,)``
              - ``str``
            * - ``"flip_tangent_u"``
              - Flip tangent U.
              - ``(N, 1)``
              - ``bool``
            * - ``"flip_tangent_v"``
              - Flip tangent V.
              - ``(N, 1)``
              - ``bool``
    
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
            * - ``"detail_texture_translate"``
              - Controls the position of the detail texture.
              - ``(N, 2)``
              - ``float``
            * - ``"detail_texture_rotate"``
              - Rotates angle of the detail texture (in degrees).
              - ``(N, 1)``
              - ``float``
            * - ``"detail_texture_scale"``
              - Controls the repetition of the detail texture.
              - ``(N, 2)``
              - ``float``
    
        .. list-table:: Geometry
            :header-rows: 1
    
            * - Input name
              - Description
              - Shape / Length
              - Type
            * - ``"round_edges_radius"``
              - Influence radius around the edges (in meters).
              - ``(N, 1)``
              - ``float``
            * - ``"round_edges_roundness"``
              - Determines how round the edge will look.
              - ``(N, 1)``
              - ``float``
            * - ``"round_edges_across_materials"``
              - Round edge across materials.
              - ``(N, 1)``
              - ``bool``
    
        Args:
            paths: Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.
    
        Raises:
            ValueError: If resulting paths are mixed or invalid.
    
        Example:
    
        .. code-block:: python
    
            >>> from isaacsim.core.experimental.materials import OmniPbrMaterial
            >>>
            >>> # given an empty USD stage with the /World Xform prim,
            >>> # create visual material at paths: /World/prim_0, /World/prim_1, and /World/prim_2
            >>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
            >>> prims = OmniPbrMaterial(paths)  # doctest: +NO_CHECK
        
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
                    >>> result = OmniPbrMaterial.are_of_type(["/World", "/World/prim_0"])
                    >>> print(result)
                    [[False]
                     [ True]]
                
        """
    def __init__(self, paths: str | list[str]) -> None:
        ...
