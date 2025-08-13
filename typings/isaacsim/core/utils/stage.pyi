from __future__ import annotations
import _thread
import builtins as builtins
import carb as carb
import contextlib as contextlib
import omni as omni
from omni.kit.usd import layers
from omni.metrics.assembler.core import get_metrics_assembler_interface
from omni.usd.commands.usd_commands import DeletePrimsCommand
from pxr import Sdf
from pxr import Usd
import pxr.Usd
from pxr import UsdGeom
from pxr import UsdUtils
import threading as threading
import typing as typing
import usdrt as usdrt
__all__: list[str] = ['AXES_TOKEN', 'DeletePrimsCommand', 'Sdf', 'Usd', 'UsdGeom', 'UsdUtils', 'add_reference_to_stage', 'builtins', 'carb', 'clear_stage', 'close_stage', 'contextlib', 'create_new_stage', 'create_new_stage_async', 'create_new_stage_in_memory', 'get_current_stage', 'get_current_stage_id', 'get_metrics_assembler_interface', 'get_next_free_path', 'get_stage_units', 'get_stage_up_axis', 'is_stage_loading', 'layers', 'omni', 'open_stage', 'open_stage_async', 'print_stage_prim_paths', 'remove_deleted_references', 'save_stage', 'set_livesync_stage', 'set_stage_units', 'set_stage_up_axis', 'threading', 'traverse_stage', 'typing', 'update_stage', 'update_stage_async', 'usdrt', 'use_stage']
def add_reference_to_stage(usd_path: str, prim_path: str, prim_type: str = 'Xform') -> pxr.Usd.Prim:
    """
    Add USD reference to the opened stage at specified prim path.
    
        Adds a reference to an external USD file at the specified prim path on the current stage.
        If the prim does not exist, it will be created with the specified type.
        This function also handles stage units verification to ensure compatibility.
    
        Args:
            usd_path: The path to USD file to reference.
            prim_path: The prim path where the reference will be attached.
            prim_type: The type of prim to create if it doesn't exist. Defaults to "Xform".
    
        Returns:
            The USD prim at the specified prim path.
    
        Raises:
            FileNotFoundError: When the input USD file is not found at the specified path.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>>
            >>> # load an USD file (franka.usd) to the stage under the path /World/panda
            >>> prim = stage_utils.add_reference_to_stage(
            ...     usd_path="/home/<user>/Documents/Assets/Robots/FrankaRobotics/FrankaPanda/franka.usd",
            ...     prim_path="/World/panda"
            ... )
            >>> prim
            Usd.Prim(</World/panda>)
        
    """
def clear_stage(predicate: typing.Optional[typing.Callable[[str], bool]] = None) -> None:
    """
    Deletes all prims in the stage without populating the undo command buffer
    
        Args:
            predicate (typing.Optional[typing.Callable[[str], bool]], optional):
                user defined function that takes a prim_path (str) as input and returns True/False if the prim
                should/shouldn't be deleted. If predicate is None, a default is used that deletes all prims
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>>
            >>> # clear the whole stage
            >>> stage_utils.clear_stage()
            >>>
            >>> # given the stage: /World/Cube, /World/Cube_01, /World/Cube_02.
            >>> # Delete only the prims of type Cube
            >>> predicate = lambda path: prims_utils.get_prim_type_name(path) == "Cube"
            >>> stage_utils.clear_stage(predicate)  # after the execution the stage will be /World
        
    """
def close_stage(callback_fn: typing.Callable = None) -> bool:
    """
    Closes the current opened USD stage.
    
        .. note::
    
            Once the stage is closed, it is necessary to open a new stage or create a new one in order to work on it.
    
        Args:
            callback_fn (typing.Callable, optional): Callback function to call while closing. Defaults to None.
    
        Returns:
            bool: True if operation is successful, otherwise false.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>>
            >>> stage_utils.close_stage()
            True
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>>
            >>> def callback(*args, **kwargs):
            ...     print("callback:", args, kwargs)
            ...
            >>> stage_utils.close_stage(callback)
            True
            >>> stage_utils.close_stage(callback)
            callback: (False, 'Stage opening or closing already in progress!!') {}
            False
        
    """
def create_new_stage() -> pxr.Usd.Stage:
    """
    Create a new stage attached to the USD context.
    
        Returns:
            Usd.Stage: The created USD stage.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>>
            >>> stage_utils.create_new_stage()
            Usd.Stage.Open(rootLayer=Sdf.Find('anon:0x7fba6c04f840:World7.usd'),
                            sessionLayer=Sdf.Find('anon:0x7fba6c01c5c0:World7-session.usda'),
                            pathResolverContext=<invalid repr>)
        
    """
def create_new_stage_async() -> None:
    """
    Create a new stage (asynchronous version).
    
        Example:
    
        .. code-block:: python
    
            >>> import asyncio
            >>> import isaacsim.core.utils.stage as stage_utils
            >>> from omni.kit.async_engine import run_coroutine
            >>>
            >>> async def task():
            ...     await stage_utils.create_new_stage_async()
            ...
            >>> run_coroutine(task())
        
    """
