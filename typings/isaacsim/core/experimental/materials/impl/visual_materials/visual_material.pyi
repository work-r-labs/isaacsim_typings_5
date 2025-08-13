from __future__ import annotations
import abc
from abc import ABC
from abc import abstractmethod
import isaacsim.core.experimental.prims.impl.prim
from isaacsim.core.experimental.prims.impl.prim import Prim
from isaacsim.core.experimental.utils import ops as ops_utils
from isaacsim.core.experimental.utils import stage as stage_utils
import numpy as np
import omni as omni
from pxr import Sdf
from pxr import Usd
from pxr import UsdShade
import typing
import warp as wp
__all__: list[str] = ['ABC', 'Prim', 'Sdf', 'Usd', 'UsdShade', 'VisualMaterial', 'abstractmethod', 'np', 'omni', 'ops_utils', 'stage_utils', 'wp']
class VisualMaterial(isaacsim.core.experimental.prims.impl.prim.Prim, abc.ABC):
    """
    Base class for visual materials.
    
        Args:
            paths: Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.
            resolve_paths: Whether to resolve the given paths (true) or use them as is (false).
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'are_of_type'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def _get_material_and_shader(stage: Usd.Stage, path: str) -> tuple[UsdShade.Material | None, UsdShade.Shader | None]:
        """
        Get the material and shader for a given material path.
        """
    @staticmethod
    def _get_material_and_shader_from_material(stage: Usd.Stage, path: str) -> tuple[UsdShade.Material | None, UsdShade.Shader | None]:
        """
        Get the material and shader from a material.
        """
    @staticmethod
    def _get_sdf_type_spec(sdf_type: Sdf.ValueTypeName, sdf_type_class: type) -> tuple[callable, callable, callable, callable]:
        """
        Get helper functions to place, create, set and get values for a given Sdf type.
        """
    @staticmethod
    def _parse_sdf_type(type_name: str | Sdf.ValueTypeName) -> tuple[Sdf.ValueTypeName, type]:
        """
        Parse a Sdf value type name into Sdf type and type class.
        """
    @staticmethod
    def are_of_type(paths: str | Usd.Prim | list[str | Usd.Prim]) -> wp.array:
        """
        Check if the prims at the given paths are valid for creating material instances of this type.
        
                Args:
                    paths: Prim paths (or prims) to check for.
        
                Returns:
                    Boolean flags indicating if the prims are valid for creating material instances (shape ``(N, 1)``).
                
        """
    @staticmethod
    def fetch_instances(paths: str | Usd.Prim | list[str | Usd.Prim]) -> list[VisualMaterial | None]:
        """
        Fetch instances of visual material from prims (or prim paths) at the given paths.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    paths: Prim paths (or prims) to get visual material instances from.
        
                Returns:
                    List of visual material instances or ``None`` if the prim is not a supported visual material type.
        
                Example:
        
                .. code-block:: python
        
                    >>> import omni.kit.commands
                    >>> from isaacsim.core.experimental.materials import VisualMaterial
                    >>>
                    >>> # given a USD stage with the prims at paths /World, /World/A (USD Preview Surface)
                    >>> omni.kit.commands.execute(
                    ...     "CreatePreviewSurfaceMaterialPrim",
                    ...     mtl_path=f"/World/A",
                    ...     select_new_prim=False,
                    ... )  # doctest: +NO_CHECK
                    >>>
                    >>> # fetch visual material instances
                    >>> VisualMaterial.fetch_instances(["/World", "/World/A"])
                    [None, <isaacsim.core.experimental.materials.impl.visual_materials.preview_surface.PreviewSurfaceMaterial object at 0x...>]
                
        """
    def __init__(self, paths: str | list[str], *, resolve_paths: bool = True) -> None:
        ...
    def _get_input_values(self, *, name: str, type_name: str | Sdf.ValueTypeName, indices: list | np.ndarray | wp.array | None = None) -> list | wp.array:
        """
        Get shader input values.
        """
    def _set_input_values(self, *, name: str, values: list | np.ndarray | wp.array, type_name: str | Sdf.ValueTypeName, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set shader input values.
        """
    def get_input_values(self, name: str, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get shaders' input values.
        
                .. warning::
        
                    Inputs are not initialized by default. They must be initialized before being read (see :py:meth:`set_input_values`).
        
                Args:
                    name: Shader input name.
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Values (shape and data type depend on the input name).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    ValueError: If the input name is invalid.
                    RuntimeError: If the shader input is not initialized.
        
                Example:
        
                .. code-block:: python
        
                    >>> from isaacsim.core.experimental.materials import OmniGlassMaterial, OmniPbrMaterial, PreviewSurfaceMaterial
                    >>>
                    >>> # get the glass IOR of all prims (OmniGlass)
                    >>> if isinstance(prims, OmniGlassMaterial):
                    ...     prims.set_input_values(name="glass_ior", values=[1.5])
                    ...     glass_ior = prims.get_input_values(name="glass_ior")
                    >>>
                    >>> # get the metallic amount of all prims (OmniPBR)
                    >>> if isinstance(prims, OmniPbrMaterial):
                    ...     prims.set_input_values(name="metallic_constant", values=[0.5])
                    ...     metallic_constant = prims.get_input_values(name="metallic_constant")
                    >>>
                    >>> # get the opacity of all prims (USD Preview Surface)
                    >>> if isinstance(prims, PreviewSurfaceMaterial):
                    ...     prims.set_input_values(name="opacity", values=[0.1])
                    ...     opacity = prims.get_input_values(name="opacity")
                
        """
    def set_input_values(self, name: str, values: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set shaders' input values.
        
                Args:
                    name: Shader input name.
                    values: Input values (shape and data type depend on the input name).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    ValueError: If the input name is invalid.
        
                Example:
        
                .. code-block:: python
        
                    >>> from isaacsim.core.experimental.materials import OmniGlassMaterial, OmniPbrMaterial, PreviewSurfaceMaterial
                    >>>
                    >>> # set same glass color (green) for all prims (OmniGlass)
                    >>> if isinstance(prims, OmniGlassMaterial):
                    ...     prims.set_input_values(name="glass_color", values=[0.0, 1.0, 0.0])
                    >>>
                    >>> # set the Albedo map (textures) for all prims (OmniPBR)
                    >>> if isinstance(prims, OmniPbrMaterial):
                    ...     prims.set_input_values(name="diffuse_texture", values=[
                    ...         "/local/path/to/texture_0",
                    ...         "/local/path/to/texture_1",
                    ...         "/local/path/to/texture_2",
                    ...     ])
                    >>>
                    >>> # set same diffuse color (red) for all prims (USD Preview Surface)
                    >>> if isinstance(prims, PreviewSurfaceMaterial):
                    ...     prims.set_input_values(name="diffuseColor", values=[1.0, 0.0, 0.0])
                
        """
    @property
    def materials(self) -> list[UsdShade.Material]:
        """
        USD materials encapsulated by the wrapper.
        
                Returns:
                    List of USD materials.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.materials
                    [UsdShade.Material(Usd.Prim(</World/prim_0>)),
                     UsdShade.Material(Usd.Prim(</World/prim_1>)),
                     UsdShade.Material(Usd.Prim(</World/prim_2>))]
                
        """
    @property
    def shaders(self) -> list[UsdShade.Shader]:
        """
        USD shaders encapsulated by the wrapper.
        
                Returns:
                    List of USD shaders.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.shaders
                    [UsdShade.Shader(Usd.Prim(</World/prim_0/Shader>)),
                     UsdShade.Shader(Usd.Prim(</World/prim_1/Shader>)),
                     UsdShade.Shader(Usd.Prim(</World/prim_2/Shader>))]
                
        """
_MSG_PRIM_NOT_VALID: str = 'Instance is not valid. This is most likely because some of the wrapped prims have been removed from the stage, or because the instance has been deleted'
