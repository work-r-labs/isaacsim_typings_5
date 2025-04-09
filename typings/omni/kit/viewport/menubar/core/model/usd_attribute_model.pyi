from __future__ import annotations
import math as math
import omni as omni
from omni.kit.viewport.menubar.core.model.usd_object_model import USDObjectModel
from pxr import Gf
import pxr.Sdf
from pxr import Sdf
import pxr.Usd
from pxr import Usd
from pxr import UsdUtils
__all__: list = ['USDAttributeModel', 'USDIntAttributeModel', 'USDFloatAttributeModel', 'USDStringAttributeModel']
class USDAttributeModel(omni.kit.viewport.menubar.core.model.usd_object_model.USDObjectModel):
    """
    A simple value model to watch the specified attribute.
    """
    def __init__(self, stage: pxr.Usd.Stage, path: pxr.Sdf.Path, prop_name: str, prop_type: pxr.Sdf.ValueTypeNames = None, draggable: bool = False):
        """
        
                Constructor.
        
                Args:
                    stage (Usd.Stage): USD stage.
                    path (Sdf.Path): Path in stage.
                    prop_name (str): Attribute name.
        
                Keyword Args:
                    prop_type (Sdf.ValueTypeNames): Attribute type, defaults to None means get type from attribute value.
                    draggable (bool): Widget that model bind to can be dragged, defaults to False.
                
        """
    def _get_value(self) -> typing.Any:
        """
        Get the value directly from USD
        """
    def _is_value_changed(self, prev, current):
        ...
    def get_type_name(self, value: typing.Any) -> typing.Optional[pxr.Sdf.ValueTypeNames]:
        """
        Return the explicitly requested property type, or one auto-deduced from the value
        """
    def set_value(self, value: typing.Any) -> None:
        """
        
                Set the value directly to USD.
        
                Args:
                    value (Any): Value to set.
                
        """
class USDBoolAttributeModel(USDAttributeModel):
    """
    A simple value model to watch the boolean attribute.
    """
    def __init__(self, stage: pxr.Usd.Stage, path: pxr.Sdf.Path, prop_name: str):
        """
        
                Constructor.
        
                Args:
                    stage (Usd.Stage): USD stage.
                    path (Sdf.Path): Path in stage.
                    prop_name (str): Attribute name.
                
        """
    def set_value(self, value: bool):
        """
        
                Set the value directly to USD.
        
                Args:
                    value (bool): New value to set.
                
        """
class USDFloatAttributeModel(USDAttributeModel):
    """
    A simple value model to watch the float attribute.
    """
    def __init__(self, stage: pxr.Usd.Stage, path: pxr.Sdf.Path, prop_name: str, draggable: bool = False):
        """
        
                Constructor.
        
                Args:
                    stage (Usd.Stage): USD stage.
                    path (Sdf.Path): Path in stage.
                    prop_name (str): Attribute name.
        
                Keyword Args:
                    draggable (bool): Widget that model bind to can be dragged, defaults to False.
                
        """
    def _is_value_changed(self, prev, current):
        ...
    def set_value(self, value: float):
        """
        
                Set the value directly to USD.
        
                Args:
                    value (float): New value to set.
                
        """
class USDIntAttributeModel(USDAttributeModel):
    """
    A simple value model to watch the integer attribute.
    """
    def __init__(self, stage: pxr.Usd.Stage, path: pxr.Sdf.Path, prop_name: str):
        """
        
                Constructor.
        
                Args:
                    stage (Usd.Stage): USD stage.
                    path (Sdf.Path): Path in stage.
                    prop_name (str): Attribute name.
                
        """
    def set_value(self, value: int):
        """
        
                Set the value directly to USD.
        
                Args:
                    value (int): New value to set.
                
        """
class USDStringAttributeModel(USDAttributeModel):
    """
    A simple value model to watch the string attribute.
    """
    def __init__(self, stage: pxr.Usd.Stage, path: pxr.Sdf.Path, prop_name: str):
        """
        
                Constructor.
        
                Args:
                    stage (Usd.Stage): USD stage.
                    path (Sdf.Path): Path in stage.
                    prop_name (str): Attribute name.
                
        """
    def set_value(self, value: str):
        """
        
                Set the value directly to USD.
        
                Args:
                    value (str): New value to set.
                
        """
