from __future__ import annotations
from isaacsim.core.utils._isaac_utils import _find_matching_prim_paths
from isaacsim.core.utils.semantics import add_update_semantics
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.core.utils.stage import get_current_stage
from isaacsim.core.utils.string import find_root_prim_path_from_regex
import numpy as np
import omni as omni
from omni.usd.commands.usd_commands import DeletePrimsCommand
from omni.usd.commands.usd_commands import MovePrimCommand
from pxr import Gf
from pxr import Sdf
from pxr import Usd
import pxr.Usd
from pxr import UsdGeom
from pxr import UsdPhysics
import re as re
import typing as typing
import usdrt as usdrt
__all__ = ['DeletePrimsCommand', 'Gf', 'MovePrimCommand', 'SDF_type_to_Gf', 'Sdf', 'Usd', 'UsdGeom', 'UsdPhysics', 'add_reference_to_stage', 'add_update_semantics', 'create_prim', 'define_prim', 'delete_prim', 'find_matching_prim_paths', 'find_root_prim_path_from_regex', 'get_all_matching_child_prims', 'get_articulation_root_api_prim_path', 'get_current_stage', 'get_first_matching_child_prim', 'get_first_matching_parent_prim', 'get_prim_at_path', 'get_prim_attribute_names', 'get_prim_attribute_value', 'get_prim_children', 'get_prim_object_type', 'get_prim_parent', 'get_prim_path', 'get_prim_property', 'get_prim_type_name', 'is_prim_ancestral', 'is_prim_hidden_in_stage', 'is_prim_no_delete', 'is_prim_non_root_articulation_link', 'is_prim_path_valid', 'is_prim_root_path', 'move_prim', 'np', 'omni', 'query_parent_path', 're', 'set_prim_attribute_value', 'set_prim_hide_in_stage_window', 'set_prim_no_delete', 'set_prim_property', 'set_prim_visibility', 'set_targets', 'typing', 'usdrt']
def create_prim(prim_path: str, prim_type: str = 'Xform', position: typing.Optional[typing.Sequence[float]] = None, translation: typing.Optional[typing.Sequence[float]] = None, orientation: typing.Optional[typing.Sequence[float]] = None, scale: typing.Optional[typing.Sequence[float]] = None, usd_path: typing.Optional[str] = None, semantic_label: typing.Optional[str] = None, semantic_type: str = 'class', attributes: typing.Optional[dict] = None) -> pxr.Usd.Prim:
    """
    Create a prim into current USD stage.
    
        The method applies specified transforms, the semantic label and set specified attributes.
    
        Args:
            prim_path (str): The path of the new prim.
            prim_type (str): Prim type name
            position (typing.Sequence[float], optional): prim position (applied last)
            translation (typing.Sequence[float], optional): prim translation (applied last)
            orientation (typing.Sequence[float], optional): prim rotation as quaternion
            scale (np.ndarray (3), optional): scaling factor in x, y, z.
            usd_path (str, optional): Path to the USD that this prim will reference.
            semantic_label (str, optional): Semantic label.
            semantic_type (str, optional): set to "class" unless otherwise specified.
            attributes (dict, optional): Key-value pairs of prim attributes to set.
    
        Raises:
            Exception: If there is already a prim at the prim_path
    
        Returns:
            Usd.Prim: The created USD prim.
    
        Example:
    
        .. code-block:: python
    
            >>> import numpy as np
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> # create a cube (/World/Cube) of size 2 centered at (1.0, 0.5, 0.0)
            >>> prims_utils.create_prim(
            ...     prim_path="/World/Cube",
            ...     prim_type="Cube",
            ...     position=np.array([1.0, 0.5, 0.0]),
            ...     attributes={"size": 2.0}
            ... )
            Usd.Prim(</World/Cube>)
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> # load an USD file (franka.usd) to the stage under the path /World/panda
            >>> prims_utils.create_prim(
            ...     prim_path="/World/panda",
            ...     prim_type="Xform",
            ...     usd_path="/home/<user>/Documents/Assets/Robots/Franka/franka.usd"
            ... )
            Usd.Prim(</World/panda>)
        
    """
