from __future__ import annotations
import _thread
import carb as carb
import contextlib as contextlib
from isaacsim.core.experimental.utils.impl import backend as backend_utils
from isaacsim.core.experimental.utils.impl import prim as prim_utils
import omni as omni
from omni.metrics.assembler.core import get_metrics_assembler_interface
from pxr import Sdf
from pxr import Usd
from pxr import UsdUtils
import threading as threading
import typing
import usdrt as usdrt
__all__: list[str] = ['Sdf', 'Usd', 'UsdUtils', 'add_reference_to_stage', 'backend_utils', 'carb', 'contextlib', 'create_new_stage', 'create_new_stage_async', 'define_prim', 'get_current_stage', 'get_metrics_assembler_interface', 'get_stage_id', 'is_stage_set', 'omni', 'open_stage', 'open_stage_async', 'prim_utils', 'threading', 'usdrt', 'use_stage']
def add_reference_to_stage(usd_path: str, path: str, *, prim_type: str = 'Xform', variants: list[tuple[str, str]] = list()) -> Usd.Prim:
    """
    Add a USD file reference to the stage at the specified prim path.
    
        Backends: :guilabel:`usd`.
    
        .. note::
    
            This function handles stage units verification to ensure compatibility.
    
        Args:
            usd_path: USD file path to reference.
            path: Prim path where the reference will be attached.
            prim_type: Prim type to create if the given ``path`` doesn't exist.
            variants: Variants (variant sets and selections) to author on the USD prim.
    
        Returns:
            USD prim.
    
        Raises:
            Exception: The USD file might not exist or might not be a valid USD file.
            ValueError: If a variant set or selection is invalid.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.experimental.utils.stage as stage_utils
            >>> from isaacsim.storage.native import get_assets_root_path
            >>>
            >>> prim = stage_utils.add_reference_to_stage(
            ...     usd_path=get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd",
            ...     path="/panda",
            ...     variants=[("Gripper", "AlternateFinger"), ("Mesh", "Performance")],
            ... )
        
    """
def create_new_stage(*, template: str | None = None) -> Usd.Stage:
    """
    Create a new USD stage attached to the USD context.
    
        Backends: :guilabel:`usd`.
    
        .. note::
    
            At least the following templates should be available.
            Other templates might be available depending on app customizations.
    
            .. list-table::
                :header-rows: 1
    
                * - Template
                  - Description
                * - ``"default stage"``
                  - Stage with a gray gridded plane, dome and distant lights, and the ``/World`` Xform prim.
                * - ``"empty"``
                  - Empty stage with the ``/World`` Xform prim.
                * - ``"sunlight"``
                  - Stage with a distant light and the ``/World`` Xform prim.
    
        Args:
            template: The template to use to create the stage. If ``None``, a new stage is created with nothing.
    
        Returns:
            New USD stage instance.
    
        Raises:
            ValueError: When the template is not found.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.experimental.utils.stage as stage_utils
            >>>
            >>> # create a new stage from the 'sunlight' template
            >>> stage_utils.create_new_stage(template="sunlight")
            Usd.Stage.Open(rootLayer=Sdf.Find('anon:...usd'), ...)
        
    """
def create_new_stage_async(*, template: str | None = None) -> Usd.Stage:
    """
    Create a new USD stage attached to the USD context.
    
        Backends: :guilabel:`usd`.
    
        This function is the asynchronous version of :py:func:`create_new_stage`.
    
        Args:
            template: The template to use to create the stage. If ``None``, a new stage is created with nothing.
    
        Returns:
            New USD stage instance.
    
        Raises:
            ValueError: When the template is not found.
        
    """
def define_prim(path: str, type_name: str = 'Xform') -> Usd.Prim | usdrt.Usd.Prim:
    """
    Attempt to define a prim of the specified type at the given path.
    
        Backends: :guilabel:`usd`, :guilabel:`usdrt`, :guilabel:`fabric`.
    
        Common token values for ``type_name`` are:
    
        * ``"Camera"``, ``"Mesh"``, ``"PhysicsScene"``, ``"Xform"``
        * Shapes (``"Capsule"``, ``"Cone"``, ``"Cube"``, ``"Cylinder"``, ``"Plane"``, ``"Sphere"``)
        * Lights (``"CylinderLight"``, ``"DiskLight"``, ``"DistantLight"``, ``"DomeLight"``, ``"RectLight"``, ``"SphereLight"``)
    
        Args:
            path: Absolute prim path.
            type_name: Token identifying the prim type.
    
        Raises:
            ValueError: If the path is not a valid or absolute path string.
            RuntimeError: If there is already a prim at the given path with a different type.
    
        Returns:
            Defined prim.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.experimental.utils.stage as stage_utils
            >>>
            >>> stage_utils.define_prim("/World/Sphere", type_name="Sphere")
            Usd.Prim(</World/Sphere>)
        
    """
