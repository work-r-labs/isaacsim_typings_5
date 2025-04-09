from __future__ import annotations
import carb as carb
from omni.kit.manipulator.selection.model import SelectionShapeModel
from omni.ui import scene as sc
import omni.ui_scene._scene
import typing
import weakref as weakref
__all__: list = ['SelectionManipulator', 'SelectionMode']
class SelectionManipulator(omni.ui_scene._scene.Manipulator):
    """
    A manipulator for selecting objects within a scene.
    
        This manipulator allows users to select objects using various gestures, such as dragging for rectangle selection or clicking for single object selection. It can be styled with custom colors and thickness for the selection rectangle.
    
        Args:
            style (dict, optional): A dictionary with custom style attributes. Defaults to None.
            *args: Variable length argument list which will be forwarded to execute.
            **kwargs: Arbitrary keyword arguments that will be forwarded to execute.
    
        Attributes:
            model: SelectionShapeModel
                The model associated with the selection manipulator.
            gestures: list
                A list of gesture recognizers associated with the manipulator.
    """
    def _SelectionManipulator__draw_shape(self, start, end, as_rect):
        """
        Draws the selection shape on the screen.
        
                Args:
                    start (Tuple[float, float, float]): The starting point of the selection shape in OBJECT space.
                    end (Tuple[float, float, float]): The ending point of the selection shape in OBJECT space.
                    as_rect (bool): Determines if the selection shape should be drawn as a rectangle or a polygon.
                
        """
    def __init__(self, style: dict = None, *args, **kwargs):
        """
        Initializes a selection manipulator with optional custom styling.
        
                Args:
                    style (dict, optional): A dictionary with custom style attributes. Defaults to None.
                    *args: Variable length argument list which will be forwarded to execute.
                    **kwargs: Arbitrary keyword arguments that will be forwarded to execute.
                
        """
    def on_build(self):
        """
        Builds the selection manipulator's UI elements.
        """
    def on_model_updated(self, item):
        """
        Updates the selection manipulator when the model changes.
        
                Args:
                    item: The item in the model that was updated.
                
        """
class SelectionMode:
    """
    An enumeration for different selection modes in a manipulator.
    """
    APPEND: typing.ClassVar[int] = 1
    REMOVE: typing.ClassVar[int] = 2
    REPLACE: typing.ClassVar[int] = 0
class _ClickGesture(omni.ui_scene._scene.ClickGesture):
    def __init__(self, manipulator: omni.ui_scene._scene.Manipulator, *args, **kwargs):
        ...
    def on_ended(self):
        ...
class _DragGesture(omni.ui_scene._scene.DragGesture):
    def __init__(self, manipulator: omni.ui_scene._scene.Manipulator, *args, **kwargs):
        ...
    def on_began(self):
        ...
    def on_changed(self):
        ...
    def on_ended(self):
        ...
class _ModifierDown:
    def __init__(self):
        ...
    def test(self, modifiers: int):
        ...
class _SelectionGesture:
    def _SelectionGesture__get_selection_mode(self):
        ...
    def _on_ended(self, manipulator: omni.ui_scene._scene.Manipulator):
        ...
    def _set_mouse(self, model: omni.ui_scene._scene.AbstractManipulatorModel, ndc_mouse: typing.List[float], is_start: bool = False):
        ...
class _SelectionPreventer(omni.ui_scene._scene.GestureManager):
    """
    Class to explicitly block selection in favor of alt-orbit when alt-dragging
    """
    @staticmethod
    def _SelectionPreventer__check_alt_modifier(gesture):
        ...
    def can_be_prevented(self, gesture):
        ...
    def should_prevent(self, gesture, preventer):
        ...
def _optional_bool(model: omni.ui_scene._scene.AbstractManipulatorModel, item: str, default_value: bool = False):
    ...
