from __future__ import annotations
import carb as carb
import dataclasses
from dataclasses import asdict
from dataclasses import dataclass
import json as json
from omni.kit.hotkeys.core.filter import HotkeyFilter
import omni.kit.hotkeys.core.hotkey
from omni.kit.hotkeys.core.hotkey import Hotkey
from omni.kit.hotkeys.core.key_combination import KeyCombination
import typing
__all__: list = ['HotkeyDescription', 'HotkeyStorage']
class HotkeyDescription:
    """
    HotkeyDescription(hotkey_ext_id: str = '', action_ext_id: str = '', action_id: str = '', key: str = '', trigger_press: bool = True, context: str = None, windows: str = None)
    """
    __dataclass_fields__: typing.ClassVar[dict]  # value = {'hotkey_ext_id': Field(name='hotkey_ext_id',type=<class 'str'>,default='',default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'action_ext_id': Field(name='action_ext_id',type=<class 'str'>,default='',default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'action_id': Field(name='action_id',type=<class 'str'>,default='',default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'key': Field(name='key',type=<class 'str'>,default='',default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'trigger_press': Field(name='trigger_press',type=<class 'bool'>,default=True,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'context': Field(name='context',type=<class 'str'>,default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'windows': Field(name='windows',type=<class 'str'>,default=None,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD)}
    __dataclass_params__: typing.ClassVar[dataclasses._DataclassParams]  # value = _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)
    __hash__: typing.ClassVar[None] = None
    __match_args__: typing.ClassVar[tuple] = ('hotkey_ext_id', 'action_ext_id', 'action_id', 'key', 'trigger_press', 'context', 'windows')
    action_ext_id: typing.ClassVar[str] = ''
    action_id: typing.ClassVar[str] = ''
    context = None
    hotkey_ext_id: typing.ClassVar[str] = ''
    key: typing.ClassVar[str] = ''
    trigger_press: typing.ClassVar[bool] = True
    windows = None
    @staticmethod
    def from_hotkey(hotkey: omni.kit.hotkeys.core.hotkey.Hotkey):
        ...
    @staticmethod
    def get_filter_string(hotkey: omni.kit.hotkeys.core.hotkey.Hotkey) -> typing.Tuple[str, str]:
        ...
    def __eq__(self, other):
        ...
    def __init__(self, hotkey_ext_id: str = '', action_ext_id: str = '', action_id: str = '', key: str = '', trigger_press: bool = True, context: str = None, windows: str = None) -> None:
        ...
    def __repr__(self):
        ...
    def to_hotkey(self) -> omni.kit.hotkeys.core.hotkey.Hotkey:
        ...
    def update(self, hotkey: omni.kit.hotkeys.core.hotkey.Hotkey) -> None:
        ...
    @property
    def id(self) -> str:
        ...
class HotkeyStorage:
    def _HotkeyStorage__find_hotkey_desc(self, hotkey: omni.kit.hotkeys.core.hotkey.Hotkey) -> typing.Optional[omni.kit.hotkeys.core.storage.HotkeyDescription]:
        """
        
                Find if there is user-defined hotkey
                
        """
    def __init__(self):
        ...
    def clear_hotkeys(self) -> None:
        """
        
                Clear all hotkeys in storage
                
        """
    def deregister_hotkey(self, hotkey: omni.kit.hotkeys.core.hotkey.Hotkey):
        """
        
                Deregister user hotkey from storage.
        
                For system hotkey, keep in storage to reload when register again
                
        """
    def disable_hotkey(self, hotkey: omni.kit.hotkeys.core.hotkey.Hotkey):
        """
        
                Disable system hotkey.
                Disable means set key to empty string in storage.
                
        """
    def edit_hotkey(self, hotkey: omni.kit.hotkeys.core.hotkey.Hotkey):
        """
        
                Edit hotkey.
        
                This could be a user-defined hotkey or system hotkey but changed by user.
                
        """
    def get_hotkey(self, hotkey: omni.kit.hotkeys.core.hotkey.Hotkey) -> typing.Optional[omni.kit.hotkeys.core.hotkey.Hotkey]:
        """
        
                Get hotkey definition in storage.
                
        """
    def get_hotkeys(self) -> typing.List[omni.kit.hotkeys.core.hotkey.Hotkey]:
        """
        
                Discover all hotkey definitions in this storage.
                
        """
    def get_user_hotkeys(self) -> typing.List[omni.kit.hotkeys.core.hotkey.Hotkey]:
        """
        
                Get all user-defined hotkeys.
                
        """
    def is_user_hotkey(self, hotkey: omni.kit.hotkeys.core.hotkey.Hotkey) -> bool:
        """
        
                If a user-defined hotkey
                
        """
    def load_preset(self, preset: typing.List[typing.Dict]) -> None:
        """
        
                Load hotkey preset.
                
        """
    def preload_preset(self, url: str) -> typing.Optional[typing.Dict]:
        """
        
                Preload hotkey preset from file.
                
        """
    def register_user_hotkey(self, hotkey: omni.kit.hotkeys.core.hotkey.Hotkey):
        """
        
                Register user hotkey.
                
        """
    def save_preset(self, url: str) -> bool:
        """
        
                Save storage to file.
                
        """
SETTING_USER_HOTKEYS: str = '/persistent/omni.kit.hotkeys.core/userHotkeys'
USER_HOTKEY_EXT_ID: str = 'omni.kit.hotkeys.window'