def define_prim(prim_path: str, prim_type: str = 'Xform', fabric: bool = False) -> pxr.Usd.Prim:
    """
    Create a USD Prim at the given prim_path of type prim_type unless one already exists
    
        .. note::
    
            This method will create a prim of the specified type in the specified path.
            To apply a transformation (position, orientation, scale), set attributes or
            load an USD file while creating the prim use the ``create_prim`` function.
    
        Args:
            prim_path (str): path of the prim in the stage
            prim_type (str, optional): The type of the prim to create. Defaults to "Xform".
            fabric (bool, optional): True for fabric stage and False for USD stage. Defaults to False.
    
        Raises:
            Exception: If there is already a prim at the prim_path
    
        Returns:
            Usd.Prim: The created USD prim.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> prims_utils.define_prim("/World/Shapes", prim_type="Xform")
            Usd.Prim(</World/Shapes>)
        
    """
def delete_prim(prim_path: str) -> None:
    """
    Remove the USD Prim and its descendants from the scene if able
    
        Args:
            prim_path (str): path of the prim in the stage
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> prims_utils.delete_prim("/World/Cube")
        
    """
def find_matching_prim_paths(prim_path_regex: str, prim_type: typing.Optional[str] = None) -> typing.List[str]:
    """
    Find all the matching prim paths in the stage based on Regex expression.
    
        Args:
            prim_path_regex (str): The Regex expression for prim path.
            prim_type (typing.Optional[str]): The type of the prims to filter, only supports articulation and rigid_body currently. Defaults to None.
    
        Returns:
            typing.List[str]: List of prim paths that match input expression.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> # given the stage: /World/env/Cube, /World/env_01/Cube, /World/env_02/Cube
            >>> # get only the prim Cube paths from env_01 and env_02
            >>> prims_utils.find_matching_prim_paths("/World/env_.*/Cube")
            ['/World/env_01/Cube', '/World/env_02/Cube']
        
    """
def get_all_matching_child_prims(prim_path: str, predicate: typing.Callable[[str], bool] = ..., depth: typing.Optional[int] = None) -> typing.List[pxr.Usd.Prim]:
    """
    Performs a breadth-first search starting from the root and returns all the prims matching the predicate.
    
        Args:
            prim_path (str): root prim path to start traversal from.
            predicate (typing.Callable[[str], bool]): predicate that checks the prim path of a prim and returns a boolean.
            depth (typing.Optional[int]): maximum depth for traversal, should be bigger than zero if specified.
                                          Defaults to None (i.e: traversal till the end of the tree).
    
        Returns:
            typing.List[Usd.Prim]: A list containing the root and children prims matching specified predicate.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> # get all hidden prims
            >>> predicate = lambda path: prims_utils.is_prim_hidden_in_stage(path)  # True if the prim at path is hidden
            >>> prims_utils.get_all_matching_child_prims("/", predicate)
            [Usd.Prim(</OmniverseKit_Persp>),
             Usd.Prim(</OmniverseKit_Front>),
             Usd.Prim(</OmniverseKit_Top>),
             Usd.Prim(</OmniverseKit_Right>),
             Usd.Prim(</Render>)]
        
    """
def get_articulation_root_api_prim_path(prim_path):
    """
    Get the prim path that has the Articulation Root API
    
        .. note::
    
            This function assumes that all prims defined by a regular expression correspond to the same articulation type
    
        Args:
            prim_path (str): path or regex of the prim(s) on which to search for the prim containing the API
    
        Returns:
            str: path or regex of the prim(s) that has the Articulation Root API.
                 If no prim has been found, the same input value is returned
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> # given the stage: /World/env/Ant, /World/env_01/Ant, /World/env_02/Ant
            >>> # search specifying the prim with the Articulation Root API
            >>> prims_utils.get_articulation_root_api_prim_path("/World/env/Ant/torso")
            /World/env/Ant/torso
            >>> # search specifying some ancestor prim that does not have the Articulation Root API
            >>> prims_utils.get_articulation_root_api_prim_path("/World/env/Ant")
            /World/env/Ant/torso
            >>> # regular expression search
            >>> prims_utils.get_articulation_root_api_prim_path("/World/env.*/Ant")
            /World/env.*/Ant/torso
        
    """
