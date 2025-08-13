from __future__ import annotations
from isaacsim.core.experimental.utils.impl import stage as stage_utils
from pxr import Usd
import typing
import usdrt as usdrt
__all__: list[str] = ['Usd', 'get_all_matching_child_prims', 'get_first_matching_child_prim', 'get_first_matching_parent_prim', 'get_prim_at_path', 'get_prim_path', 'get_prim_variant_collection', 'get_prim_variants', 'has_api', 'set_prim_variants', 'stage_utils', 'usdrt']
def get_all_matching_child_prims(prim: str | Usd.Prim | usdrt.Usd.Prim, *, predicate: typing.Callable[[Usd.Prim | usdrt.Usd.Prim, str], bool], include_self: bool = False, max_depth: int | None = None) -> list[Usd.Prim | usdrt.Usd.Prim]:
    """
    Get all prim children of the given prim (excluding itself by default) that pass the predicate.
    
        Backends: :guilabel:`usd`, :guilabel:`usdrt`, :guilabel:`fabric`.
    
        Args:
            prim: Prim path or prim instance.
            predicate: Function to test the prims against.
                The function should take two positional arguments: a prim instance and its path.
                The function should return a boolean value indicating whether a prim passes the predicate.
            include_self: Whether to include the given prim in the search.
            max_depth: Maximum depth to search (current prim is at depth 0). If ``None``, search till the end of the tree.
    
        Returns:
            List of matching prim children.
    
        Raises:
            ValueError: If ``max_depth`` is defined and is less than 0.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.experimental.utils.prim as prim_utils
            >>> import isaacsim.core.experimental.utils.stage as stage_utils
            >>>
            >>> # define some prims
            >>> stage_utils.define_prim("/World/Cube_0", "Cube")  # doctest: +NO_CHECK
            >>> stage_utils.define_prim("/World/Cube_0/Cube_1", "Cube")  # doctest: +NO_CHECK
            >>>
            >>> # get all `/World`'s child prims of type Cube
            >>> predicate = lambda prim, path: prim.GetTypeName() == "Cube"
            >>> prim_utils.get_all_matching_child_prims("/World", predicate=predicate)
            [Usd.Prim(</World/Cube_0>), Usd.Prim(</World/Cube_0/Cube_1>)]
            >>>
            >>> # get all `/World`'s child prims of type Cube with max depth 1
            >>> prim_utils.get_all_matching_child_prims("/World", predicate=predicate, max_depth=1)
            [Usd.Prim(</World/Cube_0>)]
        
    """
def get_first_matching_child_prim(prim: str | Usd.Prim | usdrt.Usd.Prim, *, predicate: typing.Callable[[Usd.Prim | usdrt.Usd.Prim, str], bool], include_self: bool = False) -> Usd.Prim | usdrt.Usd.Prim | None:
    """
    Get the first prim child of the given prim (excluding itself by default) that passes the predicate.
    
        Backends: :guilabel:`usd`, :guilabel:`usdrt`, :guilabel:`fabric`.
    
        Args:
            prim: Prim path or prim instance.
            predicate: Function to test the prims against.
                The function should take two positional arguments: a prim instance and its path.
                The function should return a boolean value indicating whether a prim passes the predicate.
            include_self: Whether to include the given prim in the search.
    
        Returns:
            First prim child or ``None`` if no prim child passes the predicate.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.experimental.utils.prim as prim_utils
            >>> import isaacsim.core.experimental.utils.stage as stage_utils
            >>>
            >>> # define some prims
            >>> stage_utils.define_prim("/World/Cube", "Cube")  # doctest: +NO_CHECK
            >>> stage_utils.define_prim("/World/Cylinder", "Cylinder")  # doctest: +NO_CHECK
            >>> stage_utils.define_prim("/World/Sphere", "Sphere")  # doctest: +NO_CHECK
            >>>
            >>> # get the first `/World`'s child prim of type Sphere
            >>> predicate = lambda prim, path: prim.GetTypeName() == "Sphere"
            >>> prim_utils.get_first_matching_child_prim("/World", predicate=predicate)
            Usd.Prim(</World/Sphere>)
        
    """
def get_first_matching_parent_prim(prim: str | Usd.Prim | usdrt.Usd.Prim, *, predicate: typing.Callable[[Usd.Prim | usdrt.Usd.Prim, str], bool], include_self: bool = False) -> Usd.Prim | usdrt.Usd.Prim | None:
    """
    Get the first prim parent of the given prim (excluding itself by default) that passes the predicate.
    
        Backends: :guilabel:`usd`, :guilabel:`usdrt`, :guilabel:`fabric`.
    
        .. warning::
    
            The root prim (``/``) is not considered a valid parent prim but a pseudo-root prim.
            Therefore, it is not taken into account by this function, and any match for this prim will return ``None``.
    
        Args:
            prim: Prim path or prim instance.
            predicate: Function to test the prims against.
                The function should take two positional arguments: a prim instance and its path.
                The function should return a boolean value indicating whether a prim passes the predicate.
            include_self: Whether to include the given prim in the search.
    
        Returns:
            First prim parent or ``None`` if no prim parent passes the predicate.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.experimental.utils.prim as prim_utils
            >>> import isaacsim.core.experimental.utils.stage as stage_utils
            >>>
            >>> # define some nested prims
            >>> stage_utils.define_prim("/World/Cube", "Cube")  # doctest: +NO_CHECK
            >>> stage_utils.define_prim("/World/Cube/Cylinder", "Cylinder")  # doctest: +NO_CHECK
            >>> stage_utils.define_prim("/World/Cube/Cylinder/Sphere", "Sphere")  # doctest: +NO_CHECK
            >>>
            >>> # get the first `Sphere`'s parent prim of type Cube
            >>> predicate = lambda prim, path: prim.GetTypeName() == "Cube"
            >>> prim_utils.get_first_matching_parent_prim("/World/Cube/Cylinder/Sphere", predicate=predicate)
            Usd.Prim(</World/Cube>)
        
    """