def create_new_stage_in_memory() -> pxr.Usd.Stage:
    """
    Create a new stage in memory.
    
        Returns:
            Usd.Stage: The created USD stage.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>>
            >>> stage_utils.create_new_stage_in_memory()
            Usd.Stage.Open(rootLayer=Sdf.Find('anon:0xf7b00e0:tmp.usda'),
                            sessionLayer=Sdf.Find('anon:0xf7cd2e0:tmp-session.usda'),
                            pathResolverContext=<invalid repr>)
        
    """
def get_current_stage(fabric: bool = False) -> typing.Union[pxr.Usd.Stage, usdrt.Usd._Usd.Stage]:
    """
    Get the current open USD or Fabric stage
    
        Args:
            fabric (bool, optional): True to get the fabric stage. False to get the USD stage. Defaults to False.
    
        Returns:
            typing.Union[Usd.Stage, usdrt.Usd._Usd.Stage]: The USD or Fabric stage as specified by the input arg fabric.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>>
            >>> stage_utils.get_current_stage()
            Usd.Stage.Open(rootLayer=Sdf.Find('anon:0x7fba6c04f840:World7.usd'),
                            sessionLayer=Sdf.Find('anon:0x7fba6c01c5c0:World7-session.usda'),
                            pathResolverContext=<invalid repr>)
        
    """
def get_current_stage_id() -> int:
    """
    Get the current open stage id
    
        Returns:
            int: The stage id.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>>
            >>> stage_utils.get_current_stage_id()
            1234567890
        
    """
def get_next_free_path(path: str, parent: str = None) -> str:
    """
    Returns the next free usd path for the current stage
    
        Args:
            path (str): path we want to check
            parent (str, optional): Parent prim for the given path. Defaults to None.
    
        Returns:
            str: a new path that is guaranteed to not exist on the current stage
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>>
            >>> # given the stage: /World/Cube, /World/Cube_01.
            >>> # Get the next available path for /World/Cube
            >>> stage_utils.get_next_free_path("/World/Cube")
            /World/Cube_02
        
    """
def get_stage_units() -> float:
    """
    Get the stage meters per unit currently set
    
        The most common units and their values are listed in the following table:
    
        +------------------+--------+
        | Unit             | Value  |
        +==================+========+
        | kilometer (km)   | 1000.0 |
        +------------------+--------+
        | meters (m)       | 1.0    |
        +------------------+--------+
        | inch (in)        | 0.0254 |
        +------------------+--------+
        | centimeters (cm) | 0.01   |
        +------------------+--------+
        | millimeter (mm)  | 0.001  |
        +------------------+--------+
    
        Returns:
            float: current stage meters per unit
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>>
            >>> stage_utils.get_stage_units()
            1.0
        
    """
def get_stage_up_axis() -> str:
    """
    Get the current up-axis of USD stage.
    
        Returns:
            str: The up-axis of the stage.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>>
            >>> stage_utils.get_stage_up_axis()
            Z
        
    """
def is_stage_loading() -> bool:
    """
    Convenience function to see if any files are being loaded.
    
        Returns:
            bool: True if loading, False otherwise
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>>
            >>> stage_utils.is_stage_loading()
            False
        
    """
def open_stage(usd_path: str) -> bool:
    """
    Open the given usd file and replace currently opened stage.
    
        Args:
            usd_path (str): Path to the USD file to open.
    
        Raises:
            ValueError: When input path is not a supported file type by USD.
    
        Returns:
            bool: True if operation is successful, otherwise false.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>>
            >>> stage_utils.open_stage("/home/<user>/Documents/Assets/Robots/FrankaRobotics/FrankaPanda/franka.usd")
            True
        
    """
def open_stage_async(usd_path: str) -> typing.Tuple[bool, int]:
    """
    Open the given usd file and replace currently opened stage (asynchronous version).
    
        Args:
            usd_path (str): Path to the USD file to open.
    
        Raises:
            ValueError: When input path is not a supported file type by USD.
    
        Returns:
            bool: True if operation is successful, otherwise false.
    
        Example:
    
        .. code-block:: python
    
            >>> import asyncio
            >>> import isaacsim.core.utils.stage as stage_utils
            >>> from omni.kit.async_engine import run_coroutine
            >>>
            >>> async def task():
            ...     await stage_utils.open_stage_async("/home/<user>/Documents/Assets/Robots/FrankaRobotics/FrankaPanda/franka.usd")
            ...
            >>> run_coroutine(task())
        
    """
def print_stage_prim_paths(fabric: bool = False) -> None:
    """
    Traverses the stage and prints all prim (hidden or not) paths.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>>
            >>> # given the stage: /World/Cube, /World/Cube_01, /World/Cube_02.
            >>> stage_utils.print_stage_prim_paths()
            /Render
            /World
            /World/Cube
            /World/Cube_01
            /World/Cube_02
            /OmniverseKit_Persp
            /OmniverseKit_Front
            /OmniverseKit_Top
            /OmniverseKit_Right
        
    """
