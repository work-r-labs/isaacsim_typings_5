"""
This module provides a model to manage batch positions for items, supporting operations like multiselection, backdrop, and upstream positioning within a graphical interface.
"""
from __future__ import annotations
from omni.kit.widget.graph.abstract_batch_position_getter import AbstractBatchPositionGetter
import weakref as weakref
__all__: list = ['GraphModelBatchPositionHelper']
class GraphModelBatchPositionHelper:
    """
    A helper class for managing batch positions of graph items.
    
        This class is responsible for handling operations related to the positioning of multiple items as a batch within a
        graph interface. It supports functionalities such as multiselection, backdrop management, and positioning of upstream
        items. This class ensures that position-related actions are synchronized across all selected items, providing a
        consistent and expected behavior during user interactions such as dragging and editing the position of graph nodes.
        
    """
    def __init__(self):
        """
        Initializes the GraphModelBatchPositionHelper with default properties.
        """
    def _remove_get_moving_items_fn(self, id: int):
        ...
    def add_get_moving_items_fn(self, fn: typing.Callable[[typing.Any], typing.List[typing.Any]]):
        """
        Add the function that is called in batch_position_begin_edit to determine which items to move
        
                Args:
                    fn: A callable that takes a single argument and returns a list of items to be moved.
        """
    def batch_position_begin_edit(self, item: typing.Any):
        """
        Begins a batch editing process, determining and preparing items for movement.
        
                Should be called from position_begin_edit to make sure position_begin_edit is called for all the selected nodes
        
                Args:
                    item: The item for which the batch position editing is initiated.
        """
    def batch_position_end_edit(self, item: typing.Any):
        """
        Completes the batch editing process, finalizing the movement of items.
        
                Should be called from position_begin_edit to make sure position_begin_edit is called for all the selected nodes
        
                Args:
                    item: The item for which the batch position editing is being completed.
        """
    def batch_set_position(self, position: typing.List[float], item: typing.Any = None):
        """
        Sets the position for all selected nodes.
        
                Should be called in the position setter to make sure the position setter is called for all the selected nodes.
        
                Args:
                    position: The list of float values representing the new position.
                    item: The item that is currently driving the position change, if any. Defaults to None.
        """
    @property
    def batch_proxy(self):
        """
        Gets the batch proxy which is used for converting calls to input/output nodes.
        
                Returns:
                    The batch proxy object.
        """
    @batch_proxy.setter
    def batch_proxy(self, value):
        """
        Sets a new batch proxy with weak reference to avoid circular references.
        
                Args:
                    value: The new value for the batch proxy.
        """
