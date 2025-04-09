"""
This module provides utilities for material binding in USD stages, including defining constants, updating material data, retrieving material bindings for primitives, and creating non-persistent attributes for materials.
"""
from __future__ import annotations
import carb as carb
import omni as omni
from pxr import Sdf
from pxr import Usd
from pxr import UsdShade
import typing
__all__: list = ['Constant']
class Constant:
    """
    A class that defines constants for a USD stage material binding tool.
    
        This class contains various constants such as icon size, label width, font size, and
        special identifiers for missing paths or mixed values. It also ensures that its
        attributes are immutable by raising a ValueError if an attempt is made to
        set an attribute. The class checks the validity of certain constants during
        initialization to ensure correctness of the defined values.
    """
    BOUND_LABEL_WIDTH: typing.ClassVar[int] = 50
    FONT_SIZE: typing.ClassVar[float] = 14.0
    ICON_SIZE: typing.ClassVar[int] = 96
    MIXED: typing.ClassVar[str] = 'Mixed'
    MIXED_COLOR: typing.ClassVar[int] = 4291599969
    PERSISTENT_SETTINGS_PREFIX: typing.ClassVar[str] = '/persistent'
    SDF_PATH_INVALID: typing.ClassVar[str] = '$NONE$'
    def __setattr__(self, name, value):
        ...
def _populate_data(stage, material_data, collection_or_prim, material = None, relationship = None, material_missing = False):
    ...
def create_nonpersistant_attribute(material_paths, name, sdf_value_type_name, value):
    """
    Creates non-persistent attributes for a set of material paths.
    
        This function generates attribute specifications on the current stage's session layer for each
        material path provided. These attributes are marked as non-persistent and hidden. The attributes
        are created with a specified SDF value type and a default value.
    
        Args:
            material_paths (List[:obj:`Sdf.Path`]): A list of SDF Paths where the attributes will be created.
            name (str): The name of the attribute to create.
            sdf_value_type_name (str): The SDF value type name for the attribute.
            value (Any): The default value to set for the created attribute.
        
    """
def get_binding_from_prims(stage, prim_paths, material_purpose = ''):
    """
    Retrieves material bindings for a given set of primitive paths on a USD stage.
    
        Args:
            stage (:obj:`Usd.Stage`): The USD stage from which to retrieve material bindings.
            prim_paths (List[:obj:`Sdf.Path`]): A list of SDF paths representing the primitives for which material bindings are to be retrieved.
            material_purpose (str, optional): The purpose of the material binding to retrieve. Defaults to UsdShade.Tokens.allPurpose.
    
        Returns:
            dict: A dictionary containing material binding information for the specified primitives.
    """
