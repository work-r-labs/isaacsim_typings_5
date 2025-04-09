"""
This module defines the UsdShadePropertyPlaceholder class, which acts as a stand-in for Usd.Attribute for use in UsdShade widgets without serializing default properties and metadata to USD files.
"""
from __future__ import annotations
import omni as omni
from pxr import Sdf
from pxr import Sdr
import pxr.Usd
from pxr import Usd
from pxr import UsdShade
import typing
__all__: list = ['UsdShadePropertyPlaceholder']
class UsdShadePropertyPlaceholder:
    """
    This class serves as a stand-in for Usd.Attribute within the context of various UsdShade widgets.
    
        By default, the UsdPropertiesWidget widget is driven by Usd.Attributes, and if we want to display properties for a prim, then those properties need to exist on the stage. This is problematic for UsdShade properties as we don't want to serialize properties whose values have not been changed from their default. We also don't want to serialize all of the corresponding metadata these properties may contain, doing so results in unnecessarily bloated USD files. Therefore, this class can serve as a stand-in. It contains all of the necessary functions required by the UI widgets and allows us to display all of the parameters for a UsdShade.Shader that are defined via an Sdr.ShaderNode definition without having to store them on the stage and/or session layer first. These objects also provide a convenient means for overwriting metadata used to drive the display without having to serialize.
    
        Args:
            name (str): The name of the property.
            metadata (Union[dict | None]): The metadata associated with the property.
            from_sdr (bool): Indicates whether the property is from SDR.
    """
    MATERIAL_INPUT_SUFFIX: typing.ClassVar[str] = '__material_input__'
    @classmethod
    def PlaceholderFromAttribute(cls, usd_attribute: pxr.Usd.Attribute):
        """
        
                Create a UsdShadePropertyPlaceholder from a Usd.Attribute.
        
                Args:
                    usd_attribute (Usd.Attribute)
        
                Returns:
                    UsdShadePropertyPlaceholder
        """
    def FromSdr(self) -> bool:
        """
        Indicates if the property placeholder was created from an Sdr node.
        
                Returns:
                    bool: True if created from Sdr, False otherwise.
        """
    def GetAllMetadata(self) -> dict:
        """
        Retrieves all metadata associated with the property.
        
                Returns:
                    dict: A dictionary of all metadata.
        """
    def GetAllSdrMetadata(self) -> typing.Dict:
        ...
    def GetColorSpace(self) -> typing.Optional[str]:
        """
        Gets the color space of the property.
        
                Returns:
                    Union[str, None]: The color space of the property, or None if not set.
        """
    def GetConnectability(self) -> typing.Optional[str]:
        ...
    def GetDefaultValue(self) -> typing.Optional[typing.Any]:
        """
        Gets the default value of the property.
        
                Returns:
                    Union[Any, None]: The default value of the property, or None if not set.
        """
    def GetDisplayGroup(self) -> str:
        """
        Gets the display group of the property.
        
                Returns:
                    str: The display group of the property.
        """
    def GetDisplayName(self) -> str:
        """
        Gets the display name of the property.
        
                Returns:
                    str: The display name of the property.
        """
    def GetDocumentation(self) -> typing.Optional[str]:
        ...
    def GetEnableIfCondition(self) -> typing.Optional[str]:
        """
        Gets the enable-if condition for the property.
        
                Returns:
                    Union[str, None]: The enable-if condition, or None if not set.
        """
    def GetHidden(self) -> bool:
        ...
    def GetMdlArrayElementType(self) -> typing.Optional[str]:
        ...
    def GetMdlModifier(self) -> str:
        ...
    def GetMdlStructType(self) -> typing.Optional[str]:
        ...
    def GetMdlSymbol(self) -> typing.Optional[str]:
        ...
    def GetMetadata(self, key: str) -> typing.Optional[typing.Any]:
        """
        Retrieves the metadata value for the given key.
        
                Args:
                    key (str): The metadata key to query.
        
                Returns:
                    Union[Any, None]: The value of the given metadata key, or None if not set.
        """
    def GetName(self) -> str:
        """
        Retrieves the name of the property.
        
                Returns:
                    str: The name of the property.
        """
    def GetPropertyType(self):
        """
        Gets the type of the property represented by the placeholder.
        
                Returns:
                    :obj:`Usd.Attribute`: The type of property.
        """
    def GetRenderType(self) -> typing.Optional[str]:
        ...
    def GetSdrMetadata(self, key, default_value = None) -> typing.Optional[typing.Any]:
        ...
    def GetTypeName(self) -> typing.Optional[str]:
        """
        Gets the type name of the property.
        
                Returns:
                    Union[str, None]: The type name of the property, or None if not set.
        """
    def HasMetadata(self, key) -> bool:
        """
        Checks if the specified metadata key is present.
        
                Args:
                    key (str): The metadata key to check.
        
                Returns:
                    bool: True if the key is present, False otherwise.
        """
    def IsHidden(self) -> bool:
        """
        Checks if the property is hidden.
        
                Returns:
                    bool: True if the property is hidden, False otherwise.
        """
    def SetColorSpace(self, value: str) -> None:
        """
        Sets the color space of the property.
        
                Args:
                    value (str): The new color space for the property.
        """
    def SetDisplayGroup(self, value: str) -> None:
        """
        Sets the display group of the property.
        
                Args:
                    value (str): The new display group for the property.
        """
    def SetDisplayName(self, value: str) -> None:
        """
        Sets the display name of the property.
        
                Args:
                    value (str): The new display name for the property.
        """
    def SetHidden(self, value: bool) -> None:
        """
        Sets the hidden state of the property.
        
                Args:
                    value (bool): The new hidden state for the property.
        """
    def SetMetadata(self, key: str, value: typing.Any) -> None:
        """
        Sets the metadata key to the given value.
        
                Args:
                    key (str): The metadata key.
                    value (Any): The value to associate with the key.
        """
    def SetName(self, name: str) -> None:
        """
        Sets the name of the property.
        
                Args:
                    name (str): The new name for the property.
        """
    def __init__(self, name: str, metadata: typing.Optional[dict], from_sdr: bool = False):
        """
        Initializer for the UsdShadePropertyPlaceholder class.
        """
