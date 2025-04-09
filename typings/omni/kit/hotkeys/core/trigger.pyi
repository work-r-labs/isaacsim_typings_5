from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.hotkeys.core.context import HotkeyContext
from omni.kit.hotkeys.core.hovered_window import get_hovered_window
from omni.kit.hotkeys.core.key_combination import KeyCombination
from omni.kit.hotkeys.core.registry import HotkeyRegistry
__all__: list = ['HotkeyTrigger']
class HotkeyTrigger:
    def _HotkeyTrigger__trigger(self, key_combination: omni.kit.hotkeys.core.key_combination.KeyCombination, pos_x: float, pos_y: float):
        ...
    def __init__(self, registry: omni.kit.hotkeys.core.registry.HotkeyRegistry, context: omni.kit.hotkeys.core.context.HotkeyContext):
        """
        
                Trigger hotkey on keyboard input.
        
                Args:
                    registry (HotkeyRegistry): Hotkey registry.
                    context (HotkeyContext): Hotkey context.
                
        """
    def _on_input_event(self, event, *_):
        ...
    def _run(self):
        ...
    def destroy(self):
        ...
SETTING_ALLOW_LIST: str = '/exts/omni.kit.hotkeys.core/allow_list'
