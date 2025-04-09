"""
This module provides the BundlePropertyWidgets class for registering and managing custom property widgets in the Omniverse Kit application.
"""
from __future__ import annotations
import omni as omni
from omni.kit.property.bundle.geom_scheme_delegate import GeomPrimSchemeDelegate
from omni.kit.property.bundle.material_scheme_delegate import MaterialPrimSchemeDelegate
from omni.kit.property.bundle.material_scheme_delegate import ShaderPrimSchemeDelegate
from omni.kit.property.bundle.path_scheme_delegate import PathPrimSchemeDelegate
__all__ = ['BundlePropertyWidgets', 'GeomPrimSchemeDelegate', 'MaterialPrimSchemeDelegate', 'PathPrimSchemeDelegate', 'ShaderPrimSchemeDelegate', 'omni']
class BundlePropertyWidgets(omni.ext._extensions.IExt):
    """
    A class for registering and managing property widgets in an application.
    
        This class is designed to interface with the application's property window, registering various schemes and their corresponding delegates to handle different types of property widgets. It manages the lifecycle of these widgets by providing methods for their registration on startup and unregistration on shutdown. The class ensures that property widgets for geometry, materials, paths, shaders, physics, and animation graphs are made available within the application's user interface, allowing users to interact with different aspects of a scene or object properties.
        
    """
    def __init__(self):
        """
        Initializes the bundle property widgets.
        """
    def _register_widget(self):
        ...
    def _unregister_widget(self):
        ...
    def on_shutdown(self):
        """
        Called when the extension is shutting down.
        """
    def on_startup(self, ext_id):
        """
        Called when the extension is started up.
        
                Args:
                    ext_id (str): The ID of the extension being started.
        """
