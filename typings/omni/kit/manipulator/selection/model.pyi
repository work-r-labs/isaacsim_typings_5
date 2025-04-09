from __future__ import annotations
from omni.ui import scene as sc
import omni.ui_scene._scene
__all__ = ['SelectionShapeModel', 'sc']
class SelectionShapeModel(omni.ui_scene._scene.AbstractManipulatorModel):
    """
    A model to handle the selection region in a manipulator.
    
        This model manages the selection shapes such as rectangles and supports querying and
        setting their properties. It provides a way to interact with the selection shapes
        using named manipulator items and supports both integer and float values.
    
        Args:
            *args: Variable length argument list which will be forwarded to execute.
            **kwargs: Arbitrary keyword arguments that will be forwarded to execute.
        
    """
    def _SelectionShapeModel__validate_arguments(self, name: typing.Union[str, omni.ui_scene._scene.AbstractManipulatorItem], values: typing.Sequence[typing.Union[int, float]] = None) -> omni.ui_scene._scene.AbstractManipulatorItem:
        """
        Validates the arguments provided to other methods.
        
                Ensures that the provided name corresponds to a valid manipulator item
                and that the number of values matches the expected length.
        
                Args:
                    name (Union[str, sc.AbstractManipulatorItem]): The name of the item or the item itself.
                    values (Sequence[Union[int, float]], optional): A sequence of integers or floats to set for the item.
        
                Returns:
                    sc.AbstractManipulatorItem: The validated manipulator item.
        
                Raises:
                    KeyError: If the name is not recognized as an item.
                    ValueError: If the number of provided values does not match the expected length.
                
        """
    def __init__(self, *args, **kwargs):
        """
        Initializes the selection shape model with default values.
        
                This creates a set of manipulator items to store selection shape data.
        
                Args:
                    *args: Variable length argument list which will be forwarded to execute.
                    **kwargs: Arbitrary keyword arguments that will be forwarded to execute.
                
        """
    def get_as_floats(self, name: str) -> typing.List[float]:
        """
        Gets the value of the specified item as a sequence of floats.
        
                If the item is 'ndc_rect', computes the rectangle's coordinates from 'ndc_start' and 'ndc_current'.
        
                Args:
                    name (str): The name of the item to retrieve the value from.
        
                Returns:
                    List[float]: The values of the item as a list of floats, or the computed rectangle coordinates.
                
        """
    def get_as_ints(self, name: str) -> typing.List[int]:
        """
        Gets the value of the specified item as a sequence of integers.
        
                Args:
                    name (str): The name of the item to retrieve the value from.
        
                Returns:
                    List[int]: The values of the item as a list of integers.
                
        """
    def get_item(self, name: str) -> <omni.ui_scene._scene.AbstractManipulatorItem object>:
        """
        Retrieves the manipulator item associated with the given name.
        
                Args:
                    name (str): The name of the item to retrieve.
        
                Returns:
                    sc.AbstractManipulatorItem: The corresponding manipulator item.
                
        """
    def set_floats(self, name: str, values: typing.Sequence[int]):
        """
        Sets a sequence of floats for the specified item.
        
                Args:
                    name (str): The name of the item to update.
                    values (Sequence[int]): A sequence of floats to set for the item.
                
        """
    def set_ints(self, name: str, values: typing.Sequence[int]):
        """
        Sets a sequence of integers for the specified item.
        
                Args:
                    name (str): The name of the item to update.
                    values (Sequence[int]): A sequence of integers to set for the item.
                
        """
