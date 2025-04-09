"""
This module defines the ManipulatorPrim2Core class that initializes and manages core components for manipulator primitives in a 3D application, setting up registries and tools for viewport manipulators.
"""
from __future__ import annotations
import omni as omni
from omni.kit.manipulator.prim.core.global_registry import clean_prim_data_accessor_registry
from omni.kit.manipulator.prim.core.global_registry import get_prim_data_accessor_registry
from omni.kit.manipulator.prim.core.global_registry import set_prim_data_accessor_registry
from omni.kit.manipulator.prim.core.prim_data_accessor_registry import PrimDataAccessorRegistry
from omni.kit.manipulator.prim.core.prim_transform_manipulator import PrimTransformManipulator
from omni.kit.manipulator.prim.core.prim_transform_manipulator_registry import TransformManipulatorRegistry
from omni.kit.manipulator.prim.core.reference_prim_marker import ReferencePrimMarker
from omni.kit.manipulator.prim.core.tools import PrimManipTools
__all__ = ['ManipulatorPrim2Core', 'PrimDataAccessorRegistry', 'PrimManipTools', 'PrimTransformManipulator', 'ReferencePrimMarker', 'TransformManipulatorRegistry', 'clean_prim_data_accessor_registry', 'get_prim_data_accessor_registry', 'omni', 'set_prim_data_accessor_registry']
class ManipulatorPrim2Core(omni.ext._extensions.IExt):
    """
    A class responsible for initializing and managing core components for manipulator primitives in a 3D application.
    
        This extension class sets up the necessary registries and tools used for handling manipulator primitives. It creates a legacy manipulator for viewport 1 (VP1) and a manipulator registry for viewport 2 (VP2). It also handles the creation of a marker to reference primitives within the scene. Upon shutdown, it ensures that all created components are properly destroyed and the global registry is cleaned up.
        
    """
    def on_shutdown(self):
        """
        Cleans up all manipulator systems and tools upon shutdown.
        """
    def on_startup(self, ext_id):
        """
        Initializes the core manipulator systems and tools.
        
                Args:
                    ext_id (str): External ID provided during startup.
        """
