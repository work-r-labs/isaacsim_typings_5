"""
pybind11 carb.input bindings
"""
from __future__ import annotations
import carb._carb
import typing
__all__ = ['ActionEvent', 'ActionMappingDesc', 'ActionMappingSet', 'BUTTON_FLAG_DOWN', 'BUTTON_FLAG_PRESSED', 'BUTTON_FLAG_RELEASED', 'BUTTON_FLAG_UP', 'DeviceType', 'EVENT_TYPE_ALL', 'EventType', 'FilterResult', 'Gamepad', 'GamepadConnectionEvent', 'GamepadConnectionEventType', 'GamepadEvent', 'GamepadInput', 'IInput', 'InputDevice', 'InputEvent', 'InputProvider', 'KEYBOARD_MODIFIER_FLAG_ALT', 'KEYBOARD_MODIFIER_FLAG_CAPS_LOCK', 'KEYBOARD_MODIFIER_FLAG_CONTROL', 'KEYBOARD_MODIFIER_FLAG_NUM_LOCK', 'KEYBOARD_MODIFIER_FLAG_SHIFT', 'KEYBOARD_MODIFIER_FLAG_SUPER', 'Keyboard', 'KeyboardEvent', 'KeyboardEventType', 'KeyboardInput', 'Mouse', 'MouseEvent', 'MouseEventType', 'MouseInput', 'SUBSCRIPTION_ORDER_DEFAULT', 'SUBSCRIPTION_ORDER_FIRST', 'SUBSCRIPTION_ORDER_LAST', 'acquire_input_interface', 'acquire_input_provider', 'get_action_mapping_desc_from_string', 'get_string_from_action_mapping_desc']
class ActionEvent:
    @property
    def action(self) -> str:
        ...
    @property
    def flags(self) -> int:
        ...
    @property
    def value(self) -> float:
        ...
class ActionMappingDesc:
    @property
    def device(self) -> typing.Any:
        ...
    @property
    def deviceType(self) -> DeviceType:
        ...
    @property
    def input(self) -> typing.Any:
        ...
    @property
    def modifiers(self) -> int:
        ...
class ActionMappingSet:
    pass
class DeviceType:
    """
    Members:
    
      KEYBOARD
    
      MOUSE
    
      GAMEPAD
    """
    GAMEPAD: typing.ClassVar[DeviceType]  # value = <DeviceType.GAMEPAD: 2>
    KEYBOARD: typing.ClassVar[DeviceType]  # value = <DeviceType.KEYBOARD: 0>
    MOUSE: typing.ClassVar[DeviceType]  # value = <DeviceType.MOUSE: 1>
    __members__: typing.ClassVar[dict[str, DeviceType]]  # value = {'KEYBOARD': <DeviceType.KEYBOARD: 0>, 'MOUSE': <DeviceType.MOUSE: 1>, 'GAMEPAD': <DeviceType.GAMEPAD: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EventType:
    """
    Members:
    
      UNKNOWN
    """
    UNKNOWN: typing.ClassVar[EventType]  # value = <EventType.UNKNOWN: 0>
    __members__: typing.ClassVar[dict[str, EventType]]  # value = {'UNKNOWN': <EventType.UNKNOWN: 0>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class FilterResult:
    """
    Members:
    
      RETAIN
    
      CONSUME
    """
    CONSUME: typing.ClassVar[FilterResult]  # value = <FilterResult.CONSUME: 1>
    RETAIN: typing.ClassVar[FilterResult]  # value = <FilterResult.RETAIN: 0>
    __members__: typing.ClassVar[dict[str, FilterResult]]  # value = {'RETAIN': <FilterResult.RETAIN: 0>, 'CONSUME': <FilterResult.CONSUME: 1>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Gamepad(InputDevice):
    def __hash__(self) -> int:
        ...
class GamepadConnectionEvent:
    @property
    def device(self) -> InputDevice:
        ...
    @property
    def gamepad(self) -> Gamepad:
        ...
    @property
    def type(self) -> GamepadConnectionEventType:
        ...
class GamepadConnectionEventType:
    """
    Members:
    
      CREATED
    
      CONNECTED
    
      DISCONNECTED
    
      DESTROYED
    """
    CONNECTED: typing.ClassVar[GamepadConnectionEventType]  # value = <GamepadConnectionEventType.CONNECTED: 1>
    CREATED: typing.ClassVar[GamepadConnectionEventType]  # value = <GamepadConnectionEventType.CREATED: 0>
    DESTROYED: typing.ClassVar[GamepadConnectionEventType]  # value = <GamepadConnectionEventType.DESTROYED: 3>
    DISCONNECTED: typing.ClassVar[GamepadConnectionEventType]  # value = <GamepadConnectionEventType.DISCONNECTED: 2>
    __members__: typing.ClassVar[dict[str, GamepadConnectionEventType]]  # value = {'CREATED': <GamepadConnectionEventType.CREATED: 0>, 'CONNECTED': <GamepadConnectionEventType.CONNECTED: 1>, 'DISCONNECTED': <GamepadConnectionEventType.DISCONNECTED: 2>, 'DESTROYED': <GamepadConnectionEventType.DESTROYED: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class GamepadEvent:
    @property
    def device(self) -> InputDevice:
        ...
    @property
    def gamepad(self) -> Gamepad:
        ...
    @property
    def input(self) -> GamepadInput:
        ...
    @property
    def value(self) -> float:
        ...
