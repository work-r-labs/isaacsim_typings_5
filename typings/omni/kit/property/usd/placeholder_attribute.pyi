from __future__ import annotations
import carb as carb
from pxr import Sdf
from pxr import UsdGeom
from pxr import UsdShade
__all__: list = ['PlaceholderAttribute']
class PlaceholderAttribute:
    """
    This is a placeholder for Usd.Attribute object as those objects have to be attached to a Usd.Prim object.
        This conforms to enough of the Usd.Attribute API to be used by omni.kit.property.usd widgets.
    
        The purpose of this is so custom Usd.Attributes can be created and displayed by widgets but don't actually effect the Usd.Prim until user modifies a value,
        then the `CreateAttribute` function will be called and a real Usd.Attribute will be created using values from this class.
    """
    def CreateAttribute(self):
        """
        Create the Usd.Attribute in the Usd.Prim
        """
    def Get(self, time_code = 0):
        """
        Mock Usd.Attribute function
        """
    def GetAllMetadata(self):
        """
        Mock Usd.Attribute function
        """
    def GetMetadata(self, token):
        """
        Mock Usd.Attribute function
        """
    def GetPath(self):
        """
        Mock Usd.Attribute function
        """
    def GetPrim(self):
        """
        Mock Usd.Attribute function
        """
    def GetPropertyStack(self, *args, **kwargs):
        ...
    def HasAuthoredConnections(self):
        """
        Mock Usd.Attribute function
        """
    def IsHidden(self):
        """
        Mock Usd.Attribute function
        """
    def ValueMightBeTimeVarying(self):
        """
        Mock Usd.Attribute function
        """
    def __init__(self, name, prim = None, metadata = None):
        """
        Initializes the PlaceholderAttribute.
        
                Args:
                    name (str): Name of the mock Usd.Prim.
                    prim: (Usd.Prim): Prim attribute is attached to.
                    metadata: (dict): metadata of mock attribute.
        """
