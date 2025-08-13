from __future__ import annotations
import abc as abc
import carb as carb
import omni.kit.hotkeys.core.key_combination
from omni.kit.hotkeys.core.key_combination import KeyCombination
import typing
import weakref as weakref
__all__: list[str] = ['FrenchKeyboardLayout', 'GermanKeyboardLayout', 'KeyCombination', 'KeyboardLayoutDelegate', 'USKeyboardLayout', 'abc', 'carb', 'weakref']
class FrenchKeyboardLayout(KeyboardLayoutDelegate):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def get_maps(self) -> typing.Dict[carb.input.KeyboardInput, carb.input.KeyboardInput]:
        ...
    def get_name(self) -> str:
        ...
class GermanKeyboardLayout(KeyboardLayoutDelegate):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def get_maps(self) -> typing.Dict[carb.input.KeyboardInput, carb.input.KeyboardInput]:
        ...
    def get_name(self) -> str:
        ...
class KeyboardLayoutDelegate(abc.ABC):
    """
    Base class for keyboard layout delegates and registry of these same delegate instances.
        Whenever an instance of this class is created, it is automatically registered.
        
    """
    _KeyboardLayoutDelegate__g_registered: typing.ClassVar[list]  # value = [<weakref at 0x7031499722a0; to 'USKeyboardLayout' at 0x7031491aa910>, <weakref at 0x703147e18900; to 'GermanKeyboardLayout' at 0x7031491876d0>, <weakref at 0x703147e19490; to 'FrenchKeyboardLayout' at 0x7031491aba50>]
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'get_name', 'get_maps'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @classmethod
    def get_instance(cls, name: str) -> typing.Optional[ForwardRef('KeyboardLayoutDelegate')]:
        ...
    @classmethod
    def get_instances(cls) -> typing.List[ForwardRef('KeyboardLayoutDelegate')]:
        ...
    def __del__(self):
        ...
    def __init__(self):
        ...
    def destroy(self):
        ...
    def get_maps(self) -> dict:
        ...
    def get_name(self) -> str:
        ...
    def map_key(self, key: omni.kit.hotkeys.core.key_combination.KeyCombination) -> typing.Optional[omni.kit.hotkeys.core.key_combination.KeyCombination]:
        ...
    def restore_key(self, key: omni.kit.hotkeys.core.key_combination.KeyCombination) -> typing.Optional[omni.kit.hotkeys.core.key_combination.KeyCombination]:
        ...
class USKeyboardLayout(KeyboardLayoutDelegate):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def get_maps(self) -> typing.Dict[carb.input.KeyboardInput, carb.input.KeyboardInput]:
        ...
    def get_name(self) -> str:
        ...
