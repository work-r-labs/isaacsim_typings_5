"""
This module provides a registry for managing PrimTransformManipulatorScene instances, handling their lifecycle within a scene.
"""
from __future__ import annotations
from omni.kit.manipulator.prim.core.prim_transform_manipulator import PrimTransformManipulator
from omni.kit.manipulator.prim.core.reference_prim_marker import ReferencePrimMarker
import weakref as weakref
__all__: list = ['TransformManipulatorRegistry']
class PrimTransformManipulatorScene:
    visible = ...
    def __init__(self, desc: dict):
        ...
    def destroy(self):
        ...
    @property
    def categories(self):
        ...
    @property
    def name(self):
        ...
class TransformManipulatorRegistry:
    """
    A registry for managing instances of :obj:`PrimTransformManipulatorScene` within a scene.
    
        This class is responsible for the lifecycle management of the :obj:`PrimTransformManipulatorScene` instances. It registers the :obj:`PrimTransformManipulatorScene` with the scene, ensuring that manipulators for transforming primitives are properly managed and destroyed when no longer needed.
        
    """
    def __del__(self):
        ...
    def __init__(self):
        """
        Initializes the TransformManipulatorRegistry instance.
        """
    def destroy(self):
        """
        Cleans up resources used by the TransformManipulatorRegistry instance.
        """