def get_first_matching_child_prim(prim_path: str, predicate: typing.Callable[[str], bool], fabric: bool = False) -> pxr.Usd.Prim:
    """
    Recursively get the first USD Prim at the path string that passes the predicate function
    
        Args:
            prim_path (str): path of the prim in the stage
            predicate (typing.Callable[[str], bool]): Function to test the prims against
            fabric (bool, optional): True for fabric stage and False for USD stage. Defaults to False.
    
        Returns:
             Usd.Prim: The first prim or child of the prim, as defined by GetChildren, that passes the predicate
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> # given the stage: /World/Cube, /World/Cube_01, /World/Cube_02.
            >>> # Get the first child prim of type Cube
            >>> predicate = lambda path: prims_utils.get_prim_type_name(path) == "Cube"
            >>> prims_utils.get_first_matching_child_prim("/", predicate)
            Usd.Prim(</World/Cube>)
        
    """
def get_first_matching_parent_prim(prim_path: str, predicate: typing.Callable[[str], bool]) -> pxr.Usd.Prim:
    """
    Recursively get the first USD Prim at the parent path string that passes the predicate function
    
        Args:
            prim_path (str): path of the prim in the stage
            predicate (typing.Callable[[str], bool]): Function to test the prims against
    
        Returns:
            str: The first prim on the parent path, as defined by GetParent, that passes the predicate
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> # given the stage: /World/Cube. Get the first parent of Cube prim of type Xform
            >>> predicate = lambda path: prims_utils.get_prim_type_name(path) == "Xform"
            >>> prims_utils.get_first_matching_parent_prim("/World/Cube", predicate)
            Usd.Prim(</World>)
        
    """
def get_prim_at_path(prim_path: str, fabric: bool = False) -> typing.Union[pxr.Usd.Prim, usdrt.Usd._Usd.Prim]:
    """
    Get the USD or Fabric Prim at a given path string
    
        Args:
            prim_path (str): path of the prim in the stage.
            fabric (bool, optional): True for fabric stage and False for USD stage. Defaults to False.
    
        Returns:
            typing.Union[Usd.Prim, usdrt.Usd._Usd.Prim]: USD or Fabric Prim object at the given path in the current stage.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> prims_utils.get_prim_at_path("/World/Cube")
            Usd.Prim(</World/Cube>)
        
    """
def get_prim_attribute_names(prim_path: str, fabric: bool = False) -> typing.List[str]:
    """
    Get all the attribute names of a prim at the path
    
        Args:
            prim_path (str): path of the prim in the stage
            fabric (bool, optional): True for fabric stage and False for USD stage. Defaults to False.
    
        Raises:
            Exception: If there is not a valid prim at the given path
    
        Returns:
            typing.List[str]: List of the prim attribute names
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> prims_utils.get_prim_attribute_names("/World/Cube")
            ['doubleSided', 'extent', 'orientation', 'primvars:displayColor', 'primvars:displayOpacity',
             'purpose', 'size', 'visibility', 'xformOp:orient', 'xformOp:scale', 'xformOp:translate', 'xformOpOrder']
        
    """
def get_prim_attribute_value(prim_path: str, attribute_name: str, fabric: bool = False) -> typing.Any:
    """
    Get a prim attribute value
    
        Args:
            prim_path (str): path of the prim in the stage
            attribute_name (str): name of the attribute to get
            fabric (bool, optional): True for fabric stage and False for USD stage. Defaults to False.
    
        Raises:
            Exception: If there is not a valid prim at the given path
    
        Returns:
            typing.Any: Prim attribute value
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> prims_utils.get_prim_attribute_value("/World/Cube", attribute_name="size")
            1.0
        
    """
def get_prim_children(prim: pxr.Usd.Prim) -> typing.List[pxr.Usd.Prim]:
    """
    Return the call of the USD Prim's GetChildren member function
    
        Args:
            prim (Usd.Prim): The parent USD Prim
    
        Returns:
            typing.List[Usd.Prim]: A list of the prim's children.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> # given the stage: /World/Cube, /World/Cube_01, /World/Cube_02.
            >>> # Get all prims under the prim World
            >>> prim = prims_utils.get_prim_at_path("/World")
            >>> prims_utils.get_prim_children(prim)
            [Usd.Prim(</World/Cube>), Usd.Prim(</World/Cube_01>), Usd.Prim(</World/Cube_02>)]
        
    """
