"""
This module provides a UI for managing extension registries, allowing users to add, remove, or set a registry as default, and features editing capabilities for registry entries.
"""
from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.window.extensions.common import get_registries
from omni.kit.window.extensions.ext_components import SimpleCheckBox
from omni.kit.window.extensions.styles import get_style
from omni.kit.window.extensions.utils import copy_text
from omni.kit.window.extensions.utils import get_setting
from omni import ui
__all__: list = ['RegistryItem', 'RegistriesModel', 'EditableDelegate', 'ExtsRegistriesWidget']
class EditableDelegate(omni.ui._ui.AbstractItemDelegate):
    """
    A delegate class that provides an editable interface for registry items.
    
        This delegate is used to create interactive UI elements for each registry item in a TreeView. It supports editing of the item's name and URL, copying the item's text with a context menu, and handling user interactions such as double-clicking to edit and confirming edits. It also includes visual cues to distinguish between user-defined and built-in registry items.
        
    """
    def __init__(self):
        """
        Initialize the EditableDelegate with default values and a context menu.
        """
    def _show_copy_context_menu(self, x, y, button, modifier, text):
        ...
    def build_header(self, column_id):
        """
        Builds the header for a specified column in the tree view.
        
                Args:
                    column_id (int): Identifier for the column header to build.
        """
    def build_widget(self, model, item, column_id, level, expanded):
        """
        Create a widget per column per item
        
                Args:
                    model (:obj:`ui.AbstractItemModel`): The model that holds the data.
                    item (:obj:`ui.AbstractItem`): The item for which to build the widget.
                    column_id (int): Identifier for the column in which the widget will be placed.
                    level (int): The indentation level of the item in the tree structure.
                    expanded (bool): Indicates if the item's children are expanded.
        """
    def destroy(self):
        """
        Cleans up the delegate by clearing subscriptions and context menus.
        """
    def on_double_click(self, button, field, label, model, item):
        """
        Called when the user double-clicked the item in TreeView
        
                Args:
                    button (int): The mouse button that was pressed.
                    field (:obj:`ui.StringField`): The string field that is double-clicked.
                    label (:obj:`ui.Label`): The label of the item where the double click occurred.
                    model (:obj:`ui.AbstractItemModel`): The model containing the item.
                    item (:obj:`ui.AbstractItem`): The item that was double-clicked.
        """
    def on_end_edit(self, text, field, label, model):
        """
        Called when the user is editing the item and pressed Enter or clicked outside of the item
        
                Args:
                    text (str): The text entered by the user.
                    field (:obj:`ui.StringField`): The string field that was being edited.
                    label (:obj:`ui.Label`): The label of the item that was edited.
                    model (:obj:`ui.AbstractItemModel`): The model containing the item.
        """
class ExtsRegistriesWidget:
    """
    A widget for managing extension registries in a UI environment.
    
        This widget uses a tree view to list and edit registry entries, allowing users to add, remove, or set a registry as default. It features a scrolling frame for easy navigation of registry items and supports context menus for copy actions. The widget is styled according to the application's theme and is intended for use within a larger application framework.
        
    """
    def __init__(self):
        """
        Initialize the ExtsRegistriesWidget with a model and a delegate to manage registries.
        """
    def destroy(self):
        """
        Cleans up the model and delegate resources associated with the ExtsRegistriesWidget.
        """
class RegistriesModel(omni.ui._ui.AbstractItemModel):
    """
    A model representing a collection of registry items for an application.
    
        This class maintains a list of registry items, each represented by a `RegistryItem` instance. It provides methods to load registry data, add or remove registry items, save changes, and set a default registry.
    
        The class uses an internal model to manage the state of each registry item and to interact with the UI for displaying and editing registries. It also handles notifications for registry changes and ensures that registry updates are saved to the application settings.
    
        The model is used in conjunction with a UI tree view to enable users to view and modify the list of registries in a structured fashion.
        
    """
    def __init__(self):
        """
        Initializes the model for the registries view.
        """
    def _load(self):
        ...
    def add_empty(self):
        """
        Adds a new empty item to the model.
        """
    def destroy(self):
        """
        Clears all children items from the model.
        """
    def get_item_children(self, item):
        """
        Retrieves the child items of a given item.
        
                Args:
                    item (:obj:`ui.AbstractItem`): The parent item whose children are to be retrieved.
        
                Returns:
                    list: A list of child items.
        """
    def get_item_value_model(self, item, column_id):
        """
        Gets the value model for a given item and column.
        
                Args:
                    item (:obj:`ui.AbstractItem`): The item to get the value model for.
                    column_id (int): The ID of the column.
        
                Returns:
                    :obj:`ui.SimpleStringModel` or None: The value model for the specified item and column.
        """
    def get_item_value_model_count(self, item):
        """
        Returns the number of columns for the item's value model.
        
                Args:
                    item (:obj:`ui.AbstractItem`): The item to get the value model count for.
        
                Returns:
                    int: The number of value model columns.
        """
    def remove_item(self, item):
        """
        Removes a specified item from the model and saves the change.
        
                Args:
                    item (:obj:`ui.AbstractItem`): The item to be removed.
        """
    def save(self):
        """
        Saves the current state of the model's registries to settings.
        """
    def set_default(self, item, value):
        """
        Sets a specified item as the default registry.
        
                Args:
                    item (:obj:`ui.AbstractItem`): The item to set as default or not.
                    value (bool): Whether to set or unset the item as default.
        """
class RegistryItem(omni.ui._ui.AbstractItem):
    """
    A class representing an individual registry item in the application.
    
        This class encapsulates the details of a registry entry, which includes its name, URL, and flags to indicate if it's a user-defined registry or a default one. It also supports adding a dummy entry.
    
        Args:
            name (str): The name of the registry item.
            url (str): The URL associated with the registry item.
            is_user (bool): Flag indicating if the item is user-defined.
            is_default (bool): Flag indicating if the item is set as default.
            add_dummy (bool): Flag indicating if a dummy item should be added.
    """
    def __init__(self, name, url, is_user = True, is_default = False, add_dummy = False):
        """
        Initializes a new instance of the RegistryItem with the provided name, URL, and status flags.
        """
DEFAUT_PUBLISH_SETTING: str = 'app/extensions/registryPublishDefault'
EMPTY_REGISTRY_NAME: str = '[enter_name]'
REGISTRIES_CHANGED_EVENT: int = 17790543992418514273
REGISTRIES_COLUMNS: list = ['name', 'url', 'default', 'user']
USER_REGISTRIES_SETTING: str = '/persistent/exts/omni.kit.registry.nucleus/userRegistries'
