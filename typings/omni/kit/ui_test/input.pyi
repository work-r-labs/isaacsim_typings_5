from __future__ import annotations
import carb as carb
from carb.input import KeyboardEventType
from carb.input import KeyboardInput
from carb.input import MouseEventType
from functools import lru_cache
from itertools import chain
import logging as logging
import omni as omni
from omni.kit.ui_test.common import human_delay
from omni.kit.ui_test.common import wait_n_updates_internal
from omni.kit.ui_test.vec2 import Vec2
from omni import ui
__all__ = ['KeyDownScope', 'KeyboardEventType', 'KeyboardInput', 'MODIFIERS_MAP', 'MODIFIERS_TO_KEY', 'MouseEventType', 'Vec2', 'carb', 'chain', 'emulate_char_press', 'emulate_key_combo', 'emulate_keyboard', 'emulate_keyboard_press', 'emulate_mouse', 'emulate_mouse_click', 'emulate_mouse_drag_and_drop', 'emulate_mouse_move', 'emulate_mouse_move_and_click', 'emulate_mouse_scroll', 'emulate_mouse_slow_move', 'human_delay', 'logger', 'logging', 'lru_cache', 'omni', 'ui', 'wait_n_updates_internal']
class KeyDownScope:
    def __aenter__(self):
        ...
    def __aexit__(self, exc_type, exc, tb):
        ...
    def __init__(self, key: carb.input.KeyboardInput, modifier: carb.input.KeyboardInput = 0, human_delay_speed: int = 2):
        ...
def _get_input_provider(*args, **kwargs):
    ...
def _get_windowing(*args, **kwargs):
    ...
def emulate_char_press(chars: str, delay_every_n_symbols: int = 20, human_delay_speed: int = 2):
    """
    Emulate Keyboard char input. Type N chars immediately and do a delay, then continue.
    """
def emulate_key_combo(combo: str, human_delay_speed: int = 2):
    """
    Emulate Keyboard key combination.
    
        Parse string of keys separated by '+' sign and treat as a key combo to emulate.
    
        Examples: "CTRL+ENTER", "SHIFT+ALT+Y", "Z"
        
    """
def emulate_keyboard(event_type: carb.input.KeyboardEventType, key: carb.input.KeyboardInput, modifier: carb.input.KeyboardInput = 0):
    ...
def emulate_keyboard_press(key: carb.input.KeyboardInput, modifier: carb.input.KeyboardInput = 0, human_delay_speed: int = 2):
    """
    Emulate Keyboard key press. Down and up.
    """
def emulate_mouse(event_type: carb.input.MouseEventType, pos: omni.kit.ui_test.vec2.Vec2 = ..., modifiers: int | None = None):
    ...
def emulate_mouse_click(right_click = False, double = False, modifiers: int | None = None):
    """
    Emulate Mouse single or double click.
    """
def emulate_mouse_drag_and_drop(start_pos, end_pos, right_click = False, human_delay_speed: int = 4):
    """
    Emulate Mouse Drag & Drop. Click at start position and slowly move to end position.
    """
def emulate_mouse_move(pos: omni.kit.ui_test.vec2.Vec2, human_delay_speed: int = 2):
    """
    Emulate Mouse move into position.
    """
def emulate_mouse_move_and_click(pos: omni.kit.ui_test.vec2.Vec2, right_click = False, double = False, human_delay_speed: int = 2):
    """
    Emulate Mouse move into position and click.
    """
def emulate_mouse_scroll(delta: omni.kit.ui_test.vec2.Vec2, human_delay_speed: int = 2):
    """
    Emulate Mouse scroll by delta.
    """
def emulate_mouse_slow_move(start_pos, end_pos, num_steps = 8, human_delay_speed: int = 4):
    """
    Emulate Mouse slow move. Mouse is moved in steps between start and end with the human delay between each step.
    """
MODIFIERS_MAP: dict  # value = {'CTRL': (<KeyboardInput.LEFT_CONTROL: 98>, 2), 'CONTROL': (<KeyboardInput.LEFT_CONTROL: 98>, 2), 'SHIFT': (<KeyboardInput.LEFT_SHIFT: 97>, 1), 'ALT': (<KeyboardInput.LEFT_ALT: 99>, 4)}
MODIFIERS_TO_KEY: dict  # value = {2: <KeyboardInput.LEFT_CONTROL: 98>, 1: <KeyboardInput.LEFT_SHIFT: 97>, 4: <KeyboardInput.LEFT_ALT: 99>}
logger: logging.Logger  # value = <Logger omni.kit.ui_test.input (DEBUG)>
