"""
Contains the class of UsdLayerUndo and UsdEditTargetUndo
"""
from __future__ import annotations
import pxr.Sdf
from pxr import Sdf
import pxr.Usd
from pxr import Usd
__all__ = ['Sdf', 'Usd', 'UsdEditTargetUndo', 'UsdLayerUndo']
class UsdEditTargetUndo(UsdLayerUndo):
    """
    A class for managing undo operations on a USD edit target.
    
        This class provides methods to reserve and undo changes made to a USD layer through an edit target.
    
        Args:
            edit_target: Usd.EditTarget
                The edit target to be managed for undo operations.
    """
    def __init__(self, edit_target: pxr.Usd.EditTarget):
        """
        Initializes a UsdEditTargetUndo instance with the given edit target.
        
                Args:
                    edit_target (Usd.EditTarget): The edit target to be managed for undo operations.
        """
    def reserve(self, path: pxr.Sdf.Path, info = None):
        """
        Reserves the specified path and info for undo, mapped to the edit target's namespace.
        
                Args:
                    path (Sdf.Path): The path to be reserved.
                    info (str, optional): The info key to be reserved. If None, the entire spec is reserved.
        """
class UsdLayerUndo:
    """
    A class for managing undo operations on USD layers.
    
        This class encapsulates the functionality to reserve changes, perform undo operations, and reset the undo stack for a USD layer. It is designed to work with Sdf.Layer objects, allowing for precise control over the changes made to the layer.
    
        Args:
            layer: Sdf.Layer
                The Sdf.Layer object on which the undo operations are performed.
    """
    class Key:
        """
        A class to represent a key in the undo system for USD layers.
        
                Args:
                    path: Sdf.Path
                        The path associated with the change to be undone.
                    info: Any
                        Optional information associated with the path, such as a specific attribute or metadata key.
        """
        def __init__(self, path, info):
            ...
    def __init__(self, layer: pxr.Sdf.Layer):
        """
        Initializes the UsdLayerUndo instance.
        
                Args:
                    layer (Sdf.Layer): The USD layer to be managed by this undo instance.
        """
    def reserve(self, path: pxr.Sdf.Path, info = None):
        """
        Reserves the changes made to the path in the USD layer to allow undo operations.
        
                Args:
                    path (Sdf.Path): The path in the USD layer to reserve.
                    info (optional): Additional information about the reservation, default is None.
        """
    def reset(self):
        """
        Resets the internal state of the UsdLayerUndo instance, clearing any changes reserved.
        """
    def undo(self):
        """
        Undoes the last set of changes reserved by the reserve method.
        
                Raises:
                    Exception: If the layer cannot be found.
        """
