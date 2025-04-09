from __future__ import annotations
import carb as carb
import enum
from enum import Enum
from enum import auto
from omni.kit.manipulator.transform.settings_constants import Constants as c
import omni.kit.manipulator.transform.subscription
from omni.kit.manipulator.transform.subscription import Subscription
import typing
import weakref as weakref
__all__ = ['Enum', 'Listener', 'OpSettingsListener', 'SnapSettingsListener', 'Subscription', 'auto', 'c', 'carb', 'weakref']
class Listener:
    """
    A class that manages a collection of callback functions.
    
        This class provides methods to add, remove, and invoke callbacks. It is used for listening to
        settings changes and executing the registered callbacks when those settings change.
    """
    def __init__(self):
        """
        Initializes the Listener with an empty dictionary to store callbacks.
        """
    def _invoke_callbacks(self, *args, **kwargs):
        """
        Invokes all registered callbacks with the given arguments and keyword arguments.
        """
    def add_listener(self, callback: typing.Callable) -> int:
        """
        Adds a callback to the Listener.
        
                Args:
                    callback (Callable): The function to be called when the listener is triggered.
        
                Returns:
                    int: A unique identifier for the newly added callback.
        """
    def remove_listener(self, id: int):
        """
        Removes a callback from the Listener by its identifier.
        
                Args:
                    id (int): The unique identifier of the callback to be removed.
        """
    def subscribe_listener(self, callback: typing.Callable) -> omni.kit.manipulator.transform.subscription.Subscription:
        """
        Subscribes a callback to the Listener and returns a Subscription object.
        
                The Subscription object, when deleted, will remove the callback from the Listener.
        
                Args:
                    callback (Callable): The function to be called when the listener is triggered.
        
                Returns:
                    Subscription: An object representing the subscription, which can be used to unsubscribe the callback.
        """
class OpSettingsListener(Listener):
    """
    A listener for operation settings in a transformation manipulator.
    
        This class extends the base `Listener` to specifically listen to changes in operation,
        translation mode, and rotation mode settings. When a change is detected, registered callbacks
        are invoked with the appropriate `CallbackType`.
    
        Attributes:
            selected_op: The currently selected operation mode.
            translation_mode: The current translation mode setting.
            rotation_mode: The current rotation mode setting.
        
    """
    class CallbackType(enum.Enum):
        """
        An enumeration of callback types for the OpSettingsListener.
        
                This enum defines the types of changes that the OpSettingsListener can be notified about.
        """
        OP_CHANGED: typing.ClassVar[OpSettingsListener.CallbackType]  # value = <CallbackType.OP_CHANGED: 1>
        ROTATION_MODE_CHANGED: typing.ClassVar[OpSettingsListener.CallbackType]  # value = <CallbackType.ROTATION_MODE_CHANGED: 3>
        TRANSLATION_MODE_CHANGED: typing.ClassVar[OpSettingsListener.CallbackType]  # value = <CallbackType.TRANSLATION_MODE_CHANGED: 2>
    def __del__(self):
        ...
    def __init__(self) -> None:
        ...
    def _on_op_changed(self, item, event_type):
        ...
    def _on_rotation_mode_changed(self, item, event_type):
        ...
    def _on_translate_mode_changed(self, item, event_type):
        ...
    def destroy(self):
        ...
class SnapSettingsListener(Listener):
    """
    A class that listens for changes in snap settings and triggers callbacks.
    
        This class extends the base `Listener` class to monitor various snap settings such as snap enable toggle, snap movement along axes, snap rotation, snap scaling, and snap to surface provider. It subscribes to the settings and updates its attributes accordingly when a change is detected.
    
        Args:
            enabled_setting_path (str, optional): The setting path for snap enable toggle. Defaults to '/app/viewport/snapEnabled'.
            move_x_setting_path (str, optional): The setting path for snap movement along the x-axis. Defaults to '/persistent/app/viewport/stepMove/x'.
            move_y_setting_path (str, optional): The setting path for snap movement along the y-axis. Defaults to '/persistent/app/viewport/stepMove/y'.
            move_z_setting_path (str, optional): The setting path for snap movement along the z-axis. Defaults to '/persistent/app/viewport/stepMove/z'.
            rotate_setting_path (str, optional): The setting path for snap rotation. Defaults to '/persistent/app/viewport/stepRotate'.
            scale_setting_path (str, optional): The setting path for snap scaling. Defaults to '/persistent/app/viewport/stepScale'.
            provider_setting_path (str, optional): The setting path for snap to surface provider. Defaults to '/persistent/app/viewport/snapToSurface'.
    """
    def __del__(self):
        ...
    def __init__(self, enabled_setting_path: str = None, move_x_setting_path: str = None, move_y_setting_path: str = None, move_z_setting_path: str = None, rotate_setting_path: str = None, scale_setting_path: str = None, provider_setting_path: str = None) -> None:
        """
        Initializes a SnapSettingsListener to listen for changes in snap settings.
        """
    def destroy(self):
        """
        Cleans up the subscriptions made by the SnapSettingsListener instance.
        
                This method unsubscribes from all the setting change events to which this listener has previously subscribed.
        """
