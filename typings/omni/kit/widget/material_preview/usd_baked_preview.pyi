from __future__ import annotations
import base64 as base64
import enum
from enum import Enum
from pxr import Sdf
import pxr.Usd
from pxr import Usd
import typing
import zlib as zlib
__all__: list = ['UsdBakedPreview']
class UsdBakedPreview:
    """
    ApiSchema-like object to store image preview on the prim
    """
    class PreviewType(enum.Enum):
        """
        An enumeration.
        """
        ZIP: typing.ClassVar[UsdBakedPreview.PreviewType]  # value = <PreviewType.ZIP: 0>
    ATTR_NAME: typing.ClassVar[str] = 'omni:baked_preview'
    def __init__(self, prim: pxr.Usd.Prim):
        ...
    def create_baked_preview_attr(self) -> typing.Optional[pxr.Usd.Attribute]:
        """
        Creates and returns the baked preview attribute
        """
    def get_baked_preview_attr(self) -> typing.Optional[pxr.Usd.Attribute]:
        """
        Returns the baked preview attribute
        """
    def get_baked_preview_data(self) -> typing.Optional[typing.Tuple[typing.List[int], int, int]]:
        """
        Returns baked preview (data, width, height)
        """
    def has_baked_preview_attr(self) -> typing.Optional[bool]:
        """
        True when the prim has the baked preview attribute
        """
    def set_baked_preview_data(self, data, width, height, format, data_type: UsdBakedPreview.PreviewType = ...):
        """
        
                Serializes bytes data to string and sets baked preview attribute.
                
        """
