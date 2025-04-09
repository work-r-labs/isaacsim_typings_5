"""
Provides a property scheme delegate for building widget schemes based on USD geometric primitives.
"""
from __future__ import annotations
import omni.kit.window.property.property_scheme_delegate
from omni.kit.window.property.property_scheme_delegate import PropertySchemeDelegate
from pxr import UsdGeom
from pxr import UsdLux
from pxr import UsdMedia
from pxr import UsdSkel
__all__ = ['GeomPrimSchemeDelegate', 'PropertySchemeDelegate', 'UsdGeom', 'UsdLux', 'UsdMedia', 'UsdSkel']
class GeomPrimSchemeDelegate(omni.kit.window.property.property_scheme_delegate.PropertySchemeDelegate):
    """
    A delegate class that provides widget building schemes for geometric primitives in a property window.
    
        This class extends the PropertySchemeDelegate and overrides methods to determine the appropriate widgets to display or hide, based on the type of USD geometric primitives encountered. The widget construction is primarily guided by the type of the USD primitive provided in the payload, such as UsdGeom.Mesh, UsdGeom.Camera, or UsdLux.Light among others. It caters to both the inclusion of relevant widgets and the exclusion of irrelevant or unwanted widgets for a given primitive.
        
    """
    def get_unwanted_widgets(self, payload):
        """
        Identifies unwanted widgets for removal based on the given payload.
        
                Args:
                    payload (dict): Payload containing stage and prim paths to identify unwanted widgets.
        
                Returns:
                    list: A list of unwanted widget names.
        """
    def get_widgets(self, payload):
        """
        Determines widgets to build based on the given payload.
        
                Args:
                    payload (dict): Payload containing stage and prim paths to determine widgets.
        
                Returns:
                    list: A list of widget names to be built.
        """