def get_prim_object_type(prim_path: str) -> typing.Optional[str]:
    """
    Get the dynamic control object type of the USD Prim at the given path.
    
        If the prim at the path is of Dynamic Control type e.g.: rigid_body, joint, dof, articulation, attractor, d6joint,
        then the corresponding string returned. If is an Xformable prim, then "xform" is returned. Otherwise None
        is returned.
    
        Args:
            prim_path (str): path of the prim in the stage
    
        Raises:
            Exception: If the USD Prim is not a supported type.
    
        Returns:
            str: String corresponding to the object type.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> prims_utils.get_prim_object_type("/World/Cube")
            xform
        
    """
def get_prim_parent(prim: pxr.Usd.Prim) -> pxr.Usd.Prim:
    """
    Return the call of the USD Prim's GetChildren member function
    
        Args:
            prim (Usd.Prim): The USD Prim to call GetParent on
    
        Returns:
            Usd.Prim: The prim's parent returned from GetParent
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> # given the stage: /World/Cube. Get the prim Cube's parent
            >>> prim = prims_utils.get_prim_at_path("/World/Cube")
            >>> prims_utils.get_prim_parent(prim)
            Usd.Prim(</World>)
        
    """
def get_prim_path(prim: pxr.Usd.Prim) -> str:
    """
    Get the path of a given USD prim.
    
        Args:
            prim (Usd.Prim): The input USD prim.
    
        Returns:
            str: The path to the input prim.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> prim = prims_utils.get_prim_at_path("/World/Cube")  # Usd.Prim(</World/Cube>)
            >>> prims_utils.get_prim_path(prim)
            /World/Cube
        
    """
def get_prim_property(prim_path: str, property_name: str) -> typing.Any:
    """
    Get the attribute of the USD Prim at the given path
    
        Args:
            prim_path (str): path of the prim in the stage
            property_name (str): name of the attribute to get
    
        Returns:
            typing.Any: The attribute if it exists, None otherwise
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> prims_utils.get_prim_property("/World/Cube", property_name="size")
            1.0
        
    """
def get_prim_type_name(prim_path: str, fabric: bool = False) -> str:
    """
    Get the TypeName of the USD Prim at the path if it is valid
    
        Args:
            prim_path (str): path of the prim in the stage
            fabric (bool, optional): True for fabric stage and False for USD stage. Defaults to False.
    
        Raises:
            Exception: If there is not a valid prim at the given path
    
        Returns:
            str: The TypeName of the USD Prim at the path string
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> prims_utils.get_prim_type_name("/World/Cube")
            Cube
        
    """
def is_prim_ancestral(prim_path: str) -> bool:
    """
    Check if any of the prims ancestors were brought in as a reference
    
        Args:
            prim_path (str): The path to the USD prim.
    
        Returns:
            True if prim is part of a referenced prim, false otherwise.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> # /World/Cube is a prim created
            >>> prims_utils.is_prim_ancestral("/World/Cube")
            False
            >>> # /World/panda is an USD file loaded (as reference) under that path
            >>> prims_utils.is_prim_ancestral("/World/panda")
            False
            >>> prims_utils.is_prim_ancestral("/World/panda/panda_link0")
            True
        
    """
def is_prim_hidden_in_stage(prim_path: str) -> bool:
    """
    Checks if the prim is hidden in the USd stage or not.
    
        .. warning ::
    
            This function checks for the ``hide_in_stage_window`` prim metadata.
            This metadata is not related to the visibility of the prim.
    
        Args:
            prim_path (str): The path to the USD prim.
    
        Returns:
            True if prim is hidden from stage window, False if not hidden.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> # prim without the 'hide_in_stage_window' metadata
            >>> prims_utils.is_prim_hidden_in_stage("/World/Cube")
            None
            >>> # prim with the 'hide_in_stage_window' metadata set to True
            >>> prims_utils.is_prim_hidden_in_stage("/World/Cube")
            True
        
    """
