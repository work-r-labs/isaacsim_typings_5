from __future__ import annotations
import carb as carb
import omni as omni
import typing
__all__ = ['SNAP_ENABLED_SETTING', 'SnapHotkey', 'carb', 'omni']
class SnapHotkey:
    """
    A class that handles the registration, use, and cleanup of a hotkey for toggling snappable manipulators.
    
        This class provides functionality to register a hotkey that toggles snapping for manipulators in a viewport. It supports fallback registration if the hotkey core extension is not available and ensures that resources are cleaned up appropriately.
    
        Args:
            on_hotkey_changed_fn (Callable[[str], None], optional): Callback triggered when the hotkey state changes.
    """
    def __init__(self, on_hotkey_changed_fn: typing.Callable[[str], None] = None):
        """
        Initializes the SnapHotkey instance.
        
                Args:
                    on_hotkey_changed_fn (Callable[[str], None], optional): A callback function that will be called when the hotkey changes.
                
        """
    def _on_hotkey_changed(self, event: carb.events.IEvent):
        """
        Internal callback function that is invoked when the hotkey is changed.
        
                Args:
                    event (carb.events.IEvent): The event containing the hotkey change information.
        """
    def _register_hotkey(self):
        """
        Registers the hotkey using the hotkey core extension if it's available, otherwise,
                it falls back to a manual registration method.
        """
    def _register_hotkey_fallback(self):
        """
        Registers a fallback hotkey manually in case the hotkey core extension is not enabled.
        """
    def _unregister_hotkey(self):
        """
        Unregisters the hotkey and falls back to a manual registration method if necessary.
        
                It also cleans up any subscriptions and references related to hotkey registration.
        """
    def _unregister_hotkey_fallback(self):
        """
        Unregisters the fallback hotkey and cleans up any related resources.
        """
    def destroy(self):
        """
        Cleans up the snap hotkey by unregistering the hotkey, deregistering the action, and
                releasing other resources.
        """
    def get_as_string(self, default: str):
        """
        Gets the currently registered hotkey as a string representation.
        
                Args:
                    default (str): The default string to return if no hotkey is registered.
        
                Returns:
                    str: The registered hotkey as a string, or the default string if no hotkey is registered.
        """
SNAP_ENABLED_SETTING: str = '/app/viewport/snapEnabled'
