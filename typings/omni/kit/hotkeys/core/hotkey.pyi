from __future__ import annotations
import carb as carb
import omni.kit.actions.core._kit_actions_core
from omni.kit.actions.core._kit_actions_core import Action
from omni.kit.actions.core.actions import get_action_registry
from omni.kit.hotkeys.core.filter import HotkeyFilter
from omni.kit.hotkeys.core.key_combination import KeyCombination
import typing
__all__ = ['Action', 'Hotkey', 'HotkeyFilter', 'KeyCombination', 'carb', 'get_action_registry']
class Hotkey:
    """
    
        Hotkey object class.
        
    """
    __hash__: typing.ClassVar[None] = None
    def __eq__(self, other) -> bool:
        ...
    def __init__(self, hotkey_ext_id: str, key: typing.Union[str, omni.kit.hotkeys.core.key_combination.KeyCombination], action_ext_id: str, action_id: str, filter: typing.Optional[omni.kit.hotkeys.core.filter.HotkeyFilter] = None):
        """
        
                Define a hotkey object.
        
                Args:
                    hotkey_ext_id (str): Extension id which owns the hotkey.
                    key (Union[str, KeyCombination]): Key combination.
                    action_ext_id (str): Extension id which owns the action assigned to the hotkey.
                    action_id (str): Action id assigned to the hotkey.
        
                Keyword Args:
                    filter (Optional[HotkeyFilter]): Hotkey filter. Default None
        
                Returns:
                    The hotkey object that was created.
                
        """
    def __repr__(self):
        ...
    def execute(self) -> None:
        """
        
                Execute action assigned to the hotkey
                
        """
    @property
    def action(self) -> omni.kit.actions.core._kit_actions_core.Action:
        """
        
                Action object assigned to this hotkey.
                
        """
    @property
    def action_text(self) -> str:
        """
        
                String of action object assigned to this hotkey.
                
        """
    @property
    def filter_text(self) -> str:
        """
        
                String of filter object assigned to this hotkey.
                
        """
    @property
    def id(self) -> str:
        """
        
                Identifier string of this hotkey.
                
        """
    @property
    def key_text(self) -> str:
        """
        
                String of key bindings assigned to this hotkey.
                
        """