def get_prim_at_path(path: str) -> Usd.Prim | usdrt.Usd.Prim:
    """
    Get the prim at a given path.
    
        Backends: :guilabel:`usd`, :guilabel:`usdrt`, :guilabel:`fabric`.
    
        Args:
            path: Prim path.
    
        Returns:
            Prim.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.experimental.utils.prim as prim_utils
            >>> import isaacsim.core.experimental.utils.stage as stage_utils
            >>>
            >>> stage_utils.define_prim(f"/World/Cube", "Cube")  # doctest: +NO_CHECK
            >>>
            >>> prim_utils.get_prim_at_path("/World/Cube")
            Usd.Prim(</World/Cube>)
        
    """
def get_prim_path(prim: Usd.Prim | usdrt.Usd.Prim) -> str:
    """
    Get the path of a given prim.
    
        Backends: :guilabel:`usd`, :guilabel:`usdrt`, :guilabel:`fabric`.
    
        Args:
            prim: Prim instance.
    
        Returns:
            Prim path.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.experimental.utils.prim as prim_utils
            >>> import isaacsim.core.experimental.utils.stage as stage_utils
            >>>
            >>> prim = stage_utils.define_prim(f"/World/Cube", "Cube")
            >>> prim_utils.get_prim_path(prim)
            '/World/Cube'
        
    """
def get_prim_variant_collection(prim: str | Usd.Prim) -> dict[str, list[str]]:
    """
    Get variant collection (all variant sets and selections) for a USD prim.
    
        Backends: :guilabel:`usd`.
    
        Args:
            prim: Prim path or prim instance.
    
        Returns:
            Variant collection (variant sets and selections).
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.experimental.utils.prim as prim_utils
            >>> import isaacsim.core.experimental.utils.stage as stage_utils
            >>> from isaacsim.storage.native import get_assets_root_path
            >>>
            >>> stage_utils.open_stage(
            ...     get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
            ... )  # doctest: +NO_CHECK
            >>>
            >>> prim_utils.get_prim_variant_collection("/panda")
            {'Mesh': ['Performance', 'Quality'], 'Gripper': ['AlternateFinger', 'Default']}
        
    """
def get_prim_variants(prim: str | Usd.Prim) -> list[tuple[str, str]]:
    """
    Get variants (variant sets and selections) authored on a USD prim.
    
        Backends: :guilabel:`usd`.
    
        Args:
            prim: Prim path or prim instance.
    
        Returns:
            Authored variants (variant sets and selections).
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.experimental.utils.prim as prim_utils
            >>> import isaacsim.core.experimental.utils.stage as stage_utils
            >>> from isaacsim.storage.native import get_assets_root_path
            >>>
            >>> stage_utils.open_stage(
            ...     get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
            ... )  # doctest: +NO_CHECK
            >>>
            >>> prim_utils.get_prim_variants("/panda")
            [('Gripper', 'Default'), ('Mesh', 'Performance')]
        
    """
def has_api(prim: str | Usd.Prim, api: str | type | list[str | type], *, test: typing.Literal['all', 'any', 'none'] = 'all') -> bool:
    """
    Check if a prim has or not the given API schema(s) applied.
    
        Backends: :guilabel:`usd`.
    
        Args:
            prim: Prim path or prim instance.
            api: API schema name or type, or a list of them.
            test: Checking operation to test for.
                - "all": All APIs must be present.
                - "any": Any API must be present.
                - "none": No APIs must be present.
    
        Returns:
            Whether the prim has or not (depending on the test) the given API schema applied.
    
        Raises:
            ValueError: If the test operation is invalid.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.experimental.utils.prim as prim_utils
            >>> import isaacsim.core.experimental.utils.stage as stage_utils
            >>> from pxr import UsdLux
            >>>
            >>> prim = stage_utils.define_prim("/World/Light", "SphereLight")
            >>> prim_utils.has_api(prim, UsdLux.LightAPI)
            True
        
    """
def set_prim_variants(prim: str | Usd.Prim, *, variants: list[tuple[str, str]]) -> None:
    """
    Set/author variants (variant sets and selections) on a USD prim.
    
        Backends: :guilabel:`usd`.
    
        Args:
            prim: Prim path or prim instance.
            variants: Variants (variant sets and selections) to author on the USD prim.
    
        Raises:
            ValueError: If a variant set or selection is invalid.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.experimental.utils.prim as prim_utils
            >>> import isaacsim.core.experimental.utils.stage as stage_utils
            >>> from isaacsim.storage.native import get_assets_root_path
            >>>
            >>> stage_utils.open_stage(
            ...     get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
            ... )  # doctest: +NO_CHECK
            >>>
            >>> prim_utils.set_prim_variants("/panda", variants=[("Mesh", "Quality"), ("Gripper", "AlternateFinger")])
        
    """
