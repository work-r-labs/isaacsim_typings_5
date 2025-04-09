from __future__ import annotations
import carb as carb
__all__: list = ['HotkeyContext']
class HotkeyContext:
    def __init__(self):
        """
        Represent hotkey context.
        """
    def _update_settings(self):
        ...
    def clean(self) -> None:
        """
        Clean all contexts
        """
    def get(self) -> typing.Optional[str]:
        """
        Get last context.
        """
    def pop(self) -> typing.Optional[str]:
        """
        Remove and return last context.
        """
    def push(self, name: str) -> None:
        """
        
                Push a context.
        
                Args:
                    name (str): name of context
                
        """
SETTING_HOTKEY_CURRENT_CONTEXT: str = '/exts/omni.kit.hotkeys.core/context'