def remove_deleted_references():
    """
    Clean up deleted references in the current USD stage.
    
        Removes any deleted items from both payload and references lists
        for all prims in the stage's root layer. Prints information about
        any deleted items that were cleaned up.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>> stage_utils.remove_deleted_references()
            Removed 2 deleted payload items from </World/Robot>
            Removed 1 deleted reference items from </World/Scene>
        
    """
def save_stage(usd_path: str, save_and_reload_in_place = True) -> bool:
    """
    Save usd file to path, it will be overwritten with the current stage
    
        Args:
            usd_path (str): File path to save the current stage to
            save_and_reload_in_place (bool, optional): use ``save_as_stage`` to save and reload the root layer in place. Defaults to True.
    
        Raises:
            ValueError: When input path is not a supported file type by USD.
    
        Returns:
            bool: True if operation is successful, otherwise false.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>>
            >>> stage_utils.save_stage("/home/<user>/Documents/Save/stage.usd")
            True
        
    """
def set_livesync_stage(usd_path: str, enable: bool) -> bool:
    """
    Save the stage and set the Live Sync mode for real-time live editing of shared files on a Nucleus server
    
        Args:
            usd_path (str): path to enable live sync for, it will be overwritten with the current stage
            enable (bool): True to enable livesync, false to disable livesync
    
        Returns:
            bool: True if operation is successful, otherwise false.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>>
            >>> stage_utils.set_livesync_stage("omniverse://localhost/Users/Live/stage.usd", enable=True)
            server omniverse://localhost: ConnectionStatus.CONNECTING
            server omniverse://localhost: ConnectionStatus.CONNECTED
            True
        
    """
def set_stage_units(stage_units_in_meters: float) -> None:
    """
    Set the stage meters per unit
    
        The most common units and their values are listed in the following table:
    
        +------------------+--------+
        | Unit             | Value  |
        +==================+========+
        | kilometer (km)   | 1000.0 |
        +------------------+--------+
        | meters (m)       | 1.0    |
        +------------------+--------+
        | inch (in)        | 0.0254 |
        +------------------+--------+
        | centimeters (cm) | 0.01   |
        +------------------+--------+
        | millimeter (mm)  | 0.001  |
        +------------------+--------+
    
        Args:
            stage_units_in_meters (float): units for stage
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>>
            >>> stage_utils.set_stage_units(1.0)
        
    """
def set_stage_up_axis(axis: str = 'z') -> None:
    """
    Change the up axis of the current stage
    
        Args:
            axis (UsdGeom.Tokens, optional): valid values are ``"x"``, ``"y"`` and ``"z"``
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>>
            >>> # set stage up axis to Y-up
            >>> stage_utils.set_stage_up_axis("y")
        
    """
def traverse_stage(fabric = False) -> typing.Iterable:
    """
    Traverse through prims (hidden or not) in the opened Usd stage.
    
        Returns:
            typing.Iterable: Generator which yields prims from the stage in depth-first-traversal order.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>>
            >>> # given the stage: /World/Cube, /World/Cube_01, /World/Cube_02.
            >>> # Traverse through prims in the stage
            >>> for prim in stage_utils.traverse_stage():
            >>>     print(prim)
            Usd.Prim(</World>)
            Usd.Prim(</World/Cube>)
            Usd.Prim(</World/Cube_01>)
            Usd.Prim(</World/Cube_02>)
            Usd.Prim(</OmniverseKit_Persp>)
            Usd.Prim(</OmniverseKit_Front>)
            Usd.Prim(</OmniverseKit_Top>)
            Usd.Prim(</OmniverseKit_Right>)
            Usd.Prim(</Render>)
        
    """
def update_stage() -> None:
    """
    Update the current USD stage.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>>
            >>> stage_utils.update_stage()
        
    """
def update_stage_async() -> None:
    """
    Update the current USD stage (asynchronous version).
    
        Example:
    
        .. code-block:: python
    
            >>> import asyncio
            >>> import isaacsim.core.utils.stage as stage_utils
            >>> from omni.kit.async_engine import run_coroutine
            >>>
            >>> async def task():
            ...     await stage_utils.update_stage_async()
            ...
            >>> run_coroutine(task())
        
    """
def use_stage(*args, **kwds) -> None:
    """
    Context manager that sets a thread-local stage.
    
        Args:
            stage: The stage to set in the context.
    
        Raises:
            AssertionError: If the stage is not a USD stage instance.
    
        Example:
    
        .. code-block:: python
    
            >>> from pxr import Usd
            >>> import isaacsim.core.utils.stage as stage_utils
            >>>
            >>> stage_in_memory = Usd.Stage.CreateInMemory()
            >>> with stage_utils.use_stage(stage_in_memory):
            ...    # operate on the specified stage
            ...    pass
            >>> # operate on the default stage attached to the USD context
        
    """
AXES_TOKEN: dict = {'X': 'X', 'x': 'X', 'Y': 'Y', 'y': 'Y', 'Z': 'Z', 'z': 'Z'}
_context: _thread._local  # value = <_thread._local object>
