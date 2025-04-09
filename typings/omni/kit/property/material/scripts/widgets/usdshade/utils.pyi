"""
This module provides utilities for manipulating USDShade and SDR shader properties, including finding shader nodes, getting shader information, updating dictionary values, and handling shader properties and connections in USD.
"""
from __future__ import annotations
import collections as collections
import omni as omni
from omni.kit.property.material.scripts.widgets.usdshade.placeholder import GetPlaceholderPropertiesForPrim
from omni.kit.property.material.scripts.widgets.usdshade.placeholder.placeholder import UsdShadePropertyPlaceholder
from pxr import Ar
from pxr import Sdf
import pxr.Sdr
from pxr import Sdr
import pxr.Usd
from pxr import Usd
from pxr import UsdShade
import pxr.UsdShade
import re as re
__all__: list = ['get_sdr_shader_node_for_prim', 'get_shader_info', 'property_name_to_display_name', 'create_nonpersistant_attribute', 'get_mdl_subidentifiers_for_prim', 'get_info_ids_for_prim', 'deep_dict_update', 'get_display_group_for_render_context', 'get_sdr_shader_property_default_value', 'remove_properties_and_connections']
def create_nonpersistant_attribute(material_paths, name, sdf_value_type_name, value):
    """
    Creates a non-persistent attribute for the given material paths with the specified name, type, and value.
    
        Args:
            material_paths (List[str]): A list of material paths where the attribute should be created.
            name (str): The name of the attribute to create.
            sdf_value_type_name (str): The SDF value type name for the attribute.
            value: The value to set for the attribute.
    """
def deep_dict_update(d: dict, u: dict) -> dict:
    """
    Recursively updates a dictionary by merging a second dictionary into it.
    
        Args:
            d (dict): The dictionary to be updated.
            u (dict): The dictionary with values to be merged into the first dictionary.
    
        Returns:
            dict: The updated dictionary after merging.
    """
def get_display_group_for_render_context(render_context: str) -> str:
    """
    
        Create a pretty display group name for the named render context
        
    """
def get_info_ids_for_prim(prim: pxr.Usd.Prim) -> typing.Optional[typing.List[str]]:
    """
    Returns a list of allowed tokens for the info:id property of a shader.
    
        Args:
            prim (:obj:`Usd.Prim`): The USD primitive representing the shader.
    
        Returns:
            Union[List[str], None]: A list of info:id tokens if found, otherwise None.
    """
def get_mdl_subidentifiers_for_prim(prim: pxr.Usd.Prim) -> typing.Optional[typing.List[str]]:
    """
    Retrieves the list of MDL subidentifiers associated with a given USD primitive (prim) if any exist. MDL subidentifiers are unique identifiers used to reference sub-components or variants within an MDL asset.
    
        Args:
            prim (:obj:`Usd.Prim`): The USD primitive for which to retrieve MDL subidentifiers.
    
        Returns:
            Union[List[str], None]: A sorted list of MDL subidentifiers associated with the provided USD primitive if any exist; otherwise, None.
        
    """
def get_sdr_shader_node_for_prim(prim: pxr.Usd.Prim, source_type_priority: typing.List[str] = None, warn_on_substitution: bool = False) -> typing.Optional[pxr.Sdr.ShaderNode]:
    """
    Finds and returns the Sdr.ShaderNode used to define the corresponding UsdShade.Shader prim.
    
        Args:
            prim (:obj:`Usd.Prim`): The USD primitive to find the shader node for.
            source_type_priority (Optional[List[str]]): A list of source type priorities to consider when finding the shader node.
            warn_on_substitution (bool): UsdMdl.RegistryUtils.FindShaderNodeForPrim will first try and find the Sdr.ShaderNode using the subidentifier on the prim.
                                         If it is not able to do so it attempts to find one by decuction.  If a suitable match was found this flag is used to indicate whether or not a warning should be issued.
    
        Returns:
            Union[Sdr.ShaderNode, None]: The found Sdr.ShaderNode, or None if not found.
    """
def get_sdr_shader_property_default_value(sdr_shader_property: pxr.Sdr.ShaderProperty, metadata: dict) -> typing.Optional[typing.Any]:
    """
    Returns the default value for a given SDR shader property considering the metadata.
    
        Args:
            sdr_shader_property (:obj:`Sdr.ShaderProperty`): The shader property for which the default value is being queried.
            metadata (dict): The metadata dictionary that may contain additional information to determine the default value.
    
        Returns:
            Union[Any, None]: The default value of the shader property, or None if no default can be determined.
    """
def get_shader_info(usdshade_shader: pxr.UsdShade.Shader) -> typing.Tuple[str, typing.Optional[str], typing.Optional[str]]:
    """
    Gets the shader information for a given UsdShade.Shader.
    
        Args:
            usdshade_shader (:obj:`UsdShade.Shader`): The shader to retrieve information from.
    
        Returns:
            Tuple[str, Optional[str], Optional[str]]: A tuple containing the shader's implementation source as the first element, the shader ID as the second element (if implementation source is 'id'), and the source asset sub-identifier as the third element (if implementation source is 'sourceAsset'). If the shader ID or source asset sub-identifier is not available, their respective positions in the tuple will be None.
        
    """
def property_name_to_display_name(property_name: str) -> str:
    """
    Converts a property name to a display name by splitting camel casing.
    
        Args:
            property_name (str): The property name to be converted into display name format.
    
        Returns:
            str: The converted display name with spaces.
    """
def remove_properties_and_connections(prim: pxr.Usd.Prim) -> typing.Tuple[bool, typing.List, typing.Dict]:
    """
    Remove properties and connections from a given USD Prim that are no longer valid.
    
        This function will remove properties that are no longer valid due to changing the shader node type, as well as
        disconnect any connections that are no longer valid.
    
        Args:
            prim (:obj:`Usd.Prim`): The Prim from which to remove properties and connections.
    
        Returns:
            Tuple[bool, List, Dict]: A tuple containing a boolean indicating success or failure, a list of removed properties, and a dictionary of removed connections.
        
    """
