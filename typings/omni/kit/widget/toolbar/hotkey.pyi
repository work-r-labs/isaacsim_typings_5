from __future__ import annotations
import carb as carb
import omni as omni
import typing
__all__: list = ['Hotkey']
class Hotkey:
    """
    
        A helper class to add hotkey to a Toolbar widget.
    
        Hotkey registers an Action with `omni.kit.actions.core` and  assigns a hotkey using `omni.kit.hotkeys.core`.
        If `omni.kit.hotkeys.core` is not enabled, hotkey will not be in effect.
        
    """
    def __init__(self, action_name: str, hotkey: carb.input.KeyboardInput, on_action_fn: typing.Callable[[], None], hotkey_enabled_fn: typing.Callable[[], bool], modifiers: int = 0, on_hotkey_changed_fn: typing.Callable[[str], None] = None):
        """
        
                Initialize a Hotkey object.
        
                Args:
                    action_name (str): The Action name associated with the hotkey. It needs to be unique.
                    hotkey (carb.input.KeyboardInput): The keyboard key binding.
                    on_action_fn (Callable[[], None]): Callback function to be called when Action is triggered.
                    hotkey_enabled_fn (Callable[[], bool]): Predicate callback function to be called when Action is triggered,
                                                            but before `on_action_fn` to determine if it should be called.
                    modifiers (int): Modifier of the hotkey.
                    on_hotkey_changed_fn (Callable[[str], None]): Callback function when Hotkey is reassigned by external system
                                                                  such as `omni.kit.hotkeys.window`. The parameter will be the
                                                                  new key combo.
        
                
        """
    def _on_hotkey_changed(self, event: carb.events.IEvent):
        ...
    def _register_hotkey(self):
        ...
    def _unregister_hotkey(self):
        ...
    def clean(self):
        """
        
                Cleanup function to be called before Hotkey object is destroyed.
                
        """
    def get_as_string(self, default: str) -> str:
        """
        
                Gets the string representation of the hotkey combo. Useful as tooltip.
                
        """