class GamepadInput:
    """
    Members:
    
      LEFT_STICK_RIGHT
    
      LEFT_STICK_LEFT
    
      LEFT_STICK_UP
    
      LEFT_STICK_DOWN
    
      RIGHT_STICK_RIGHT
    
      RIGHT_STICK_LEFT
    
      RIGHT_STICK_UP
    
      RIGHT_STICK_DOWN
    
      LEFT_TRIGGER
    
      RIGHT_TRIGGER
    
      A
    
      B
    
      X
    
      Y
    
      LEFT_SHOULDER
    
      RIGHT_SHOULDER
    
      MENU1
    
      MENU2
    
      LEFT_STICK
    
      RIGHT_STICK
    
      DPAD_UP
    
      DPAD_RIGHT
    
      DPAD_DOWN
    
      DPAD_LEFT
    
      COUNT
    """
    A: typing.ClassVar[GamepadInput]  # value = <GamepadInput.A: 10>
    B: typing.ClassVar[GamepadInput]  # value = <GamepadInput.B: 11>
    COUNT: typing.ClassVar[GamepadInput]  # value = <GamepadInput.COUNT: 24>
    DPAD_DOWN: typing.ClassVar[GamepadInput]  # value = <GamepadInput.DPAD_DOWN: 22>
    DPAD_LEFT: typing.ClassVar[GamepadInput]  # value = <GamepadInput.DPAD_LEFT: 23>
    DPAD_RIGHT: typing.ClassVar[GamepadInput]  # value = <GamepadInput.DPAD_RIGHT: 21>
    DPAD_UP: typing.ClassVar[GamepadInput]  # value = <GamepadInput.DPAD_UP: 20>
    LEFT_SHOULDER: typing.ClassVar[GamepadInput]  # value = <GamepadInput.LEFT_SHOULDER: 14>
    LEFT_STICK: typing.ClassVar[GamepadInput]  # value = <GamepadInput.LEFT_STICK: 18>
    LEFT_STICK_DOWN: typing.ClassVar[GamepadInput]  # value = <GamepadInput.LEFT_STICK_DOWN: 3>
    LEFT_STICK_LEFT: typing.ClassVar[GamepadInput]  # value = <GamepadInput.LEFT_STICK_LEFT: 1>
    LEFT_STICK_RIGHT: typing.ClassVar[GamepadInput]  # value = <GamepadInput.LEFT_STICK_RIGHT: 0>
    LEFT_STICK_UP: typing.ClassVar[GamepadInput]  # value = <GamepadInput.LEFT_STICK_UP: 2>
    LEFT_TRIGGER: typing.ClassVar[GamepadInput]  # value = <GamepadInput.LEFT_TRIGGER: 8>
    MENU1: typing.ClassVar[GamepadInput]  # value = <GamepadInput.MENU1: 16>
    MENU2: typing.ClassVar[GamepadInput]  # value = <GamepadInput.MENU2: 17>
    RIGHT_SHOULDER: typing.ClassVar[GamepadInput]  # value = <GamepadInput.RIGHT_SHOULDER: 15>
    RIGHT_STICK: typing.ClassVar[GamepadInput]  # value = <GamepadInput.RIGHT_STICK: 19>
    RIGHT_STICK_DOWN: typing.ClassVar[GamepadInput]  # value = <GamepadInput.RIGHT_STICK_DOWN: 7>
    RIGHT_STICK_LEFT: typing.ClassVar[GamepadInput]  # value = <GamepadInput.RIGHT_STICK_LEFT: 5>
    RIGHT_STICK_RIGHT: typing.ClassVar[GamepadInput]  # value = <GamepadInput.RIGHT_STICK_RIGHT: 4>
    RIGHT_STICK_UP: typing.ClassVar[GamepadInput]  # value = <GamepadInput.RIGHT_STICK_UP: 6>
    RIGHT_TRIGGER: typing.ClassVar[GamepadInput]  # value = <GamepadInput.RIGHT_TRIGGER: 9>
    X: typing.ClassVar[GamepadInput]  # value = <GamepadInput.X: 12>
    Y: typing.ClassVar[GamepadInput]  # value = <GamepadInput.Y: 13>
    __members__: typing.ClassVar[dict[str, GamepadInput]]  # value = {'LEFT_STICK_RIGHT': <GamepadInput.LEFT_STICK_RIGHT: 0>, 'LEFT_STICK_LEFT': <GamepadInput.LEFT_STICK_LEFT: 1>, 'LEFT_STICK_UP': <GamepadInput.LEFT_STICK_UP: 2>, 'LEFT_STICK_DOWN': <GamepadInput.LEFT_STICK_DOWN: 3>, 'RIGHT_STICK_RIGHT': <GamepadInput.RIGHT_STICK_RIGHT: 4>, 'RIGHT_STICK_LEFT': <GamepadInput.RIGHT_STICK_LEFT: 5>, 'RIGHT_STICK_UP': <GamepadInput.RIGHT_STICK_UP: 6>, 'RIGHT_STICK_DOWN': <GamepadInput.RIGHT_STICK_DOWN: 7>, 'LEFT_TRIGGER': <GamepadInput.LEFT_TRIGGER: 8>, 'RIGHT_TRIGGER': <GamepadInput.RIGHT_TRIGGER: 9>, 'A': <GamepadInput.A: 10>, 'B': <GamepadInput.B: 11>, 'X': <GamepadInput.X: 12>, 'Y': <GamepadInput.Y: 13>, 'LEFT_SHOULDER': <GamepadInput.LEFT_SHOULDER: 14>, 'RIGHT_SHOULDER': <GamepadInput.RIGHT_SHOULDER: 15>, 'MENU1': <GamepadInput.MENU1: 16>, 'MENU2': <GamepadInput.MENU2: 17>, 'LEFT_STICK': <GamepadInput.LEFT_STICK: 18>, 'RIGHT_STICK': <GamepadInput.RIGHT_STICK: 19>, 'DPAD_UP': <GamepadInput.DPAD_UP: 20>, 'DPAD_RIGHT': <GamepadInput.DPAD_RIGHT: 21>, 'DPAD_DOWN': <GamepadInput.DPAD_DOWN: 22>, 'DPAD_LEFT': <GamepadInput.DPAD_LEFT: 23>, 'COUNT': <GamepadInput.COUNT: 24>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class IInput:
    @typing.overload
    def add_action_mapping(self, action_mapping_set: ActionMappingSet, action: str, keyboard: Keyboard, keyboard_input: KeyboardInput, modifiers: int = 0) -> int:
        ...
    @typing.overload
    def add_action_mapping(self, action_mapping_set: ActionMappingSet, action: str, mouse: Mouse, mouse_input: MouseInput, modifiers: int = 0) -> int:
        ...
    @typing.overload
    def add_action_mapping(self, action_mapping_set: ActionMappingSet, action: str, gamepad: Gamepad, gamepad_input: GamepadInput) -> int:
        ...
    def clear_action_mappings(self, arg0: ActionMappingSet, arg1: str) -> None:
        ...
    def create_action_mapping_set(self, arg0: str) -> ActionMappingSet:
        ...
    def destroy_action_mapping_set(self, arg0: ActionMappingSet) -> None:
        ...
    def distribute_buffered_events(self) -> None:
        ...
    def filter_buffered_events(self, arg0: typing.Callable[[InputEvent], FilterResult]) -> None:
        ...
    @typing.overload
    def get_action_button_flags(self, arg0: ActionMappingSet, arg1: str) -> int:
        ...
    @typing.overload
    def get_action_button_flags(self, arg0: ActionMappingSet, arg1: str) -> int:
        ...
    def get_action_count(self, arg0: ActionMappingSet) -> int:
        ...
    def get_action_mapping_count(self, arg0: ActionMappingSet, arg1: str) -> int:
        ...
    @typing.overload
    def get_action_mapping_set_by_path(self, arg0: str) -> ActionMappingSet:
        ...
    @typing.overload
    def get_action_mapping_set_by_path(self, arg0: str) -> ActionMappingSet:
        ...
    def get_action_mappings(self, arg0: ActionMappingSet, arg1: str) -> list[ActionMappingDesc]:
        ...
    @typing.overload
    def get_action_value(self, arg0: ActionMappingSet, arg1: str) -> float:
        ...
    @typing.overload
    def get_action_value(self, arg0: ActionMappingSet, arg1: str) -> float:
        ...
    def get_actions(self, arg0: ActionMappingSet) -> list[str]:
        ...
    def get_device_name(self, arg0: InputDevice) -> str:
        ...
    def get_device_type(self, arg0: InputDevice) -> DeviceType:
        ...
    def get_gamepad_button_flags(self, arg0: Gamepad, arg1: GamepadInput) -> int:
        ...
    def get_gamepad_guid(self, arg0: Gamepad) -> str:
        ...
    def get_gamepad_name(self, arg0: Gamepad) -> str:
        ...
    def get_gamepad_value(self, arg0: Gamepad, arg1: GamepadInput) -> float:
        ...
    def get_global_modifier_flags(self, modifiers: int = 0, mouse_buttons: typing.Any = None) -> int:
        ...
    def get_input_provider(self) -> ...:
        ...
    def get_keyboard_button_flags(self, arg0: Keyboard, arg1: KeyboardInput) -> int:
        ...
    def get_keyboard_name(self, arg0: Keyboard) -> str:
        ...
    def get_keyboard_value(self, arg0: Keyboard, arg1: KeyboardInput) -> float:
        ...
    def get_modifier_flags(self, modifiers: int = 0, input_devices: list[InputDevice] = [], device_types: list[DeviceType] = [], mouse_buttons: typing.Any = None) -> int:
        ...
    def get_mouse_button_flags(self, arg0: Mouse, arg1: MouseInput) -> int:
        ...
    def get_mouse_coords_normalized(self, arg0: Mouse) -> carb._carb.Float2:
        ...
    def get_mouse_coords_pixel(self, arg0: Mouse) -> carb._carb.Float2:
        ...
    def get_mouse_name(self, arg0: Mouse) -> str:
        ...
    def get_mouse_value(self, arg0: Mouse, arg1: MouseInput) -> float:
        ...
    def remove_action_mapping(self, arg0: ActionMappingSet, arg1: str, arg2: int) -> None:
        ...
    @typing.overload
    def set_action_mapping(self, action_mapping_set: ActionMappingSet, action: str, index: int, keyboard: Keyboard, keyboard_input: KeyboardInput, modifiers: int = 0) -> None:
        ...
    @typing.overload
    def set_action_mapping(self, action_mapping_set: ActionMappingSet, action: str, index: int, mouse: Mouse, mouse_input: MouseInput, modifiers: int = 0) -> None:
        ...
    @typing.overload
    def set_action_mapping(self, action_mapping_set: ActionMappingSet, action: str, index: int, gamepad: Gamepad, gamepad_input: GamepadInput) -> None:
        ...
    @typing.overload
    def set_default_action_mapping(self, arg0: ActionMappingSet, arg1: str, arg2: Keyboard, arg3: KeyboardInput, arg4: int) -> bool:
        ...
    @typing.overload
    def set_default_action_mapping(self, arg0: ActionMappingSet, arg1: str, arg2: Gamepad, arg3: GamepadInput) -> bool:
        ...
    @typing.overload
    def set_default_action_mapping(self, arg0: ActionMappingSet, arg1: str, arg2: Mouse, arg3: MouseInput, arg4: int) -> bool:
        ...
    def shutdown(self) -> None:
        ...
    def startup(self) -> None:
        ...
    @typing.overload
    def subscribe_to_action_events(self, arg0: ActionMappingSet, arg1: str, arg2: typing.Callable[[ActionEvent], bool]) -> int:
        ...
    @typing.overload
    def subscribe_to_action_events(self, arg0: ActionMappingSet, arg1: str, arg2: typing.Callable[[ActionEvent], bool]) -> int:
        ...
    def subscribe_to_gamepad_connection_events(self, arg0: typing.Callable[[GamepadConnectionEvent], None]) -> int:
        ...
    def subscribe_to_gamepad_events(self, arg0: Gamepad, arg1: typing.Callable[[GamepadEvent], bool]) -> int:
        ...
    def subscribe_to_input_events(self, eventFn: typing.Callable[[InputEvent], bool], eventTypes: int = 4294967295, device: InputDevice = None, order: int = -1) -> int:
        ...
    def subscribe_to_keyboard_events(self, arg0: Keyboard, arg1: typing.Callable[[KeyboardEvent], bool]) -> int:
        ...
    def subscribe_to_mouse_events(self, arg0: Mouse, arg1: typing.Callable[[MouseEvent], bool]) -> int:
        ...
    @typing.overload
    def unsubscribe_to_action_events(self, arg0: int) -> None:
        ...
    @typing.overload
    def unsubscribe_to_action_events(self, arg0: int) -> None:
        ...
    def unsubscribe_to_gamepad_connection_events(self, arg0: int) -> None:
        ...
    def unsubscribe_to_gamepad_events(self, arg0: Gamepad, arg1: int) -> None:
        ...
    def unsubscribe_to_input_events(self, arg0: int) -> None:
        ...
    def unsubscribe_to_keyboard_events(self, arg0: Keyboard, arg1: int) -> None:
        ...
    def unsubscribe_to_mouse_events(self, arg0: Mouse, arg1: int) -> None:
        ...
