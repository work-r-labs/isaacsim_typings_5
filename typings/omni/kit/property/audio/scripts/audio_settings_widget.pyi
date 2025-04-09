"""
A module providing a widget to manage audio settings for USD scenes within the Omniverse Kit.
"""
from __future__ import annotations
import omni as omni
from omni.kit.property.usd.usd_property_widget_builder import UsdPropertiesWidgetBuilder
from omni.kit.window.property.templates.simple_property_widget import SimplePropertyWidget
from omni import ui
import pxr.Usd
from pxr import Usd
__all__ = ['AudioSettingsWidget', 'SimplePropertyWidget', 'Usd', 'UsdPropertiesWidgetBuilder', 'omni', 'ui']
class AudioSettingsWidget(omni.kit.window.property.templates.simple_property_widget.SimplePropertyWidget):
    """
    A widget to manage audio settings in a USD scene.
    
        This widget allows users to manipulate various audio parameters such as the active listener, doppler effects, distance delay, and others. It provides a user interface to modify settings that affect the audio simulation in the scene, including the speed of sound, doppler scale, and the timescale for spatial and non-spatial audio processing. The widget interacts with the USD stage and its audio interface to reflect changes and update the scene accordingly.
        
    """
    class ChangeNotifier(omni.ui._ui.AbstractValueModel):
        """
        A model representing the value of a changeable entity in the UI.
        
                This model notifies the provided callback with the updated value when a change occurs. It is typically used to reflect and manipulate values within UI components.
        
                Args:
                    update_callback (Callable[[Any], None]): The callback function to invoke when the value changes.
        """
        def __init__(self, update_callback):
            """
            Initializes a new instance of ChangeNotifier.
            """
        def get_value_as_float(self):
            """
            Retrieves the current value as a float.
            
                        Returns:
                            float: The value of the model converted to a float.
            """
        def get_value_as_int(self):
            """
            Retrieves the current value as an integer.
            
                        Returns:
                            int: The value of the model converted to an integer.
            """
        def get_value_as_string(self):
            """
            Returns the current value as a string.
            
                        Returns:
                            str: The value of the model represented as a string.
            """
    class DefaultsComboBoxNotifier(omni.ui._ui.AbstractItemModel):
        """
        A class for managing default audio feature settings via a combo box UI component.
        
                This class provides a way to select between different default states for audio features such as on, off, force on, and force off. It is used within the audio settings widget to control settings like Doppler effect, distance delay, and more.
        
                Args:
                    set_callback (Callable[[int], None]): A callback function that is called when the selected option changes. The callback is passed the integer value associated with the selected option.
                
        """
        class MinimalItem(omni.ui._ui.AbstractItem):
            """
            A minimalist UI item for representing an option in a combo box.
            
                        This class is used to create a simple UI element representing a selectable option within a combo box widget.
            
                        Args:
                            text (str): The display text for the combo box option.
            """
            def __init__(self, text):
                """
                Initializes a MinimalItem instance with default settings.
                """
        def __init__(self, set_callback):
            """
            Initializer for DefaultsComboBoxNotifier.
            """
        def _changed_model(self, model):
            ...
        def get_item_children(self, item):
            """
            Returns the child items of the given item.
            
                        Args:
                            item (omni.ui.AbstractItem): The item to get children for.
            
                        Returns:
                            The children of the given item.
                        
            """
        def get_item_value_model(self, item, column_id):
            """
            Gets the value model for the item and column id.
            
                        Args:
                            item (omni.ui.AbstractItem): The item to get the model for.
                            column_id (int): The column id for which the model is requested.
            
                        Returns:
                            The value model for the item.
                        
            """
        def set_value(self, value):
            """
            Sets the selected value in the combo box.
            
                        Args:
                            value (int): The value to be set as selected in the combo box.
            """
    class FastChangeNotifier(AudioSettingsWidget.ChangeNotifier):
        """
        A class that provides a fast notification mechanism for value changes.
        
                This notifier is designed to immediately trigger an update callback whenever its value is changed, without waiting for an edit to end. It is a specialized version of ChangeNotifier, inheriting its interface for value retrieval and modification.
        
                Args:
                    update_callback (callable): A function to be called whenever the value changes.
        """
        def set_value(self, value):
            """
            Sets the value to the notifier without triggering an update callback.
            
                        Args:
                            value (Any): The new value to be set.
            """
    class ListenerComboBoxNotifier(omni.ui._ui.AbstractItemModel):
        """
        A class that represents a custom item model for a combo box notifier.
        
                This model manages the selection and notification of changes in a combo box that represents a list of listeners. It is designed to be used in a UI context where the user can select an active listener from a dropdown menu. The class also handles the refresh of the item list based on external callbacks.
        
                Args:
                    refresh_items_callback (Callable[[], List[str]]): A callback function that returns a list of strings representing the available items for the combo box.
                    set_callback (Callable[[int], None]): A callback function that takes an index as an argument and sets the selected item based on this index.
                
        """
        class MinimalItem(omni.ui._ui.AbstractItem):
            """
            A minimalist UI item for representing an option in a combo box.
            
                        This class is used to create a simple UI element representing a selectable option within a combo box widget.
            
                        Args:
                            text (str): The display text for the combo box option.
            """
            def __init__(self, text):
                """
                Initializes a MinimalItem instance with default settings.
                """
        def __init__(self, refresh_items_callback, set_callback):
            """
            Initializer for ListenerComboBoxNotifier.
            """
        def _changed_model(self, model):
            ...
        def get_item_children(self, item):
            """
            Gets the children of the given item.
            
                        Args:
                            item (AbstractItem): The item to get children for.
            
                        Returns:
                            The children of the given item.
                        
            """
        def get_item_value_model(self, item, column_id):
            """
            Gets the value model for the item in the given column.
            
                        Args:
                            item (AbstractItem): The item to get the value model for.
                            column_id (int): The ID of the column.
            
                        Returns:
                            The value model of the input item.
                        
            """
        def get_value_as_string(self):
            """
            Returns the current path as a string.
            
                        Returns:
                            str: The current path.
            """
        def refresh_items(self):
            """
            Refreshes the items in the combo box based on the refresh_items_callback.
            """
        def set_value(self, value):
            """
            Sets the value of the selected item.
            
                        Args:
                            value (str): The value to set as the selected item.
            """
    class SlowChangeNotifier(AudioSettingsWidget.ChangeNotifier):
        """
        A notifier for handling slow changes to values.
        
                This class inherits from ChangeNotifier and is designed to update its value in a way
                that does not immediately trigger an update callback. Instead, the update callback
                is triggered when the end_edit method is called. This allows for delayed
                notification of changes, which is useful in scenarios where immediate feedback
                from every change is not necessary or desired.
        """
        def end_edit(self):
            """
            Triggers the update callback with the current value.
            """
        def set_value(self, value):
            """
            Sets the value to the notifier without triggering an update callback.
            
                        Args:
                            value (Any): The new value to be set.
            """
    def __del__(self):
        ...
    def __init__(self):
        """
        Initializes the AudioSettingsWidget with default settings.
        """
    def _add_label(self, label: str):
        ...
    def _caption(self, text, width = 150):
        """
        Create a formated heading
        """
    def _create_tooltip(self, text):
        """
        Create a tooltip in a fixed style
        """
    def _on_metadata_event(self, event):
        ...
    def _refresh(self):
        ...
    def _refresh_active_listener(self):
        ...
    def _refresh_listeners(self):
        ...
    def _set_active_listener(self, index):
        ...
    def build_items(self):
        """
        Builds the UI items for the audio settings widget.
        """
    def on_new_payload(self, payload):
        """
        Handles a new payload for the widget.
        
                Args:
                    payload (dict): The new payload to be handled by the widget.
        
                Returns:
                    bool: True if payload is not None, False otherwise.
        """
    def set_stage(self, stage: pxr.Usd.Stage):
        """
        Sets the stage for audio settings.
        
                Args:
                    stage (Usd.Stage): The stage to be set for the widget.
        """
