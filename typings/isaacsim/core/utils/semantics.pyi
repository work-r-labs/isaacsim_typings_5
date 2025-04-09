import Semantics as Semantics
from __future__ import annotations
from isaacsim.core.utils import prims as prim_utils
import omni as omni
import pxr.Usd
from pxr import Usd
from pxr import UsdGeom
__all__ = ['Semantics', 'Usd', 'UsdGeom', 'add_update_semantics', 'check_incorrect_semantics', 'check_missing_semantics', 'count_semantics_in_scene', 'get_semantics', 'omni', 'prim_utils', 'remove_all_semantics']
def add_update_semantics(prim: pxr.Usd.Prim, semantic_label: str, type_label: str = 'class', suffix = '') -> None:
    """
    Apply a semantic label to a prim or update an existing label
    
        Args:
            prim (Usd.Prim): Usd Prim to add or update semantics on
            semantic_label (str): The label we want to apply
            type_label (str): The type of semantic information we are specifying (default = "class")
            suffix (str): Additional suffix used to specify multiple semantic attribute names.
            By default the semantic attribute name is "Semantics", and to specify additional
            attributes a suffix can be provided. Simple string concatenation is used :"Semantics" + suffix (default = "")
        
    """
def check_incorrect_semantics(prim_path: str = None) -> typing.List[typing.List[str]]:
    """
    Returns a list of prim path of meshes with different semantics labels than their prim path and their semantic labels
    
        Args:
            prim_path (str): This will check Prim path and its childrens' semantics
    
        Returns:
            List[List[str]]: List of prim path and semantic label
        
    """
def check_missing_semantics(prim_path: str = None) -> typing.List[str]:
    """
    Returns a list of prim path of meshes with missing semantics
    
        Args:
            prim_path (str): This will check Prim path and its childrens' semantics
    
        Returns:
            List[str]: Prim paths
        
    """
def count_semantics_in_scene(prim_path: str = None) -> typing.Dict[str, int]:
    """
    Returns a dictionary of labels and the corresponding count
    
        Args:
            prim_path (str): This will check Prim path and its childrens' semantics
    
        Returns:
            Dict[str, int]: labels and count
        
    """
def get_semantics(prim: pxr.Usd.Prim) -> typing.Dict[str, typing.Tuple[str, str]]:
    """
    Returns semantics that are applied to a prim
    
        Args:
            prim (Usd.Prim): Prim to return semantics for
    
        Returns:
            Dict[str, Tuple[str,str]]: Dictionary containing the name of the applied semantic, and the type and data associated with that semantic.
        
    """
def remove_all_semantics(prim: pxr.Usd.Prim, recursive: bool = False) -> None:
    """
    Removes all semantic tags from a given prim and its children
    
        Args:
            prim (Usd.Prim): Prim to remove any applied semantic APIs on
            recursive (bool, optional): Also traverse children and remove semantics recursively. Defaults to False.
        
    """