class InputDevice:
    @typing.overload
    def __eq__(self, arg0: Keyboard) -> bool:
        ...
    @typing.overload
    def __eq__(self, arg0: Mouse) -> bool:
        ...
    @typing.overload
    def __eq__(self, arg0: Gamepad) -> bool:
        ...
    @typing.overload
    def __eq__(self, arg0: InputDevice) -> bool:
        ...
    def __hash__(self) -> int:
        ...
class InputEvent:
    @property
    def device(self) -> InputDevice:
        ...
    @property
    def deviceType(self) -> DeviceType:
        ...
    @property
    def event(self) -> typing.Any:
        ...
class InputProvider:
    def buffer_gamepad_event(self, arg0: Gamepad, arg1: GamepadInput, arg2: float) -> None:
        ...
    def buffer_keyboard_char_event(self, arg0: Keyboard, arg1: str, arg2: int) -> None:
        ...
    def buffer_keyboard_key_event(self, arg0: Keyboard, arg1: KeyboardEventType, arg2: KeyboardInput, arg3: int) -> None:
        ...
    def buffer_mouse_event(self, arg0: Mouse, arg1: MouseEventType, arg2: carb._carb.Float2, arg3: int, arg4: carb._carb.Float2) -> None:
        ...
    def create_gamepad(self, arg0: str, arg1: str) -> Gamepad:
        ...
    def create_keyboard(self, arg0: str) -> Keyboard:
        ...
    def create_mouse(self, arg0: str) -> Mouse:
        ...
    def destroy_gamepad(self, arg0: Gamepad) -> None:
        ...
    def destroy_keyboard(self, arg0: Keyboard) -> None:
        ...
    def destroy_mouse(self, arg0: Mouse) -> None:
        ...
    def set_gamepad_connected(self, arg0: Gamepad, arg1: bool) -> None:
        ...
    def update_gamepad(self, arg0: Gamepad) -> None:
        ...
    def update_keyboard(self, arg0: Keyboard) -> None:
        ...
    def update_mouse(self, arg0: Mouse) -> None:
        ...
