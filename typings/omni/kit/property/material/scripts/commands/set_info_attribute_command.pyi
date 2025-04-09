"""
This module provides the SetUsdShadeInfoAttributeCommand class for changing property values of UsdShade info attributes and handling related property and connection updates.
"""
from __future__ import annotations
import omni as omni
from omni.kit.property.material.scripts.widgets.usdshade.utils import remove_properties_and_connections
from omni.usd.commands.usd_commands import ChangePropertyCommand
import pxr.Sdf
from pxr import Sdf
from pxr import Usd
import typing
__all__: list = ['SetUsdShadeInfoAttributeCommand']
class SetUsdShadeInfoAttributeCommand(omni.usd.commands.usd_commands.ChangePropertyCommand):
    """
    Change property value for UsdShade info.* attributes.
    
        In addition to what is done by ChangePropertyCommand, this command processes the UsdShade network and does the following:
        1. Remove any properties that no longer exist or whose types have changed.
        2. Remove any connections to/from this node that are no longer valid due to property removal or type change.
    
        Args:
            prop_path (str): The property path.
            value (Any): The new value to set.
            prev (Any): The previous value.
            timecode (Optional[Usd.TimeCode]): The timecode at which the change should happen.
            type_to_create_if_not_exist (Optional[:obj:`Sdf.ValueTypeNames`]): The type to create if it does not exist.
            target_layer (Optional[:obj:`Sdf.Layer`]): The target layer for the change.
            usd_context_name (Union[str, :obj:`omni.usd.UsdContext`, :obj:`Usd.Stage`]): The USD context name or stage.
            is_custom (bool): Specifies if the attribute is custom.
            variability (Optional[:obj:`Sdf.Variability`]): The variability of the attribute.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prop_path: str, value: typing.Any, prev: typing.Any, timecode = None, type_to_create_if_not_exist: pxr.Sdf.ValueTypeNames = None, target_layer: pxr.Sdf.Layer = None, usd_context_name: typing.Union[str, omni.usd._usd.UsdContext, pxr.Usd.Stage] = '', is_custom: bool = False, variability: pxr.Sdf.Variability = ...):
        """
        Initialize the command to set USD Shade info attribute values.
        """
    def _set_prop_value(self) -> bool:
        ...
    def undo(self):
        """
        Revert the changes made by the command.
        """
