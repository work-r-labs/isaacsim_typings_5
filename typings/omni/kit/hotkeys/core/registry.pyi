from __future__ import annotations
import carb as carb
import copy as copy
import omni as omni
from omni.kit.hotkeys.core.filter import HotkeyFilter
from omni.kit.hotkeys.core.hotkey import Hotkey
from omni.kit.hotkeys.core.key_combination import KeyCombination
from omni.kit.hotkeys.core.keyboard_layout import KeyboardLayoutDelegate
from omni.kit.hotkeys.core.storage import HotkeyStorage
import typing
__all__: list = ['HotkeyRegistry']
class HotkeyRegistry:
    """
    
        Registry of hotkeys.
        
    """
    class Result:
        ERROR_ACTION_DUPLICATED: typing.ClassVar[str] = 'Duplicated action definition'
        ERROR_KEY_DUPLICATED: typing.ClassVar[str] = 'Duplicated key definition'
        ERROR_KEY_INVALID: typing.ClassVar[str] = 'Invalid key definition'
        ERROR_NO_ACTION: typing.ClassVar[str] = 'No action defined'
        OK: typing.ClassVar[str] = 'OK'
    def _HotkeyRegistry__append_user_hotkeys(self):
        ...
    def _HotkeyRegistry__deregister_hotkey_maps(self, hotkey: omni.kit.hotkeys.core.hotkey.Hotkey) -> bool:
        ...
    def _HotkeyRegistry__edit_hotkey_internal(self, hotkey: omni.kit.hotkeys.core.hotkey.Hotkey, key_combination: omni.kit.hotkeys.core.key_combination.KeyCombination, filter: typing.Optional[omni.kit.hotkeys.core.filter.HotkeyFilter]) -> None:
        ...
    def _HotkeyRegistry__register_hotkey_maps(self, hotkey: omni.kit.hotkeys.core.hotkey.Hotkey) -> None:
        ...
    def __init__(self):
        """
        
                Define hotkey registry object.
                
        """
    def _deregister_hotkey_args(self, hotkey_ext_id: str, key: typing.Union[str, omni.kit.hotkeys.core.key_combination.KeyCombination], filter: typing.Optional[omni.kit.hotkeys.core.filter.HotkeyFilter] = None) -> bool:
        ...
    def _deregister_hotkey_obj(self, hotkey: omni.kit.hotkeys.core.hotkey.Hotkey) -> bool:
        ...
    def _register_hotkey_args(self, hotkey_ext_id: str, key: typing.Union[str, omni.kit.hotkeys.core.key_combination.KeyCombination], action_ext_id: str, action_id: str, filter: typing.Optional[omni.kit.hotkeys.core.filter.HotkeyFilter] = None) -> typing.Optional[omni.kit.hotkeys.core.hotkey.Hotkey]:
        ...
    def _register_hotkey_obj(self, hotkey: omni.kit.hotkeys.core.hotkey.Hotkey) -> typing.Optional[omni.kit.hotkeys.core.hotkey.Hotkey]:
        ...
    def _send_event(self, event: int, hotkey: omni.kit.hotkeys.core.hotkey.Hotkey):
        ...
    def clear_storage(self) -> None:
        """
        
                Clear user defined hotkeys.
                
        """
    def deregister_all_hotkeys_for_extension(self, hotkey_ext_id: typing.Optional[str]) -> None:
        """
        
                Deregister hotkeys registered from a special extension.
        
                Args:
                    hotkey_ext_id (Optional[str]): Extension id that hotkeys belongs to. If None, discover all global hotkeys
                
        """
    def deregister_all_hotkeys_for_filter(self, filter: omni.kit.hotkeys.core.filter.HotkeyFilter) -> None:
        """
        
                Deregister hotkeys registered with speicial filter.
        
                Args:
                    filter (HotkeyFilter): Hotkey HotkeyFilter.
                
        """
    def deregister_hotkey(self, *args, **kwargs) -> bool:
        """
        
                Deregister hotkey by hotkey object or arguments.
        
                Args could be:
        
                .. code:: python
        
                    deregister_hotkey(hotkey: Hotkey)
        
                or
        
                .. code:: python
        
                    deregister_hotkey(
                        hotkey_ext_id: str,
                        key: Union[str, KeyCombination],
                        filter: Optional[HotkeyFilter] = None
                    )
        
                Returns:
                    True if hotkey found. Otherwise return False.
                
        """
    def deregister_hotkeys(self, hotkey_ext_id: str, key: typing.Union[str, omni.kit.hotkeys.core.key_combination.KeyCombination]) -> None:
        """
        
                Deregister hotkeys registered from a special extension with special key combination.
        
                Args:
                    hotkey_ext_id (str): Extension id that hotkeys belongs to.
                    key (Union[str, KeyCombination]): Key combination.
                
        """
    def disable_hotkey(self, hotkey: omni.kit.hotkeys.core.hotkey.Hotkey) -> bool:
        """
        
                Disable a system hotkey.
                Disable means:
                - Deregister the hotkey immediately
                - If the hotkey is a system hotkey, do not make it work even register again until preset reset
        
                Args:
                    hotkey [Hotkey]: Hotkey object
        
                Returns:
                    True if hotkey found. Otherwise return False.
                
        """
    def edit_hotkey(self, hotkey: omni.kit.hotkeys.core.hotkey.Hotkey, key: typing.Union[str, omni.kit.hotkeys.core.key_combination.KeyCombination], filter: typing.Optional[omni.kit.hotkeys.core.filter.HotkeyFilter]) -> HotkeyRegistry.Result:
        """
        
                Change key combination of hotkey object.
        
                Args:
                    hotkey (Hotkey): Hotkey object to change.
                    key (Union[str, KeyCombination]): New key combination.
                    filter (Optional[HotkeyFiler]): New filter.
        
                Returns:
                    Result code.
                
        """
    def export_storage(self, url: str) -> None:
        """
        
                Export user defined hotkeys to file.
        
                Args:
                    url (str): File path to export user defined hotkeys.
                
        """
    def get_all_hotkeys(self) -> typing.List[omni.kit.hotkeys.core.hotkey.Hotkey]:
        """
        
                Discover all registered hotkeys.
        
                Returns:
                    List of all registered hotkeys.
                
        """
    def get_all_hotkeys_for_extension(self, hotkey_ext_id: typing.Optional[str]) -> typing.List[omni.kit.hotkeys.core.hotkey.Hotkey]:
        """
        
                Discover hotkeys registered from a special extension.
        
                Args:
                    hotkey_ext_id (Optional[str]): Extension id that hotkeys belongs to. If None, discover all global hotkeys
        
                Returns:
                    List of discovered hotkeys.
                
        """
    def get_all_hotkeys_for_filter(self, filter: omni.kit.hotkeys.core.filter.HotkeyFilter) -> typing.List[omni.kit.hotkeys.core.hotkey.Hotkey]:
        """
        
                Discover hotkeys registered with speicial filter.
        
                Args:
                    filter (HotkeyFilter): Hotkey HotkeyFilter.
        
                Returns:
                    List of discovered hotkeys.
                
        """
    def get_all_hotkeys_for_key(self, key: typing.Union[str, omni.kit.hotkeys.core.key_combination.KeyCombination]) -> typing.List[omni.kit.hotkeys.core.hotkey.Hotkey]:
        """
        
                Discover hotkeys registered from a special key.
        
                Args:
                    key (Union[str, KeyCombination]): Key combination.
        
                Returns:
                    List of discovered hotkeys.
                
        """
    def get_hotkey(self, hotkey_ext_id: str, key: typing.Union[str, omni.kit.hotkeys.core.key_combination.KeyCombination], filter: typing.Optional[omni.kit.hotkeys.core.filter.HotkeyFilter] = None) -> typing.Optional[omni.kit.hotkeys.core.hotkey.Hotkey]:
        """
        
                Discover a registered hotkey.
        
                Args:
                    hotkey_ext_id (str): Extension id which owns the hotkey.
                    key (Union[str, KeyCombination]): Key combination.
        
                Keyword Args:
                    filter (Optional[HotkeyFilter]): Hotkey filter. Default None
        
                Returns:
                    Hotkey object if discovered. Otherwise None.
                
        """
    def get_hotkey_default(self, hotkey: omni.kit.hotkeys.core.hotkey.Hotkey) -> typing.Tuple[str, omni.kit.hotkeys.core.filter.HotkeyFilter]:
        """
        
                Discover hotkey default key binding and filter.
        
                Args:
                    hotkey (Hotkey): Hotkey object.
        
                Returns:
                    Tuple of key binding string and hotkey filter object.
                
        """
    def get_hotkey_for_filter(self, key: typing.Union[str, omni.kit.hotkeys.core.key_combination.KeyCombination], filter: omni.kit.hotkeys.core.filter.HotkeyFilter) -> typing.Optional[omni.kit.hotkeys.core.hotkey.Hotkey]:
        """
        
                Discover hotkey registered with special key combination and filter
        
                Args:
                    key (Union[str, KeyCombination]): Key combination.
                    filter (HotkeyFilter): Hotkey filter.
        
                Returns:
                    First discovered hotkey. None if nothing found.
                
        """
    def get_hotkey_for_trigger(self, key: typing.Union[str, omni.kit.hotkeys.core.key_combination.KeyCombination], context: typing.Optional[str] = None, window: typing.Optional[str] = None) -> typing.Optional[omni.kit.hotkeys.core.hotkey.Hotkey]:
        """
        
                Discover hotkey for trigger from key combination and filter.
        
                Args:
                    key (Union[str, KeyCombination]): Key combination.
        
                Keyword Args:
                    context (str): Context assigned to Hotkey
                    window (str): Window assigned to Hotkey
        
                Returns:
                    Hotkey object if discovered. Otherwise None.
                
        """
    def get_hotkeys(self, hotkey_ext_id: str, key: typing.Union[str, omni.kit.hotkeys.core.key_combination.KeyCombination]) -> typing.List[omni.kit.hotkeys.core.hotkey.Hotkey]:
        """
        
                Discover hotkeys registered from a special extension with special key combination.
        
                Args:
                    hotkey_ext_id (str): Extension id that hotkeys belongs to.
                    key (Union[str, KeyCombination]): Key combination.
        
                Returns:
                    List of discovered hotkeys.
                
        """
    def has_duplicated_hotkey(self, hotkey: omni.kit.hotkeys.core.hotkey.Hotkey) -> HotkeyRegistry.Result:
        """
        
                Check if already have hotkey registered.
        
                Args:
                    hotkey (Hotkey): Hotkey object to check.
        
                Returns:
                    Result code.
                
        """
    def import_storage(self, url: str) -> bool:
        """
        
                Import user defined hotkeys from file.
        
                Args:
                    url (str): File path to import user defined hotkeys.
                
        """
    def is_user_hotkey(self, hotkey: omni.kit.hotkeys.core.hotkey.Hotkey) -> bool:
        """
        
                If a user defined hotkey.
        
                Args:
                    hotkey (Hotkey): Hotkey object.
        
                Returns:
                    True if user defined. Otherwise False.
                
        """
    def register_hotkey(self, *args, **kwargs) -> typing.Optional[omni.kit.hotkeys.core.hotkey.Hotkey]:
        """
        
                Register hotkey by hotkey object or arguments.
        
                Args could be:
        
                .. code:: python
        
                    register_hotkey(hotkey: Hotkey)
        
                or
        
                .. code:: python
        
                    register_hotkey(
                        hotkey_ext_id: str,
                        key: Union[str, KeyCombination],
                        action_ext_id: str,
                        action_id: str,
                        filter: Optional[HotkeyFilter] = None
                    )
        
                Returns:
                    Created hotkey object if register succeeded. Otherwise return None.
                
        """
    def restore_defaults(self) -> None:
        """
        
                Clean user defined hotkeys and restore system hotkey to default
                
        """
    def switch_layout(self, layout_name: str) -> None:
        """
        
                Change keyboard layout.
        
                Args:
                    layout_name (str): Name of keyboard layout to use.
                
        """
    def verify_hotkey(self, hotkey: omni.kit.hotkeys.core.hotkey.Hotkey, key_combination: typing.Optional[omni.kit.hotkeys.core.key_combination.KeyCombination] = None, hotkey_filter: typing.Optional[omni.kit.hotkeys.core.filter.HotkeyFilter] = None) -> HotkeyRegistry.Result:
        """
        
                Verify hotkey.
                
        """
    @property
    def keyboard_layout(self) -> typing.Optional[omni.kit.hotkeys.core.keyboard_layout.KeyboardLayoutDelegate]:
        """
        
                Current keyboard layout object in using.
                
        """
    @property
    def last_error(self) -> HotkeyRegistry.Result:
        """
        
                Error code for last hotkey command.
                
        """
HOTKEY_CHANGED_EVENT: int = 10827232480668153655
HOTKEY_DEREGISTER_EVENT: int = 2474222670972880127
HOTKEY_REGISTER_EVENT: int = 4501832906121664548
SETTING_DEFAULT_KEYBOARD_LAYOUT: str = '/exts/omni.kit.hotkeys.core/default_keyboard_layout'