class Keyboard(InputDevice):
    def __hash__(self) -> int:
        ...
class KeyboardEvent:
    @property
    def device(self) -> InputDevice:
        ...
    @property
    def input(self) -> typing.Any:
        ...
    @property
    def keyboard(self) -> Keyboard:
        ...
    @property
    def modifiers(self) -> int:
        ...
    @property
    def type(self) -> KeyboardEventType:
        ...
class KeyboardEventType:
    """
    Members:
    
      KEY_PRESS
    
      KEY_REPEAT
    
      KEY_RELEASE
    
      CHAR
    """
    CHAR: typing.ClassVar[KeyboardEventType]  # value = <KeyboardEventType.CHAR: 3>
    KEY_PRESS: typing.ClassVar[KeyboardEventType]  # value = <KeyboardEventType.KEY_PRESS: 0>
    KEY_RELEASE: typing.ClassVar[KeyboardEventType]  # value = <KeyboardEventType.KEY_RELEASE: 2>
    KEY_REPEAT: typing.ClassVar[KeyboardEventType]  # value = <KeyboardEventType.KEY_REPEAT: 1>
    __members__: typing.ClassVar[dict[str, KeyboardEventType]]  # value = {'KEY_PRESS': <KeyboardEventType.KEY_PRESS: 0>, 'KEY_REPEAT': <KeyboardEventType.KEY_REPEAT: 1>, 'KEY_RELEASE': <KeyboardEventType.KEY_RELEASE: 2>, 'CHAR': <KeyboardEventType.CHAR: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class KeyboardInput:
    """
    Members:
    
      UNKNOWN
    
      SPACE
    
      APOSTROPHE
    
      COMMA
    
      MINUS
    
      PERIOD
    
      SLASH
    
      KEY_0
    
      KEY_1
    
      KEY_2
    
      KEY_3
    
      KEY_4
    
      KEY_5
    
      KEY_6
    
      KEY_7
    
      KEY_8
    
      KEY_9
    
      SEMICOLON
    
      EQUAL
    
      A
    
      B
    
      C
    
      D
    
      E
    
      F
    
      G
    
      H
    
      I
    
      J
    
      K
    
      L
    
      M
    
      N
    
      O
    
      P
    
      Q
    
      R
    
      S
    
      T
    
      U
    
      V
    
      W
    
      X
    
      Y
    
      Z
    
      LEFT_BRACKET
    
      BACKSLASH
    
      RIGHT_BRACKET
    
      GRAVE_ACCENT
    
      ESCAPE
    
      TAB
    
      ENTER
    
      BACKSPACE
    
      INSERT
    
      DEL
    
      RIGHT
    
      LEFT
    
      DOWN
    
      UP
    
      PAGE_UP
    
      PAGE_DOWN
    
      HOME
    
      END
    
      CAPS_LOCK
    
      SCROLL_LOCK
    
      NUM_LOCK
    
      PRINT_SCREEN
    
      PAUSE
    
      F1
    
      F2
    
      F3
    
      F4
    
      F5
    
      F6
    
      F7
    
      F8
    
      F9
    
      F10
    
      F11
    
      F12
    
      NUMPAD_0
    
      NUMPAD_1
    
      NUMPAD_2
    
      NUMPAD_3
    
      NUMPAD_4
    
      NUMPAD_5
    
      NUMPAD_6
    
      NUMPAD_7
    
      NUMPAD_8
    
      NUMPAD_9
    
      NUMPAD_DEL
    
      NUMPAD_DIVIDE
    
      NUMPAD_MULTIPLY
    
      NUMPAD_SUBTRACT
    
      NUMPAD_ADD
    
      NUMPAD_ENTER
    
      NUMPAD_EQUAL
    
      LEFT_SHIFT
    
      LEFT_CONTROL
    
      LEFT_ALT
    
      LEFT_SUPER
    
      RIGHT_SHIFT
    
      RIGHT_CONTROL
    
      RIGHT_ALT
    
      RIGHT_SUPER
    
      MENU
    
      COUNT
    """
    A: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.A: 19>
    APOSTROPHE: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.APOSTROPHE: 2>
    B: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.B: 20>
    BACKSLASH: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.BACKSLASH: 46>
    BACKSPACE: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.BACKSPACE: 52>
    C: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.C: 21>
    CAPS_LOCK: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.CAPS_LOCK: 63>
    COMMA: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.COMMA: 3>
    COUNT: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.COUNT: 106>
    D: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.D: 22>
    DEL: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.DEL: 54>
    DOWN: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.DOWN: 57>
    E: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.E: 23>
    END: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.END: 62>
    ENTER: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.ENTER: 51>
    EQUAL: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.EQUAL: 18>
    ESCAPE: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.ESCAPE: 49>
    F: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.F: 24>
    F1: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.F1: 68>
    F10: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.F10: 77>
    F11: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.F11: 78>
    F12: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.F12: 79>
    F2: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.F2: 69>
    F3: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.F3: 70>
    F4: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.F4: 71>
    F5: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.F5: 72>
    F6: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.F6: 73>
    F7: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.F7: 74>
    F8: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.F8: 75>
    F9: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.F9: 76>
    G: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.G: 25>
    GRAVE_ACCENT: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.GRAVE_ACCENT: 48>
    H: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.H: 26>
    HOME: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.HOME: 61>
    I: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.I: 27>
    INSERT: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.INSERT: 53>
    J: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.J: 28>
    K: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.K: 29>
    KEY_0: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.KEY_0: 7>
    KEY_1: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.KEY_1: 8>
    KEY_2: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.KEY_2: 9>
    KEY_3: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.KEY_3: 10>
    KEY_4: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.KEY_4: 11>
    KEY_5: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.KEY_5: 12>
    KEY_6: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.KEY_6: 13>
    KEY_7: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.KEY_7: 14>
    KEY_8: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.KEY_8: 15>
    KEY_9: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.KEY_9: 16>
    L: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.L: 30>
    LEFT: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.LEFT: 56>
    LEFT_ALT: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.LEFT_ALT: 99>
    LEFT_BRACKET: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.LEFT_BRACKET: 45>
    LEFT_CONTROL: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.LEFT_CONTROL: 98>
    LEFT_SHIFT: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.LEFT_SHIFT: 97>
    LEFT_SUPER: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.LEFT_SUPER: 100>
    M: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.M: 31>
    MENU: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.MENU: 105>
    MINUS: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.MINUS: 4>
    N: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.N: 32>
    NUMPAD_0: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.NUMPAD_0: 80>
    NUMPAD_1: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.NUMPAD_1: 81>
    NUMPAD_2: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.NUMPAD_2: 82>
    NUMPAD_3: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.NUMPAD_3: 83>
    NUMPAD_4: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.NUMPAD_4: 84>
    NUMPAD_5: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.NUMPAD_5: 85>
    NUMPAD_6: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.NUMPAD_6: 86>
    NUMPAD_7: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.NUMPAD_7: 87>
    NUMPAD_8: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.NUMPAD_8: 88>
    NUMPAD_9: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.NUMPAD_9: 89>
    NUMPAD_ADD: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.NUMPAD_ADD: 94>
    NUMPAD_DEL: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.NUMPAD_DEL: 90>
    NUMPAD_DIVIDE: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.NUMPAD_DIVIDE: 91>
    NUMPAD_ENTER: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.NUMPAD_ENTER: 95>
    NUMPAD_EQUAL: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.NUMPAD_EQUAL: 96>
    NUMPAD_MULTIPLY: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.NUMPAD_MULTIPLY: 92>
    NUMPAD_SUBTRACT: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.NUMPAD_SUBTRACT: 93>
    NUM_LOCK: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.NUM_LOCK: 65>
    O: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.O: 33>
    P: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.P: 34>
    PAGE_DOWN: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.PAGE_DOWN: 60>
    PAGE_UP: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.PAGE_UP: 59>
    PAUSE: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.PAUSE: 67>
    PERIOD: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.PERIOD: 5>
    PRINT_SCREEN: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.PRINT_SCREEN: 66>
    Q: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.Q: 35>
    R: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.R: 36>
    RIGHT: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.RIGHT: 55>
    RIGHT_ALT: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.RIGHT_ALT: 103>
    RIGHT_BRACKET: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.RIGHT_BRACKET: 47>
    RIGHT_CONTROL: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.RIGHT_CONTROL: 102>
    RIGHT_SHIFT: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.RIGHT_SHIFT: 101>
    RIGHT_SUPER: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.RIGHT_SUPER: 104>
    S: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.S: 37>
    SCROLL_LOCK: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.SCROLL_LOCK: 64>
    SEMICOLON: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.SEMICOLON: 17>
    SLASH: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.SLASH: 6>
    SPACE: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.SPACE: 1>
    T: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.T: 38>
    TAB: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.TAB: 50>
    U: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.U: 39>
    UNKNOWN: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.UNKNOWN: 0>
    UP: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.UP: 58>
    V: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.V: 40>
    W: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.W: 41>
    X: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.X: 42>
    Y: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.Y: 43>
    Z: typing.ClassVar[KeyboardInput]  # value = <KeyboardInput.Z: 44>
    __members__: typing.ClassVar[dict[str, KeyboardInput]]  # value = {'UNKNOWN': <KeyboardInput.UNKNOWN: 0>, 'SPACE': <KeyboardInput.SPACE: 1>, 'APOSTROPHE': <KeyboardInput.APOSTROPHE: 2>, 'COMMA': <KeyboardInput.COMMA: 3>, 'MINUS': <KeyboardInput.MINUS: 4>, 'PERIOD': <KeyboardInput.PERIOD: 5>, 'SLASH': <KeyboardInput.SLASH: 6>, 'KEY_0': <KeyboardInput.KEY_0: 7>, 'KEY_1': <KeyboardInput.KEY_1: 8>, 'KEY_2': <KeyboardInput.KEY_2: 9>, 'KEY_3': <KeyboardInput.KEY_3: 10>, 'KEY_4': <KeyboardInput.KEY_4: 11>, 'KEY_5': <KeyboardInput.KEY_5: 12>, 'KEY_6': <KeyboardInput.KEY_6: 13>, 'KEY_7': <KeyboardInput.KEY_7: 14>, 'KEY_8': <KeyboardInput.KEY_8: 15>, 'KEY_9': <KeyboardInput.KEY_9: 16>, 'SEMICOLON': <KeyboardInput.SEMICOLON: 17>, 'EQUAL': <KeyboardInput.EQUAL: 18>, 'A': <KeyboardInput.A: 19>, 'B': <KeyboardInput.B: 20>, 'C': <KeyboardInput.C: 21>, 'D': <KeyboardInput.D: 22>, 'E': <KeyboardInput.E: 23>, 'F': <KeyboardInput.F: 24>, 'G': <KeyboardInput.G: 25>, 'H': <KeyboardInput.H: 26>, 'I': <KeyboardInput.I: 27>, 'J': <KeyboardInput.J: 28>, 'K': <KeyboardInput.K: 29>, 'L': <KeyboardInput.L: 30>, 'M': <KeyboardInput.M: 31>, 'N': <KeyboardInput.N: 32>, 'O': <KeyboardInput.O: 33>, 'P': <KeyboardInput.P: 34>, 'Q': <KeyboardInput.Q: 35>, 'R': <KeyboardInput.R: 36>, 'S': <KeyboardInput.S: 37>, 'T': <KeyboardInput.T: 38>, 'U': <KeyboardInput.U: 39>, 'V': <KeyboardInput.V: 40>, 'W': <KeyboardInput.W: 41>, 'X': <KeyboardInput.X: 42>, 'Y': <KeyboardInput.Y: 43>, 'Z': <KeyboardInput.Z: 44>, 'LEFT_BRACKET': <KeyboardInput.LEFT_BRACKET: 45>, 'BACKSLASH': <KeyboardInput.BACKSLASH: 46>, 'RIGHT_BRACKET': <KeyboardInput.RIGHT_BRACKET: 47>, 'GRAVE_ACCENT': <KeyboardInput.GRAVE_ACCENT: 48>, 'ESCAPE': <KeyboardInput.ESCAPE: 49>, 'TAB': <KeyboardInput.TAB: 50>, 'ENTER': <KeyboardInput.ENTER: 51>, 'BACKSPACE': <KeyboardInput.BACKSPACE: 52>, 'INSERT': <KeyboardInput.INSERT: 53>, 'DEL': <KeyboardInput.DEL: 54>, 'RIGHT': <KeyboardInput.RIGHT: 55>, 'LEFT': <KeyboardInput.LEFT: 56>, 'DOWN': <KeyboardInput.DOWN: 57>, 'UP': <KeyboardInput.UP: 58>, 'PAGE_UP': <KeyboardInput.PAGE_UP: 59>, 'PAGE_DOWN': <KeyboardInput.PAGE_DOWN: 60>, 'HOME': <KeyboardInput.HOME: 61>, 'END': <KeyboardInput.END: 62>, 'CAPS_LOCK': <KeyboardInput.CAPS_LOCK: 63>, 'SCROLL_LOCK': <KeyboardInput.SCROLL_LOCK: 64>, 'NUM_LOCK': <KeyboardInput.NUM_LOCK: 65>, 'PRINT_SCREEN': <KeyboardInput.PRINT_SCREEN: 66>, 'PAUSE': <KeyboardInput.PAUSE: 67>, 'F1': <KeyboardInput.F1: 68>, 'F2': <KeyboardInput.F2: 69>, 'F3': <KeyboardInput.F3: 70>, 'F4': <KeyboardInput.F4: 71>, 'F5': <KeyboardInput.F5: 72>, 'F6': <KeyboardInput.F6: 73>, 'F7': <KeyboardInput.F7: 74>, 'F8': <KeyboardInput.F8: 75>, 'F9': <KeyboardInput.F9: 76>, 'F10': <KeyboardInput.F10: 77>, 'F11': <KeyboardInput.F11: 78>, 'F12': <KeyboardInput.F12: 79>, 'NUMPAD_0': <KeyboardInput.NUMPAD_0: 80>, 'NUMPAD_1': <KeyboardInput.NUMPAD_1: 81>, 'NUMPAD_2': <KeyboardInput.NUMPAD_2: 82>, 'NUMPAD_3': <KeyboardInput.NUMPAD_3: 83>, 'NUMPAD_4': <KeyboardInput.NUMPAD_4: 84>, 'NUMPAD_5': <KeyboardInput.NUMPAD_5: 85>, 'NUMPAD_6': <KeyboardInput.NUMPAD_6: 86>, 'NUMPAD_7': <KeyboardInput.NUMPAD_7: 87>, 'NUMPAD_8': <KeyboardInput.NUMPAD_8: 88>, 'NUMPAD_9': <KeyboardInput.NUMPAD_9: 89>, 'NUMPAD_DEL': <KeyboardInput.NUMPAD_DEL: 90>, 'NUMPAD_DIVIDE': <KeyboardInput.NUMPAD_DIVIDE: 91>, 'NUMPAD_MULTIPLY': <KeyboardInput.NUMPAD_MULTIPLY: 92>, 'NUMPAD_SUBTRACT': <KeyboardInput.NUMPAD_SUBTRACT: 93>, 'NUMPAD_ADD': <KeyboardInput.NUMPAD_ADD: 94>, 'NUMPAD_ENTER': <KeyboardInput.NUMPAD_ENTER: 95>, 'NUMPAD_EQUAL': <KeyboardInput.NUMPAD_EQUAL: 96>, 'LEFT_SHIFT': <KeyboardInput.LEFT_SHIFT: 97>, 'LEFT_CONTROL': <KeyboardInput.LEFT_CONTROL: 98>, 'LEFT_ALT': <KeyboardInput.LEFT_ALT: 99>, 'LEFT_SUPER': <KeyboardInput.LEFT_SUPER: 100>, 'RIGHT_SHIFT': <KeyboardInput.RIGHT_SHIFT: 101>, 'RIGHT_CONTROL': <KeyboardInput.RIGHT_CONTROL: 102>, 'RIGHT_ALT': <KeyboardInput.RIGHT_ALT: 103>, 'RIGHT_SUPER': <KeyboardInput.RIGHT_SUPER: 104>, 'MENU': <KeyboardInput.MENU: 105>, 'COUNT': <KeyboardInput.COUNT: 106>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Mouse(InputDevice):
    def __hash__(self) -> int:
        ...