def is_prim_no_delete(prim_path: str) -> bool:
    """
    Checks whether a prim can be deleted or not from USD stage.
    
        .. note ::
    
            This function checks for the ``no_delete`` prim metadata. A prim with this
            metadata set to True cannot be deleted by using the edit menu, the context menu,
            or by calling the ``delete_prim`` function, for example.
    
        Args:
            prim_path (str): The path to the USD prim.
    
        Returns:
            True if prim cannot be deleted, False if it can
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> # prim without the 'no_delete' metadata
            >>> prims_utils.is_prim_no_delete("/World/Cube")
            None
            >>> # prim with the 'no_delete' metadata set to True
            >>> prims_utils.is_prim_no_delete("/World/Cube")
            True
        
    """
def is_prim_non_root_articulation_link(prim_path: str) -> bool:
    """
    Used to query if the prim_path corresponds to a link in an articulation which is a non root link.
    
        Args:
            prim_path (str): prim_path to query
    
        Returns:
            bool: True if the prim path corresponds to a link in an articulation which is a non root link
                  and can't have a transformation applied to it.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> # /World/panda contains the prim tree for the Franka panda robot.
            >>> # The prim on this path has the Physics Articulation Root property applied
            >>> prims_utils.is_prim_non_root_articulation_link("/World/panda")
            False
            >>> prims_utils.is_prim_non_root_articulation_link("/World/panda/panda_link0")
            True
        
    """
def is_prim_path_valid(prim_path: str, fabric: bool = False) -> bool:
    """
    Check if a path has a valid USD Prim at it
    
        Args:
            prim_path (str): path of the prim in the stage
            fabric (bool, optional): True for fabric stage and False for USD stage. Defaults to False.
    
        Returns:
            bool: True if the path points to a valid prim
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> # given the stage: /World/Cube
            >>> prims_utils.is_prim_path_valid("/World/Cube")
            True
            >>> prims_utils.is_prim_path_valid("/World/Cube/")
            False
            >>> prims_utils.is_prim_path_valid("/World/Sphere")  # it doesn't exist
            False
        
    """
def is_prim_root_path(prim_path: str) -> bool:
    """
    Checks if the input prim path is root or not.
    
        Args:
            prim_path (str): The path to the USD prim.
    
        Returns:
            True if the prim path is "/", False otherwise
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> # given the stage: /World/Cube
            >>> prims_utils.is_prim_root_path("/")
            True
            >>> prims_utils.is_prim_root_path("/World")
            False
            >>> prims_utils.is_prim_root_path("/World/Cube")
            False
        
    """
def move_prim(path_from: str, path_to: str) -> None:
    """
    Run the Move command to change a prims USD Path in the stage
    
        Args:
            path_from (str): Path of the USD Prim you wish to move
            path_to (str): Final destination of the prim
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> # given the stage: /World/Cube. Move the prim Cube outside the prim World
            >>> prims_utils.move_prim("/World/Cube", "/Cube")
        
    """
def query_parent_path(prim_path: str, predicate: typing.Callable[[str], bool]) -> bool:
    """
    Check if one of the ancestors of the prim at the prim_path can pass the predicate
    
        Args:
            prim_path (str): path to the USD Prim for which to check the ancestors
            predicate (typing.Callable[[str], bool]): The condition that must be True about the ancestors
    
        Returns:
            bool: True if there is an ancestor that can pass the predicate, False otherwise
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> # given the stage: /World/Cube. Check is the prim Cube has an ancestor of type Xform
            >>> predicate = lambda path: prims_utils.get_prim_type_name(path) == "Xform"
            >>> prims_utils.query_parent_path("/World/Cube", predicate)
            True
        
    """
def set_prim_attribute_value(prim_path: str, attribute_name: str, value: typing.Any, fabric: bool = False):
    """
    Set a prim attribute value
    
        Args:
            prim_path (str): path of the prim in the stage
            attribute_name (str): name of the attribute to set
            value (typing.Any): value to set the attribute to
            fabric (bool, optional): True for fabric stage and False for USD stage. Defaults to False.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> # given the stage: /World/Cube. Set the Cube size to 5.0
            >>> prims_utils.set_prim_attribute_value("/World/Cube", attribute_name="size", value=5.0)
        
    """
