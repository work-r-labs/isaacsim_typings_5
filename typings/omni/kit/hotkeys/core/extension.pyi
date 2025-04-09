from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.hotkeys.core.context import HotkeyContext
from omni.kit.hotkeys.core.keyboard_layout import FrenchKeyboardLayout
from omni.kit.hotkeys.core.keyboard_layout import GermanKeyboardLayout
from omni.kit.hotkeys.core.keyboard_layout import USKeyboardLayout
from omni.kit.hotkeys.core.registry import HotkeyRegistry
from omni.kit.hotkeys.core.trigger import HotkeyTrigger
__all__: list = ['get_hotkey_context', 'get_hotkey_registry', 'HotkeysExtension']
class HotkeysExtension(omni.ext._extensions.IExt):
    """
    
        Hotkeys extension.
        
    """
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        """
        
                Extension startup entrypoint.
                
        """
def get_hotkey_context() -> omni.kit.hotkeys.core.context.HotkeyContext:
    """
    
        Get the hotkey context.
    
        Return:
            HotkeyContext object which implements the hotkey context interface.
        
    """
def get_hotkey_registry() -> omni.kit.hotkeys.core.registry.HotkeyRegistry:
    """
    
        Get the hotkey registry.
    
        Return:
            HotkeyRegistry object which implements the hotkey registry interface.
        
    """
_hotkey_context: omni.kit.hotkeys.core.context.HotkeyContext  # value = <omni.kit.hotkeys.core.context.HotkeyContext object>
_hotkey_registry: omni.kit.hotkeys.core.registry.HotkeyRegistry  # value = <omni.kit.hotkeys.core.registry.HotkeyRegistry object>