class MouseEvent:
    @property
    def device(self) -> InputDevice:
        ...
    @property
    def modifiers(self) -> int:
        ...
    @property
    def mouse(self) -> Mouse:
        ...
    @property
    def normalized_coords(self) -> carb._carb.Float2:
        ...
    @property
    def pixel_coords(self) -> carb._carb.Float2:
        ...
    @property
    def scrollDelta(self) -> carb._carb.Float2:
        ...
    @property
    def type(self) -> MouseEventType:
        ...
class MouseEventType:
    """
    Members:
    
      LEFT_BUTTON_DOWN
    
      LEFT_BUTTON_UP
    
      MIDDLE_BUTTON_DOWN
    
      MIDDLE_BUTTON_UP
    
      RIGHT_BUTTON_DOWN
    
      RIGHT_BUTTON_UP
    
      MOVE
    
      SCROLL
    """
    LEFT_BUTTON_DOWN: typing.ClassVar[MouseEventType]  # value = <MouseEventType.LEFT_BUTTON_DOWN: 0>
    LEFT_BUTTON_UP: typing.ClassVar[MouseEventType]  # value = <MouseEventType.LEFT_BUTTON_UP: 1>
    MIDDLE_BUTTON_DOWN: typing.ClassVar[MouseEventType]  # value = <MouseEventType.MIDDLE_BUTTON_DOWN: 2>
    MIDDLE_BUTTON_UP: typing.ClassVar[MouseEventType]  # value = <MouseEventType.MIDDLE_BUTTON_UP: 3>
    MOVE: typing.ClassVar[MouseEventType]  # value = <MouseEventType.MOVE: 6>
    RIGHT_BUTTON_DOWN: typing.ClassVar[MouseEventType]  # value = <MouseEventType.RIGHT_BUTTON_DOWN: 4>
    RIGHT_BUTTON_UP: typing.ClassVar[MouseEventType]  # value = <MouseEventType.RIGHT_BUTTON_UP: 5>
    SCROLL: typing.ClassVar[MouseEventType]  # value = <MouseEventType.SCROLL: 7>
    __members__: typing.ClassVar[dict[str, MouseEventType]]  # value = {'LEFT_BUTTON_DOWN': <MouseEventType.LEFT_BUTTON_DOWN: 0>, 'LEFT_BUTTON_UP': <MouseEventType.LEFT_BUTTON_UP: 1>, 'MIDDLE_BUTTON_DOWN': <MouseEventType.MIDDLE_BUTTON_DOWN: 2>, 'MIDDLE_BUTTON_UP': <MouseEventType.MIDDLE_BUTTON_UP: 3>, 'RIGHT_BUTTON_DOWN': <MouseEventType.RIGHT_BUTTON_DOWN: 4>, 'RIGHT_BUTTON_UP': <MouseEventType.RIGHT_BUTTON_UP: 5>, 'MOVE': <MouseEventType.MOVE: 6>, 'SCROLL': <MouseEventType.SCROLL: 7>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class MouseInput:
    """
    Members:
    
      LEFT_BUTTON
    
      RIGHT_BUTTON
    
      MIDDLE_BUTTON
    
      FORWARD_BUTTON
    
      BACK_BUTTON
    
      SCROLL_RIGHT
    
      SCROLL_LEFT
    
      SCROLL_UP
    
      SCROLL_DOWN
    
      MOVE_RIGHT
    
      MOVE_LEFT
    
      MOVE_UP
    
      MOVE_DOWN
    
      COUNT
    """
    BACK_BUTTON: typing.ClassVar[MouseInput]  # value = <MouseInput.BACK_BUTTON: 4>
    COUNT: typing.ClassVar[MouseInput]  # value = <MouseInput.COUNT: 13>
    FORWARD_BUTTON: typing.ClassVar[MouseInput]  # value = <MouseInput.FORWARD_BUTTON: 3>
    LEFT_BUTTON: typing.ClassVar[MouseInput]  # value = <MouseInput.LEFT_BUTTON: 0>
    MIDDLE_BUTTON: typing.ClassVar[MouseInput]  # value = <MouseInput.MIDDLE_BUTTON: 2>
    MOVE_DOWN: typing.ClassVar[MouseInput]  # value = <MouseInput.MOVE_DOWN: 12>
    MOVE_LEFT: typing.ClassVar[MouseInput]  # value = <MouseInput.MOVE_LEFT: 10>
    MOVE_RIGHT: typing.ClassVar[MouseInput]  # value = <MouseInput.MOVE_RIGHT: 9>
    MOVE_UP: typing.ClassVar[MouseInput]  # value = <MouseInput.MOVE_UP: 11>
    RIGHT_BUTTON: typing.ClassVar[MouseInput]  # value = <MouseInput.RIGHT_BUTTON: 1>
    SCROLL_DOWN: typing.ClassVar[MouseInput]  # value = <MouseInput.SCROLL_DOWN: 8>
    SCROLL_LEFT: typing.ClassVar[MouseInput]  # value = <MouseInput.SCROLL_LEFT: 6>
    SCROLL_RIGHT: typing.ClassVar[MouseInput]  # value = <MouseInput.SCROLL_RIGHT: 5>
    SCROLL_UP: typing.ClassVar[MouseInput]  # value = <MouseInput.SCROLL_UP: 7>
    __members__: typing.ClassVar[dict[str, MouseInput]]  # value = {'LEFT_BUTTON': <MouseInput.LEFT_BUTTON: 0>, 'RIGHT_BUTTON': <MouseInput.RIGHT_BUTTON: 1>, 'MIDDLE_BUTTON': <MouseInput.MIDDLE_BUTTON: 2>, 'FORWARD_BUTTON': <MouseInput.FORWARD_BUTTON: 3>, 'BACK_BUTTON': <MouseInput.BACK_BUTTON: 4>, 'SCROLL_RIGHT': <MouseInput.SCROLL_RIGHT: 5>, 'SCROLL_LEFT': <MouseInput.SCROLL_LEFT: 6>, 'SCROLL_UP': <MouseInput.SCROLL_UP: 7>, 'SCROLL_DOWN': <MouseInput.SCROLL_DOWN: 8>, 'MOVE_RIGHT': <MouseInput.MOVE_RIGHT: 9>, 'MOVE_LEFT': <MouseInput.MOVE_LEFT: 10>, 'MOVE_UP': <MouseInput.MOVE_UP: 11>, 'MOVE_DOWN': <MouseInput.MOVE_DOWN: 12>, 'COUNT': <MouseInput.COUNT: 13>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
