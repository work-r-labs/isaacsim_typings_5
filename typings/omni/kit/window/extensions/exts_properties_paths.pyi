"""
This module provides a UI for managing extension paths with functionalities to add, remove, clean cache, and update Git-managed paths.
"""
from __future__ import annotations
import omni as omni
from omni.kit.window.extensions.styles import get_style
from omni.kit.window.extensions.utils import cleanup_folder
from omni.kit.window.extensions.utils import copy_text
from omni.kit.window.extensions.utils import get_extpath_git_ext
from omni import ui
__all__: list = ['PathItem', 'PathsModel', 'EditableDelegate', 'ExtsPathsWidget']
class EditableDelegate(omni.ui._ui.AbstractItemDelegate):
    """
    A delegate class for handling editable UI elements within a tree view structure.
    
        This delegate is responsible for managing interactive UI components such as buttons and text fields within a tree view. It enables actions such as opening file paths in the OS file explorer, editing item names directly within the UI, and triggering context menus for additional options like copying text. It also supports special functionalities for user-defined paths, cache management, and git repository updates.
    
        The delegate utilizes a context menu for copy actions and dynamically updates the UI based on user interactions, such as double-clicking to edit names or clicking buttons to add, remove, or clean items. It plays a crucial role in managing the appearance and functionality of editable items within the tree view, ensuring a responsive and intuitive user experience.
        
    """
    def __init__(self):
        """
        Initializes the EditableDelegate instance.
        """
    def _show_copy_context_menu(self, x, y, button, modifier, text):
        ...
    def build_header(self, column_id):
        """
        Builds the header for a specified column in the tree view.
        
                Args:
                    column_id (int): The column index for which to build the header.
        """
    def build_widget(self, model, item, column_id, level, expanded):
        """
        Create a widget per column per item
        
                Args:
                    model (:obj:`ui.AbstractItemModel`): The model associated with the tree view.
                    item (:obj:`ui.AbstractItem`): The item in the model for which to build the widget.
                    column_id (int): The column index where the widget will be placed.
                    level (int): The level of indentation for the item in the tree view.
                    expanded (bool): Whether the item's children are currently expanded.
        """
    def destroy(self):
        """
        Cleans up resources and references held by the delegate instance.
        """
    def on_double_click(self, button, field, label, model, item):
        """
        Called when the user double-clicked the item in TreeView
        
                Args:
                    button (int): The mouse button clicked (0 for left-click).
                    field (:obj:`ui.StringField`): The field to be edited on double-click.
                    label (:obj:`ui.Label`): The label associated with the item.
                    model (:obj:`ui.AbstractItemModel`): The model associated with the tree view.
                    item (:obj:`ui.AbstractItem`): The item that was double-clicked.
        """
    def on_end_edit(self, text, field, label, model):
        """
        Called when the user is editing the item and pressed Enter or clicked outside of the item
        
                Args:
                    text (str): The new text entered into the field.
                    field (:obj:`ui.StringField`): The text field that was being edited.
                    label (:obj:`ui.Label`): The label associated with the item.
                    model (:obj:`ui.AbstractItemModel`): The model to update with new text.
        """
class ExtsPathsWidget:
    """
    A widget that displays and manages paths related to extension directories.
    
        This widget uses a tree view to list and edit extension paths. It allows users to open paths in the OS file explorer, copy paths to the clipboard, add new path entries, remove existing ones, clean cache directories, and update Git-managed paths. Changes to paths are saved persistently. The widget supports different path types, each with its own label and color coding.
        
    """
    def __init__(self):
        """
        Initializes the ExtsPathsWidget with a model and delegate, and creates the UI components.
        """
    def destroy(self):
        """
        Cleans up the resources used by the ExtsPathsWidget.
        """
class PathItem(omni.ui._ui.AbstractItem):
    """
    A class representing a path item in a filesystem-like structure.
    
        This class encapsulates information about a path, including its type and whether it should be accompanied by a dummy element. It's used to model a single entry in a hierarchical file path representation.
    
        Args:
            path (str): The filesystem path represented by the item.
            path_type (:obj:`omni.ext.ExtensionPathType`): The type of path based on predefined constants.
            add_dummy (bool): Flag to indicate whether a dummy placeholder should be added.
    """
    def __init__(self, path, path_type: omni.ext._extensions.ExtensionPathType, add_dummy = False):
        """
        Initializes a new instance of PathItem with the provided path, path type, and an optional dummy flag.
        """
class PathsModel(omni.ui._ui.AbstractItemModel):
    """
    A model for managing and interacting with filesystem paths within a user interface.
    
        This model is designed to work with a UI framework to display and manipulate paths related to extensions and their respective types, such as collections, user directories, cache directories, and direct paths. It supports operations like adding new paths, removing existing ones, cleaning cache directories, and updating git repositories. The model holds a list of path items and provides methods to perform actions on these items.
        
    """
    def __init__(self):
        """
        Initializes the model for managing paths in the application.
        """
    def _load(self):
        ...
    def add_empty(self):
        """
        Adds an empty path item to the model.
        """
    def clean_cache(self, item):
        """
        Cleans the cache for a specified item.
        
                Args:
                    item: The item whose cache to clean.
        """
    def destroy(self):
        """
        Clears all the children from the model.
        """
    def get_item_children(self, item):
        """
        Returns all the children for the given item.
        
                Args:
                    item: The item to retrieve children for.
        """
    def get_item_value_model(self, item, column_id):
        """
        Retrieves the value model for a given item and column.
        
                Args:
                    item: The item to retrieve the value model for.
                    column_id: The column ID for which to retrieve the value model.
        """
    def get_item_value_model_count(self, item):
        """
        Returns the number of columns in the model.
        
                Args:
                    item: The item for which to count the value models.
        """
    def remove_item(self, item):
        """
        Removes a specified item from the model.
        
                Args:
                    item: The item to be removed.
        """
    def save(self):
        """
        Saves the current paths to the extension manager.
        """
    def update_git(self, item):
        """
        Updates the GIT path for a specified item.
        
                Args:
                    item: The item whose GIT path to update.
        """
PATHS_COLUMNS: list = ['', 'name', 'type', 'edit']
PATH_TYPE_TO_COLOR: dict  # value = {<ExtensionPathType.COLLECTION: 0>: 4280920489, <ExtensionPathType.COLLECTION_USER: 3>: 4279863721, <ExtensionPathType.COLLECTION_CACHE: 4>: 4289308969, <ExtensionPathType.DIRECT_PATH: 1>: 4280920361, <ExtensionPathType.EXT_1_FOLDER: 2>: 4280887721}
PATH_TYPE_TO_LABEL: dict  # value = {<ExtensionPathType.COLLECTION: 0>: '[dir]', <ExtensionPathType.COLLECTION_USER: 3>: '[user dir]', <ExtensionPathType.COLLECTION_CACHE: 4>: '[cache dir]', <ExtensionPathType.DIRECT_PATH: 1>: '[ext]', <ExtensionPathType.EXT_1_FOLDER: 2>: '[exts 1.0]'}