def get_current_stage(*, backend: str | None = None) -> Usd.Stage | usdrt.Usd.Stage:
    """
    Get the stage set in the context manager or the default stage attached to the USD context.
    
        Backends: :guilabel:`usd`, :guilabel:`usdrt`, :guilabel:`fabric`.
    
        Args:
            backend: Backend to use to get the stage. If not ``None``, it has precedence over the current backend
                set via the :py:func:`~isaacsim.core.experimental.utils.impl.backend.use_backend` context manager.
    
        Returns:
            The current stage instance or the default stage attached to the USD context if no stage is set.
    
        Raises:
            ValueError: If the backend is not supported.
            ValueError: If there is no stage (set via context manager or attached to the USD context).
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.experimental.utils.stage as stage_utils
            >>>
            >>> stage_utils.get_current_stage()
            Usd.Stage.Open(rootLayer=Sdf.Find('anon:...usd'), ...)
        
    """
def get_stage_id(stage: Usd.Stage) -> int:
    """
    Get the stage ID of a USD stage.
    
        Backends: :guilabel:`usd`.
    
        Args:
            stage: The stage to get the ID of.
    
        Returns:
            The stage ID.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.experimental.utils.stage as stage_utils
            >>>
            >>> stage = stage_utils.get_current_stage()
            >>> stage_utils.get_stage_id(stage)  # doctest: +NO_CHECK
            9223006
        
    """
def is_stage_set() -> bool:
    """
    Check if a stage is set in the context manager.
    
        Returns:
            Whether a stage is set in the context manager.
        
    """
def open_stage(usd_path: str) -> tuple[bool, Usd.Stage | None]:
    """
    Open a USD file attached to the USD context.
    
        Backends: :guilabel:`usd`.
    
        Args:
            usd_path: USD file path to open.
    
        Returns:
            Two-elements tuple. 1) Whether the USD file was opened successfully.
            2) Opened USD stage instance or None if the USD file was not opened.
    
        Raises:
            ValueError: If the USD file does not exist or is not a valid (shallow check).
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.experimental.utils.stage as stage_utils
            >>> from isaacsim.storage.native import get_assets_root_path
            >>>
            >>> # open a USD file
            >>> result, stage = stage_utils.open_stage(
            ...     get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
            ... )
            >>> result
            True
            >>> stage
            Usd.Stage.Open(rootLayer=Sdf.Find('...'), ...)
        
    """
def open_stage_async(usd_path: str) -> tuple[bool, Usd.Stage | None]:
    """
    Open a USD file attached to the USD context.
    
        Backends: :guilabel:`usd`.
    
        This function is the asynchronous version of :py:func:`open_stage`.
    
        Args:
            usd_path: USD file path to open.
    
        Returns:
            Two-elements tuple. 1) Whether the USD file was opened successfully.
            2) Opened USD stage instance or None if the USD file was not opened.
    
        Raises:
            ValueError: If the USD file does not exist or is not a valid (shallow check).
        
    """
def use_stage(*args, **kwds) -> Generator[None, None, None]:
    """
    Context manager that sets a thread-local stage instance.
    
        Args:
            stage: The stage to set in the context.
    
        Raises:
            AssertionError: If the stage is not a USD stage instance.
    
        Example:
    
        .. code-block:: python
    
            >>> from pxr import Usd
            >>> import isaacsim.core.experimental.utils.stage as stage_utils
            >>>
            >>> stage_in_memory = Usd.Stage.CreateInMemory()
            >>> with stage_utils.use_stage(stage_in_memory):
            ...    # operate on the specified stage
            ...    pass
            >>> # operate on the default stage attached to the USD context
        
    """
_context: _thread._local  # value = <_thread._local object>