def acquire_input_interface(plugin_name: str = None, library_path: str = None) -> IInput:
    ...
def acquire_input_provider(plugin_name: str = None, library_path: str = None) -> ...:
    ...
def get_action_mapping_desc_from_string(arg0: str) -> ActionMappingDesc:
    ...
@typing.overload
def get_string_from_action_mapping_desc(arg0: KeyboardInput, arg1: int) -> str:
    ...
@typing.overload
def get_string_from_action_mapping_desc(arg0: MouseInput, arg1: int) -> str:
    ...
@typing.overload
def get_string_from_action_mapping_desc(arg0: GamepadInput) -> str:
    ...
BUTTON_FLAG_DOWN: int = 8
BUTTON_FLAG_PRESSED: int = 4
BUTTON_FLAG_RELEASED: int = 1
BUTTON_FLAG_UP: int = 2
EVENT_TYPE_ALL: int = 4294967295
KEYBOARD_MODIFIER_FLAG_ALT: int = 4
KEYBOARD_MODIFIER_FLAG_CAPS_LOCK: int = 16
KEYBOARD_MODIFIER_FLAG_CONTROL: int = 2
KEYBOARD_MODIFIER_FLAG_NUM_LOCK: int = 32
KEYBOARD_MODIFIER_FLAG_SHIFT: int = 1
KEYBOARD_MODIFIER_FLAG_SUPER: int = 8
SUBSCRIPTION_ORDER_DEFAULT: int = -1
SUBSCRIPTION_ORDER_FIRST: int = 0
SUBSCRIPTION_ORDER_LAST: int = -1
