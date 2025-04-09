from __future__ import annotations
import carb as carb
import math as math
import omni.kit.manipulator.transform.gestures
from omni.kit.manipulator.transform.gestures import RotateChangedGesture
from omni.kit.manipulator.transform.gestures import RotateDragGesturePayload
from omni.kit.manipulator.transform.gestures import ScaleChangedGesture
from omni.kit.manipulator.transform.gestures import ScaleDragGesturePayload
from omni.kit.manipulator.transform.gestures import TransformDragGesturePayload
from omni.kit.manipulator.transform.gestures import TranslateChangedGesture
from omni.kit.manipulator.transform.gestures import TranslateDragGesturePayload
import omni.kit.manipulator.transform.model
from omni.kit.manipulator.transform.model import AbstractTransformManipulatorModel
from omni.kit.manipulator.transform.types import Operation
from omni.ui import scene as sc
__all__ = ['AbstractTransformManipulatorModel', 'Operation', 'RotateChangedGesture', 'RotateDragGesturePayload', 'ScaleChangedGesture', 'ScaleDragGesturePayload', 'SimpleRotateChangedGesture', 'SimpleScaleChangedGesture', 'SimpleTransformModel', 'SimpleTranslateChangedGesture', 'TransformDragGesturePayload', 'TranslateChangedGesture', 'TranslateDragGesturePayload', 'carb', 'math', 'sc']
class SimpleRotateChangedGesture(omni.kit.manipulator.transform.gestures.RotateChangedGesture):
    """
    Handles the rotation changes for a transform manipulator gesture.
    
        This gesture class responds to changes in rotation during a rotation operation. It updates the rotation matrix of the manipulated object based on the axis and angle provided by the rotation gesture payload.
        
    """
    def on_began(self):
        """
        Called when the gesture begins.
        
                Initializes the rotation matrix of the manipulated object using the current rotation values.
        """
    def on_changed(self):
        """
        Called when the rotation gesture is updated.
        
                Applies the rotation changes based on the axis and angle provided by the gesture payload. Updates the model's rotation data by applying the rotation to the starting rotation matrix. The rotation is computed by constructing a rotation matrix around the axis for the given angle in radians, then multiplying it by the initial rotation matrix. The result is decomposed back into Euler angles in degrees and set on the model.
                
        """
class SimpleScaleChangedGesture(omni.kit.manipulator.transform.gestures.ScaleChangedGesture):
    """
    A gesture class that responds to scale changes during a transform manipulator operation.
    
        This class processes scale gestures and updates the model's scale data accordingly. It listens for scale gestures and applies the scale factor to the current scale of the object being manipulated.
        
    """
    def on_began(self):
        """
        Called when the scale gesture begins.
        
                Initializes the _begin_scale attribute with the current scale values of the item being manipulated.
        """
    def on_changed(self):
        """
        Called when the scale gesture is updated.
        
                Applies a scale delta to the initial scale values and updates the model with the new scale. It multiplies the initial scale by the scale factor provided in the gesture payload for each axis.
        
                Args:
                    gesture_payload (ScaleDragGesturePayload): The payload containing the scale factor and axis information.
                    sender (AbstractTransformManipulatorModel): The model associated with the gesture.
        """
class SimpleTransformModel(omni.kit.manipulator.transform.model.AbstractTransformManipulatorModel):
    """
    A model for basic S/R/T (Scale/Rotate/Translate) transform manipulations in a 3D scene. It allows subscribing to callbacks for updates on manipulated data. Rotation operations are applied in XYZ order and values are in degrees.
        
    """
    def __init__(self):
        ...
    def get_as_floats(self, item: AbstractTransformManipulatorModel.OperationItem) -> list[float]:
        """
        Retrieves the transformation values as a list of floats for a given component.
        
                If the transformation matrix is marked as dirty and the requested item is the transform_item, it recalculates the transformation matrix before returning it.
        
                Args:
                    item (AbstractTransformManipulatorModel.OperationItem): The component to retrieve (translate_item, rotate_item, scale_item, transform_item).
        
                Returns:
                    List[float]: The transformation values for the requested component or the transformation matrix if transform_item is requested.
                
        """
    def get_operation(self) -> Operation:
        """
        Retrieves the current operation mode of the transform manipulator.
        
                Returns:
                    Operation: The current operation mode (Translate, Rotate, Scale).
        """
    def set_floats(self, item: AbstractTransformManipulatorModel.OperationItem, value: list[float]):
        """
        Updates the transformation values for a given transformation component (translation, rotation, or scale).
        
                Sets the corresponding transformation component values to the provided list of floats and marks the transformation as dirty.
        
                Args:
                    item (AbstractTransformManipulatorModel.OperationItem): The component to update (translate_item, rotate_item, or scale_item).
                    value (List[float]): The new values for the component.
        """
    def set_operation(self, op: Operation):
        """
        Sets the current operation mode of the transform manipulator.
        
                If the operation mode is different from the current mode, it sets the new mode and notifies any subscribers that the transform item has changed.
        
                Args:
                    op (Operation): The new operation mode to set.
        """
    @property
    def global_mode(self) -> bool:
        """
        
                Get whether it is global mode.
        
                Returns:
                    bool: whether it is global mode.
                
        """
    @global_mode.setter
    def global_mode(self, value: bool):
        """
        
                Set whether it is global mode.
        
                Args:
                    value (bool): whether it is global mode.
                
        """
class SimpleTranslateChangedGesture(omni.kit.manipulator.transform.gestures.TranslateChangedGesture):
    """
    A gesture that handles the change in translation during a translate operation.
    
        This class processes the translation changes when a TranslateDragGesturePayload is received. It updates the model's translation data based on the moved delta of the payload.
        
    """
    def on_changed(self):
        """
        Handles the update of the translation during a translate gesture.
        
                This method processes the translation changes when a TranslateDragGesturePayload is received. It updates the
                model's translation data by adding the moved delta of the payload to the current translation.
        """
