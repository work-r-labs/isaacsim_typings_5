from __future__ import annotations
import carb as carb
from isaacsim.core.experimental.prims.impl import _fabric
import isaacsim.core.experimental.prims.impl.prim
from isaacsim.core.experimental.prims.impl.prim import Prim
from isaacsim.core.experimental.utils import backend as backend_utils
from isaacsim.core.experimental.utils import ops as ops_utils
from isaacsim.core.experimental.utils import stage as stage_utils
from isaacsim.core.simulation_manager.impl.simulation_manager import SimulationManager
from isaacsim.core.utils import numpy as numpy_utils
from isaacsim.core.utils.prims import is_prim_non_root_articulation_link
import numpy as np
from pxr import Gf
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdShade
import typing
import usdrt as usdrt
import warp as wp
__all__: list[str] = ['Gf', 'Prim', 'SimulationManager', 'Usd', 'UsdGeom', 'UsdShade', 'XformPrim', 'backend_utils', 'carb', 'is_prim_non_root_articulation_link', 'np', 'numpy_utils', 'ops_utils', 'stage_utils', 'usdrt', 'wp']
class XformPrim(isaacsim.core.experimental.prims.impl.prim.Prim):
    """
    High level wrapper for manipulating ``Xform`` prims and their attributes.
    
        This class is a wrapper over one or more USD ``Xform`` prims in the stage to provide
        high-level functionality for manipulating transformations and other attributes.
        The prims are specified using paths that can include regular expressions for matching multiple prims.
    
        Args:
            paths: Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.
            resolve_paths: Whether to resolve the given paths (true) or use them as is (false).
            positions: Positions in the world frame (shape ``(N, 3)``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            translations: Translations in the local frame (shape ``(N, 3)``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            orientations: Orientations in the world frame (shape ``(N, 4)``, quaternion ``wxyz``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            scales: Scales to be applied to the prims (shape ``(N, 3)``).
                If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
            reset_xform_op_properties: Whether to reset the transformation operation attributes of the prims to a standard set.
                See :py:meth:`reset_xform_op_properties` for more details.
    
        Raises:
            ValueError: If no prims are found matching the specified path(s).
            AssertionError: If both positions and translations are specified.
    
        Example:
    
        .. code-block:: python
    
            >>> import numpy as np
            >>> from isaacsim.core.experimental.prims import XformPrim
            >>>
            >>> # given a USD stage with the Xform prims: /World/prim_0, /World/prim_1, and /World/prim_2
            >>> # - create wrapper over single prim
            >>> prim = XformPrim("/World/prim_0")  # doctest: +NO_CHECK
            >>> # - create wrapper over multiple prims using regex
            >>> prims = XformPrim("/World/prim_.*")  # doctest: +NO_CHECK
            >>> prims.reset_xform_op_properties()
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, paths: str | list[str], *, resolve_paths: bool = True, positions: list | np.ndarray | wp.array | None = None, translations: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, scales: list | np.ndarray | wp.array | None = None, reset_xform_op_properties: bool = False) -> None:
        ...
    def _ensure_fabric_data(self, key: str) -> dict:
        """
        Ensure fabric-related data is initialized.
        """
    def _get_fabric_hierarchy(self) -> usdrt.hierarchy.IFabricHierarchy:
        """
        Get the IFabricHierarchy interface.
        """
    def apply_visual_materials(self, materials: type['VisualMaterial'] | list[type['VisualMaterial']], *, weaker_than_descendants: list | np.ndarray | wp.array | None = None, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Apply visual materials to the prims, and optionally, to their descendants.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    visual_materials: Visual materials to be applied to the prims (shape ``(N,)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    weaker_than_descendants: Boolean flags to indicate whether descendant materials should be overridden (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> from isaacsim.core.experimental.materials import OmniGlassMaterial
                    >>>
                    >>> # create a dark-red glass visual material
                    >>> material = OmniGlassMaterial("/World/material/glass")
                    >>> material.set_input_values("glass_ior", [1.25])
                    >>> material.set_input_values("depth", [0.001])
                    >>> material.set_input_values("thin_walled", [False])
                    >>> material.set_input_values("glass_color", [0.5, 0.0, 0.0])
                    >>>
                    >>> prims.apply_visual_materials(material)
                
        """
    def get_applied_visual_materials(self, *, indices: list | np.ndarray | wp.array | None = None) -> list[type['VisualMaterial'] | None]:
        """
        Get the applied visual materials.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    List of applied visual materials (shape ``(N,)``). If a prim does not have a material, ``None`` is returned.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the applied visual material of the last wrapped prim
                    >>> prims.get_applied_visual_materials(indices=[2])[0]
                    <isaacsim.core.experimental.materials.impl.visual_materials.omni_glass.OmniGlassMaterial object at 0x...>
                
        """
    def get_default_state(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array | None, wp.array | None]:
        """
        Get the default state (positions and orientations) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Two-elements tuple. 1) The default positions in the world frame (shape ``(N, 3)``).
                    2) The default orientations in the world frame (shape ``(N, 4)``, quaternion ``wxyz``).
                    If the default state is not set using the :py:meth:`set_default_state` method, ``None`` is returned.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: If prims are non-root articulation links.
                
        """
    def get_local_poses(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array]:
        """
        Get the poses (translations and orientations) in the local frame of the prims.
        
                Backends: :guilabel:`usd`, :guilabel:`usdrt`, :guilabel:`fabric`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Two-elements tuple. 1) The translations in the local frame (shape ``(N, 3)``).
                    2) The orientations in the local frame (shape ``(N, 4)``, quaternion ``wxyz``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the local poses of all prims
                    >>> translations, orientations = prims.get_local_poses()
                    >>> translations.shape, orientations.shape
                    ((3, 3), (3, 4))
                    >>>
                    >>> # get the local pose of the first prim
                    >>> translations, orientations = prims.get_local_poses(indices=[0])
                    >>> translations.shape, orientations.shape
                    ((1, 3), (1, 4))
                
        """
    def get_local_scales(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the local scales of the prims.
        
                Backends: :guilabel:`usd`, :guilabel:`usdrt`, :guilabel:`fabric`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Scales of the prims (shape ``(N, 3)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get local scales of all prims
                    >>> scales = prims.get_local_scales()
                    >>> scales.shape
                    (3, 3)
                
        """
    def get_visibilities(self, *, indices: list | np.ndarray | wp.array | None = None) -> wp.array:
        """
        Get the visibility state (whether prims are visible or invisible during rendering) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Boolean flags indicating the visibility state (shape ``(N, 1)``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the visibility states of all prims
                    >>> visibilities = prims.get_visibilities()
                    >>> visibilities.list()
                    [True, True, True]
                    >>>
                    >>> # get the visibility states of the first and last prims
                    >>> visibilities = prims.get_visibilities(indices=[0, 2])
                    >>> visibilities.list()
                    [True, True]
                
        """
    def get_world_poses(self, *, indices: list | np.ndarray | wp.array | None = None) -> tuple[wp.array, wp.array]:
        """
        Get the poses (positions and orientations) in the world frame of the prims.
        
                Backends: :guilabel:`usd`, :guilabel:`usdrt`, :guilabel:`fabric`.
        
                Args:
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Returns:
                    Two-elements tuple. 1) The positions in the world frame (shape ``(N, 3)``).
                    2) The orientations in the world frame (shape ``(N, 4)``, quaternion ``wxyz``).
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the world poses of all prims
                    >>> positions, orientations = prims.get_world_poses()
                    >>> positions.shape, orientations.shape
                    ((3, 3), (3, 4))
                    >>>
                    >>> # get the world pose of the first prim
                    >>> positions, orientations = prims.get_world_poses(indices=[0])
                    >>> positions.shape, orientations.shape
                    ((1, 3), (1, 4))
                
        """
    def reset_to_default_state(self, *, warn_on_non_default_state: bool = False) -> None:
        """
        Reset the prims to the specified default state.
        
                Backends: :guilabel:`usd`, :guilabel:`usdrt`, :guilabel:`fabric`.
        
                This method applies the default state defined using the :py:meth:`set_default_state` method.
        
                .. note::
        
                    This method *teleports* prims to the specified default state (positions and orientations).
        
                .. warning::
        
                    This method has no effect on non-root articulation links or when no default state is set.
                    In this case, a warning message is logged if ``warn_on_non_default_state`` is ``True``.
        
                Args:
                    warn_on_non_default_state: Whether to log a warning message when no default state is set.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get default state (no default state set at this point)
                    >>> prims.get_default_state()
                    (None, None)
                    >>>
                    >>> # set default state
                    >>> # - random positions for each prim
                    >>> # - same fixed orientation for all prim
                    >>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
                    >>> prims.set_default_state(positions, orientations=[1.0, 0.0, 0.0, 0.0])
                    >>>
                    >>> # get default state (default state is set)
                    >>> prims.get_default_state()
                    (array(shape=(3, 3), dtype=float32), array(shape=(3, 4), dtype=float32))
                    >>>
                    >>> # reset prims to default state
                    >>> prims.reset_to_default_state()
                
        """
    def reset_xform_op_properties(self) -> None:
        """
        Reset the transformation operation attributes of the prims to a standard set.
        
                Backends: :guilabel:`usd`.
        
                It ensures that each prim has only the following transformations in the specified order.
                Any other transformation operations are removed, so they are not consumed.
        
                1. ``xformOp:translate`` (double precision)
                2. ``xformOp:orient`` (double precision)
                3. ``xformOp:scale`` (double precision)
        
                .. note::
        
                    This method preserves the poses of the prims in the world frame while reorganizing the transformation operations.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # reset transform operations of all prims
                    >>> prims.reset_xform_op_properties()
                    >>>
                    >>> # verify transform operations of the first wrapped prim
                    >>> prims.prims[0].GetPropertyNames()
                    [... 'xformOp:orient', 'xformOp:scale', 'xformOp:translate', 'xformOpOrder']
                
        """
    def set_default_state(self, positions: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the default state (positions and orientations) of the prims.
        
                Backends: :guilabel:`usd`.
        
                .. hint::
        
                    Prims can be reset to their default state by calling the :py:meth:`reset_to_default_state` method.
        
                Args:
                    positions: Default positions in the world frame (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    orientations: Default orientations in the world frame (shape ``(N, 4)``, quaternion ``wxyz``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: If neither positions nor orientations are specified.
                    AssertionError: Wrapped prims are not valid.
                    AssertionError: If prims are non-root articulation links.
                
        """
    def set_local_poses(self, translations: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the poses (translations and orientations) in the local frame of the prims.
        
                Backends: :guilabel:`usd`, :guilabel:`usdrt`, :guilabel:`fabric`.
        
                .. note::
        
                    This method *teleports* prims to the specified poses.
        
                Args:
                    translations: Translations in the local frame (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    orientations: Orientations in the local frame (shape ``(N, 4)``, quaternion ``wxyz``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: If neither translations nor orientations are specified.
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set random poses for all prims
                    >>> translations = np.random.uniform(low=-1, high=1, size=(3, 3))
                    >>> orientations = np.random.randn(3, 4)
                    >>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True)  # normalize quaternions
                    >>> prims.set_local_poses(translations, orientations)
                
        """
    def set_local_scales(self, scales: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the local scales of the prims.
        
                Backends: :guilabel:`usd`, :guilabel:`usdrt`, :guilabel:`fabric`.
        
                Args:
                    scales: Scales to be applied to the prims (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set random positive scales for all prims
                    >>> scales = np.random.uniform(low=0.5, high=1.5, size=(3, 3))
                    >>> prims.set_local_scales(scales)
                
        """
    def set_visibilities(self, visibilities: list | np.ndarray | wp.array, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the visibility state (whether prims are visible or invisible during rendering) of the prims.
        
                Backends: :guilabel:`usd`.
        
                Args:
                    visibilities: Boolean flags to set the visibility state (shape ``(N, 1)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # make all prims invisible
                    >>> prims.set_visibilities([False])
                    >>>
                    >>> # make first and last prims invisible
                    >>> prims.set_visibilities([True])  # restore visibility from previous call
                    >>> prims.set_visibilities([False], indices=[0, 2])
                
        """
    def set_world_poses(self, positions: list | np.ndarray | wp.array | None = None, orientations: list | np.ndarray | wp.array | None = None, *, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set the poses (positions and orientations) in the world frame of the prims.
        
                Backends: :guilabel:`usd`, :guilabel:`usdrt`, :guilabel:`fabric`.
        
                .. note::
        
                    This method *teleports* prims to the specified poses.
        
                Args:
                    positions: Positions in the world frame (shape ``(N, 3)``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    orientations: Orientations in the world frame (shape ``(N, 4)``, quaternion ``wxyz``).
                        If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).
                    indices: Indices of prims to process (shape ``(N,)``). If not defined, all wrapped prims are processed.
        
                Raises:
                    AssertionError: If neither positions nor orientations are specified.
                    AssertionError: Wrapped prims are not valid.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set random poses for all prims
                    >>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
                    >>> orientations = np.random.randn(3, 4)
                    >>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True)  # normalize quaternions
                    >>> prims.set_world_poses(positions, orientations)
                
        """
    @property
    def is_non_root_articulation_link(self) -> bool:
        """
        Indicate if the wrapped prims are a non-root link in an articulation tree.
        
                Backends: :guilabel:`usd`.
        
                .. warning::
        
                    Transformation of the poses of non-root links in an articulation tree are not supported.
        
                Returns:
                    Whether the prims are a non-root link in an articulation tree.
                
        """
_MSG_PRIM_NOT_VALID: str = 'Instance is not valid. This is most likely because some of the wrapped prims have been removed from the stage, or because the instance has been deleted'
