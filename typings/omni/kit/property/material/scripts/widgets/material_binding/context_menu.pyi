"""
This module provides functionality for material selection and manipulation in a context menu, including checking material selection, copying, pasting, and navigating to materials within the USD stage.
"""
from __future__ import annotations
import carb as carb
import omni as omni
from pxr import Usd
from pxr import UsdShade
__all__: list = list()
def copy_material(objects: dict, copy_all: bool):
    """
    Copies the materials bound to the selected prims into the clipboard.
    
        Args:
            objects (dict): A dictionary containing 'prim_list', which is a list of
                prims whose materials are to be copied.
            copy_all (bool): A flag indicating whether to copy all materials or not.
    
        
    """
def get_paste_name(objects):
    """
    Generates a name for the paste operation based on the number of materials in the clipboard.
    
        Args:
            objects (dict): The dictionary containing references to various objects such as materials, prims, etc.
    
        Returns:
            str: A string indicating the paste operation name. If only one material is in the clipboard, it returns 'Paste'; otherwise,
                 it includes the number of materials in parentheses, e.g., 'Paste (3 Materials)'.
    """
def goto_material(objects):
    """
    Navigates to the selected material in the USD stage.
    
        Args:
            objects (dict): A dictionary containing the 'material_prim' key with the material primitive to navigate to.
        
    """
def is_bindable_prim_selected(objects):
    """
    Checks if any selected prim is supported for material binding.
    
        Args:
            objects (dict): A dictionary with 'stage' key providing access to USD stage.
    
        Returns:
            bool: True if at least one selected prim is bindable, False otherwise.
    """
def is_material_copied(objects):
    """
    Checks if any material has been copied to the clipboard.
    
        Args:
            objects (dict): A dictionary containing relevant data and objects for the operation.
    
        Returns:
            bool: True if the material clipboard is not empty, False otherwise.
    """
def is_material_selected(objects):
    """
    Checks if a material is selected.
    
        Args:
            objects (dict): A dictionary containing the material primitive under the key 'material_prim'.
    
        Returns:
            bool: True if the material primitive is not None, False otherwise.
    """
def is_multiple_material_selected(objects):
    """
    Determines if more than one material is selected.
    
        Args:
            objects (dict): A dictionary containing the stage object with key 'stage' to access USD prim paths.
    
        Returns:
            bool: True if more than one unique material is selected, False otherwise.
    """
def is_paste_all(objects):
    """
    Determines whether the paste all operation is applicable.
    
        Args:
            objects (dict): A dictionary containing the USD stage and prim information.
    
        Returns:
            bool: True if the number of selected prim paths is greater than the number of materials in the clipboard, otherwise False.
        
    """
def is_prim_selected(self, objects: dict):
    """
    Checks if any prims are selected in the given objects.
    
        Args:
            self: The instance of the class.
            objects (dict): A dictionary containing prims and related information, expected to
                have 'prim' or 'prim_list' as keys to check for selected prims.
    
        Returns:
            bool: True if any prim is selected, False otherwise.
    """
def paste_material(objects: dict):
    """
    Pastes copied material(s) to selected prim paths in the USD stage.
    
        Args:
            objects (dict): A dictionary containing the USD stage and potentially other relevant information required to perform the paste operation.
        
    """
def paste_material_all(objects: dict):
    """
    Pastes material to selected prims in a round-robin fashion from a clipboard.
    
        Args:
            objects (dict): A dictionary containing the stage and possibly other relevant information for
                operation. Expected to have a 'stage' key with a value that allows access to prims via
                GetPrimAtPath method.
    """
def show_context_menu(stage, material_path, bound_prims: typing.Set[pxr.Usd.Prim]):
    """
    Displays a context menu for material-related actions on the given stage and bound prims.
    
        Args:
            stage (:obj:`Usd.Stage`): The USD stage where the operations will be performed.
            material_path (str): The path to the material in the USD stage.
            bound_prims (Set[:obj:`Usd.Prim`]): A set of USD Prims that are bound to the material.
    """
material_clipboard: list = list()
