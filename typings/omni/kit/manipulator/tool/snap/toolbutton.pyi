from __future__ import annotations
import omni as omni
from omni.kit.manipulator.tool.snap.models import SettingModel
from omni.kit.manipulator.transform.manipulator import TransformManipulator
from omni.kit.manipulator.transform.toolbar_tool import SimpleToolButton
from omni.kit.manipulator.transform.types import Operation
from omni import ui
from pathlib import Path
import typing
__all__ = ['Operation', 'Path', 'SettingModel', 'SimpleToolButton', 'SnapMenuDelegate', 'SnapToolButton', 'TransformManipulator', 'omni', 'ui']
class SnapMenuDelegate(omni.ui._ui.MenuDelegate):
    """
    A UI menu delegate for the snap functionality in a manipulator tool.
    
        This delegate provides custom styling for the snap menu used in conjunction with
        transform manipulators such as translate, rotate, and scale operations.
    """
    def get_style(self):
        """
        Returns the style configuration for the snap menu.
        
                Returns:
                    dict or style object: The style configuration for the snap menu.
        """
class SnapToolButton(omni.kit.manipulator.transform.toolbar_tool.SimpleToolButton):
    """
    A button for toggling snap functionality in transform manipulators.
    
        This class provides a UI component that allows users to enable or disable snapping when using translate, rotate, or scale manipulators. It interfaces with a SettingModel to persist the snapping state across sessions.
    
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments, among which 'operation' (Operation) is mandatory and specifies the manipulator operation type (translate, rotate, scale).
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @classmethod
    def can_build(cls, manipulator: omni.kit.manipulator.transform.manipulator.TransformManipulator, operation: omni.kit.manipulator.transform.types.Operation) -> bool:
        """
        Determines whether the snap tool button can be built for the given manipulator and operation.
        
                Args:
                    manipulator (TransformManipulator): The manipulator to check for compatibility with the snap tool.
                    operation (Operation): The operation type for which to check the possibility of building the snap tool.
        
                Returns:
                    bool: True if the snap tool button can be built for the given manipulator and operation, otherwise False.
        """
    def __init__(self, *args, **kwargs):
        """
        Initializes the snap tool button with the given operation.
        
                Args:
                    *args: Variable length argument list.
                    **kwargs: Arbitrary keyword arguments, among which 'operation' (Operation) is mandatory and specifies the manipulator operation type (translate, rotate, scale).
                
        """
    def destroy(self):
        """
        Cleans up the resources used by the SnapToolButton instance. Destroys the associated model if it exists.
        """
