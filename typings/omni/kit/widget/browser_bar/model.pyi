"""
This module provides the implementation for a string queue model and a visited history tracking system, designed to manage and interact with collections of strings representing items and a history of visited items respectively.
"""
from __future__ import annotations
from omni import ui
import omni.ui._ui
import os as os
import sys as sys
__all__ = ['StringQueueItem', 'StringQueueModel', 'VisitedHistory', 'os', 'sys', 'ui']
class StringQueueItem(omni.ui._ui.AbstractItem):
    """
    A class representing an item in a string queue.
    
        This class encapsulates a string value as part of a queue, providing a simple interface to access the string value. It is designed to be used within a queue structure that manages multiple instances of `StringQueueItem`s, allowing for operations such as enqueueing and dequeueing of string values.
    
        Args:
            value (str): The string value to be encapsulated by the `StringQueueItem`.
    """
    def __init__(self, value: str):
        """
        Initializes a new instance of StringQueueItem.
        """
    @property
    def model(self):
        """
        Gets the model associated with this StringQueueItem.
        
                Returns:
                    :obj:`ui.SimpleStringModel`: The model of the item.
        """
    @property
    def value(self):
        """
        Gets the value of the StringQueueItem as a string.
        
                Returns:
                    str: The value of the item.
        """
class StringQueueModel(omni.ui._ui.AbstractItemModel):
    """
    A class that manages a queue of string items with a maximum size.
    
        This model is designed to handle a collection of StringQueueItem objects,
        providing methods to enqueue new items, dequeue the oldest item,
        and to access items based on index or value.
        It also maintains the selection state of items in the queue.
    
        Args:
            max_items (int): The maximum number of items allowed in the queue. Defaults to 4.
            value_changed_fn (Optional[Callable[[ui.AbstractValueModel], None]]):
                                A callback function that gets called when the selected index changes.
        
    """
    def __getitem__(self, idx: int) -> StringQueueItem:
        ...
    def __init__(self, max_items: int = 4, value_changed_fn = None):
        """
        Initializes the StringQueueModel with optional max items and a value changed callback.
        """
    def _on_selection_changed(self, model: omni.ui._ui.AbstractValueModel):
        ...
    def dequeue(self):
        """
        Dequeues the last item from the queue.
        """
    def destroy(self):
        """
        Destroys the queue, clearing all items and selected index.
        """
    def enqueue(self, value: str):
        """
        Enqueues a new value to the queue.
        
                Args:
                    value (str): The value to enqueue.
        """
    def find_item(self, value: str) -> StringQueueItem:
        """
        Finds an item by its value.
        
                Args:
                    value (str): The value to search for.
        
                Returns:
                    :obj:`StringQueueItem`: The found item, or None if not found.
        """
    def get_item_children(self, item) -> [StringQueueItem]:
        """
        Gets the children of a specified item.
        
                Args:
                    item (:obj:`StringQueueItem`): The item to get children for.
        
                Returns:
                    List[:obj:`StringQueueItem`]: List of child items.
        """
    def get_item_value_model(self, item, column_id) -> omni.ui._ui.AbstractValueModel:
        """
        Gets the value model for an item and column.
        
                Args:
                    item (:obj:`StringQueueItem`): The item to get the model for.
                    column_id (int): The ID of the column.
        
                Returns:
                    :obj:`ui.AbstractValueModel`: The value model for the specified item and column.
        """
    def get_selected_item(self) -> StringQueueItem:
        """
        Retrieves the currently selected item.
        
                Returns:
                    :obj:`StringQueueItem`: The selected item if any, None otherwise.
        """
    def peek(self) -> StringQueueItem:
        """
        Peeks at the first item in the queue without removing it.
        
                Returns:
                    :obj:`StringQueueItem`: The first item if the queue is not empty, None otherwise.
        """
    def size(self) -> int:
        """
        Returns the number of items in the queue.
        
                Returns:
                    int: The size of the queue.
        """
    @property
    def selected_index(self) -> int:
        """
        Gets the currently selected index.
        
                Returns:
                    int: The current selected index.
        """
    @selected_index.setter
    def selected_index(self, index: int):
        """
        Sets the selected index.
        
                Args:
                    index (int): The new index to set as selected.
        """
class VisitedHistory:
    """
    A class for maintaining a history of visited items.
    
        This class is designed to keep track of a list of items (e.g., URLs, file paths) that have been visited, allowing for easy access to recently visited items. It supports operations such as insertion and retrieval of items, enabling or disabling the history tracking, and managing the maximum number of items to retain in history.
    
        Args:
            max_items (int, optional): The maximum number of items to retain in the visited history. Defaults to 100.
    """
    def __getitem__(self, idx: int) -> str:
        ...
    def __init__(self, max_items: int = 100):
        """
        Initializes the VisitedHistory object.
        """
    def activate(self):
        """
        Activates the history tracking.
        """
    def deactivate(self):
        """
        Deactivates the history tracking.
        """
    def destroy(self):
        """
        Destroys the visited history, clearing all items.
        """
    def get_selected_item(self) -> str:
        """
        Retrieves the currently selected item from history.
        
                Returns:
                    str: The selected item or None if not selected.
        """
    def insert(self, value: str):
        """
        Inserts a new value into the visited history.
        
                Args:
                    value (str): The value to insert.
        """
    def pop(self):
        """
        Pops the last item from the visited history.
        """
    def size(self) -> int:
        """
        Returns the size of the visited history.
        
                Returns:
                    int: The number of items in the history.
        """
    @property
    def selected_index(self) -> int:
        """
        Gets the currently selected index.
        
                Returns:
                    int: The current selected index.
        """
    @selected_index.setter
    def selected_index(self, index: int):
        """
        Sets the currently selected index.
        
                Args:
                    index (int): The new index to set as selected.
        """
