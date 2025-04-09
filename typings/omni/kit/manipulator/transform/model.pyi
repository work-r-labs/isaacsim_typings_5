"""
Abstract transform manipulator model and manipulator operations
"""
from __future__ import annotations
from omni.kit.manipulator.transform.types import Operation
from omni.ui import scene as sc
import omni.ui_scene._scene
__all__ = ['AbstractTransformManipulatorModel', 'Operation', 'sc']
class AbstractTransformManipulatorModel(omni.ui_scene._scene.AbstractManipulatorModel):
    """
    An abstract base class for transform manipulator models.
    
        This class provides a common interface for manipulation operations such as translate, rotate, and scale. Models derived from this class are responsible for updating the manipulator's state and reflecting changes onto the underlying data.
    
        Args:
            **kwargs: Arbitrary keyword arguments that will be passed to AbstractTransformManipulatorModel.
    """
    class OperationItem(omni.ui_scene._scene.AbstractManipulatorItem):
        """
        A class representing an operation item for transform manipulators.
        
                Encapsulates an operation type to be used within transform manipulator models, such as translation, rotation, and scaling.
        
                Args:
                    operation: Operation
                        The specific transform operation this item represents.
        """
        def __init__(self, op: Operation):
            ...
        @property
        def operation(self):
            ...
    def __init__(self, **kwargs):
        """
        Initialize an abstract base class for transform manipulator models.
        """
    def get_as_floats(self, item: sc.AbstractManipulatorItem) -> list[int]:
        """
        
                Return the operation items as a list of ints. Called by manipulator to fetch item values.
        
                Args:
                    item (sc.AbstractManipulatorItem): input manipulator item.
        
                Returns:
                    List[int]: a composed Matrix4x4 transform in world space as a list of int.
                
        """
    def get_item(self, name: str) -> sc.AbstractManipulatorItem:
        """
        
                Return manipulator item by name. See AbstractManipulatorItem.get_item
        
                Args:
                    name: manipulator name.
        
                Returns:
                    sc.AbstractManipulatorItem: manipulator item matches the input name.
                
        """
    def get_operation(self) -> Operation:
        """
        
                Called by the manipulator to determine which operation is active.
        
                Returns:
                    Operation: The specific transform operation this item represents.
                
        """
    def get_snap(self, item: sc.AbstractManipulatorItem):
        """
        
                Called by the manipulator, returns the minimal increment step for each operation. None if no snap should be performed.
                Different Operation requires different return values:
                - TRANSLATE: Tuple[float, float, float]. One entry for X/Y/Z axis.
                - ROTATE: float. Angle in degree.
                - SCALE: float
        
                Args:
                    sc.AbstractManipulatorItem: input manipulator item.
                Returns:
                    None
                
        """
    def set_floats(self, item: sc.AbstractManipulatorItem, value: list[float]):
        """
        
                Called when the manipulator is being dragged and value changes, or set by external code to overwrite the value.
                The model should update value to underlying data holder(s) (e.g. a USD prim(s)).
        
                Depending on the model implemetation, item and value can be customized to model's needs.
        
                Args:
                    item (sc.AbstractManipulatorItem): input manipulator item.
                    value (List[float]): a composed Matrix4x4 transform in world space as a list of float.
                
        """
    def set_ints(self, item: sc.AbstractManipulatorItem, value: list[int]):
        """
        
                Called when the manipulator is being dragged and value changes, or set by external code to overwrite the value.
                The model should update value to underlying data holder(s) (e.g. a USD prim(s)).
        
                Depending on the model implemetation, item and value can be customized to model's needs.
        
                Args:
                    item (sc.AbstractManipulatorItem): input manipulator item.
                    value (List[float]): a composed Matrix4x4 transform in world space as a list of int.
                
        """
    def widget_disabled(self):
        """
        
                Called by hosting manipulator widget(s) when they're disabled.
                It can be used to track if any hosting manipulator is active to skip background model update (i.e. running listener for changes).
                
        """
    def widget_enabled(self):
        """
        
                Called by hosting manipulator widget(s) when they're enabled.
                It can be used to track if any hosting manipulator is active to skip background model update (i.e. running listener for changes).
                
        """
