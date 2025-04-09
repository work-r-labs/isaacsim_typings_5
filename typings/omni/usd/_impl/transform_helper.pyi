from __future__ import annotations
import omni as omni
from pxr import Sdf
from pxr import Usd
__all__ = ['Sdf', 'TransformHelper', 'Usd', 'omni']
class TransformHelper:
    """
    Internal. Helper to handle transform attributes.
    """
    def __init__(self):
        ...
    def add_to_attr_order(self, attr_order, path, use_placeholder = False):
        ...
    def get_transform_attr(self, attrs: typing.List[pxr.Usd.Attribute]) -> typing.Tuple[pxr.Usd.Attribute, typing.List[pxr.Usd.Attribute], pxr.Usd.Attribute, pxr.Usd.Attribute]:
        """
        Finds all transform attributes from list.
        
                Args:
                    attrs (List[Usd.Attribute]): A list of attributes.
        
                Returns:
                    Tuple[Usd.Attribute, List[Usd.Attribute], Usd.Attribute, Usd.Attribute]: A tuple that includes
                        tranlate, list of rotations, scale, and order attributes. It's None or empty if corresponding attribute is
                        not found.
                
        """
    def is_common_attr(self, source_attr):
        ...
    def is_transform(self, source_path: str) -> bool:
        """
        If the source name is an attribute path with xformOp.
        
                Args:
                    source_path (str): The attribute name.
        
                Returns:
                    bool: True if the source name is an transform attribute, or False otherwise.
                
        """
    def order_attrs(self, attrs, order):
        ...