def set_prim_hide_in_stage_window(prim: pxr.Usd.Prim, hide: bool):
    """
    Set ``hide_in_stage_window`` metadata for a prim
    
        .. warning ::
    
            This metadata is unrelated to the visibility of the prim.
            Use the ``set_prim_visibility`` function for the latter purpose
    
        Args:
            prim (Usd.Prim): Prim to set
            hide (bool): True to hide in stage window, false to show
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> prim = prims_utils.get_prim_at_path("/World/Cube")
            >>> prims_utils.set_prim_hide_in_stage_window(prim, True)
        
    """
def set_prim_no_delete(prim: pxr.Usd.Prim, no_delete: bool):
    """
    Set ``no_delete`` metadata for a prim
    
        .. note ::
    
            A prim with this metadata set to True cannot be deleted by using the edit menu,
            the context menu, or by calling the ``delete_prim`` function, for example.
    
        Args:
            prim (Usd.Prim): Prim to set
            no_delete (bool):True to make prim undeletable in stage window, false to allow deletion
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> prim = prims_utils.get_prim_at_path("/World/Cube")
            >>> prims_utils.set_prim_no_delete(prim, True)
        
    """
def set_prim_property(prim_path: str, property_name: str, property_value: typing.Any) -> None:
    """
    Set the attribute of the USD Prim at the path
    
        Args:
            prim_path (str): path of the prim in the stage
            property_name (str): name of the attribute to set
            property_value (typing.Any): value to set the attribute to
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> # given the stage: /World/Cube. Set the Cube size to 5.0
            >>> prims_utils.set_prim_property("/World/Cube", property_name="size", property_value=5.0)
        
    """
def set_prim_visibility(prim: pxr.Usd.Prim, visible: bool) -> None:
    """
    Sets the visibility of the prim in the opened stage.
    
        .. note::
    
            The method does this through the USD API.
    
        Args:
            prim (Usd.Prim): the USD prim
            visible (bool): flag to set the visibility of the usd prim in stage.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> # given the stage: /World/Cube. Make the Cube not visible
            >>> prim = prims_utils.get_prim_at_path("/World/Cube")
            >>> prims_utils.set_prim_visibility(prim, False)
        
    """
def set_targets(prim: pxr.Usd.Prim, attribute: str, target_prim_paths: list):
    """
    Set targets for a prim relationship attribute
    
        Args:
            prim (Usd.Prim): Prim to create and set attribute on
            attribute (str): Relationship attribute to create
            target_prim_paths (list): list of targets to set
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.prims as prims_utils
            >>>
            >>> # given the stage: /World/Cube, /World/Cube_01, /World/Cube_02.
            >>> # Set each prim Cube to the relationship targetPrim of the prim World
            >>> prim = prims_utils.get_prim_at_path("/World")
            >>> targets = ["/World/Cube", "/World/Cube_01", "/World/Cube_02"]
            >>> prims_utils.set_targets(prim, "targetPrim", targets)
        
    """
SDF_type_to_Gf: dict = {'matrix3d': 'Gf.Matrix3d', 'matrix3f': 'Gf.Matrix3f', 'matrix4d': 'Gf.Matrix4d', 'matrix4f': 'Gf.Matrix4f', 'quatd': 'Gf.Quatd', 'quatf': 'Gf.Quatf', 'quath': 'Gf.Quath', 'range1d': 'Gf.Range1d', 'range1f': 'Gf.Range1f', 'range2d': 'Gf.Range2d', 'range2f': 'Gf.Range2f', 'range3d': 'Gf.Range3d', 'range3f': 'Gf.Range3f', 'rect2i': 'Gf.Rect2i', 'vec2d': 'Gf.Vec2d', 'vec2f': 'Gf.Vec2f', 'vec2h': 'Gf.Vec2h', 'vec2i': 'Gf.Vec2i', 'vec3d': 'Gf.Vec3d', 'double3': 'Gf.Vec3d', 'vec3f': 'Gf.Vec3f', 'vec3h': 'Gf.Vec3h', 'vec3i': 'Gf.Vec3i', 'vec4d': 'Gf.Vec4d', 'vec4f': 'Gf.Vec4f', 'vec4h': 'Gf.Vec4h', 'vec4i': 'Gf.Vec4i'}
