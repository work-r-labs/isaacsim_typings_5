from __future__ import annotations
import carb as carb
import re as re
__all__: list = ['KeyCombination']
class KeyCombination:
    """
    
        Key binding class.
        
    """
    @staticmethod
    def from_string(key_string: str) -> typing.Tuple[carb.input.KeyboardInput, int, bool]:
        """
        
                Get key binding information from a string.
        
                Args:
                    key_string (str): String represent a key binding.
        
                Returns:
                    Tuple of carb.input.KeyboardInput, modifiers and flag for press/release.
                
        """
    @staticmethod
    def is_valid_key_string(key: str) -> bool:
        """
        
                If key string valid.
        
                Args:
                    key (str): Key string to check.
        
                Returns:
                    True if key string is valid. Otherwise False.
                
        """
    def __eq__(self, other) -> bool:
        ...
    def __hash__(self):
        ...
    def __init__(self, key: typing.Union[str, carb.input.KeyboardInput], modifiers: int = 0, trigger_press: bool = True):
        """
        
                Create a key binding object.
        
                Args:
                    key (Union[str, carb.input.KeyboardInput]): could be string or carb.input.KeyboardInput.
                        if string, use "+" to join carb.input.KeyboardInput and modifiers, for example: "CTRL+D" or "CTRL+SHIFT+D"
        
                Keyword Args:
                    modifiers (int): Represent combination of keyboard modifier flags, which could be:
                        carb.input.KEYBOARD_MODIFIER_FLAG_CONTROL
                        carb.input.KEYBOARD_MODIFIER_FLAG_SHIFT
                        carb.input.KEYBOARD_MODIFIER_FLAG_ALT
                        carb.input.KEYBOARD_MODIFIER_FLAG_SUPER
        
                    trigger_press (bool): Trigger when key pressed if True. Otherwise trigger when key released. Default True.
                
        """
    def __repr__(self) -> str:
        ...
    @property
    def as_string(self) -> str:
        """
        
                Get string to describe key combination
                
        """
    @property
    def id(self) -> str:
        """
        
                Identifier string of this key binding object.
                
        """
    @property
    def is_valid(self) -> bool:
        """
        
                If a valid key binding object.
                
        """
PREDEFINED_STRING_TO_KEYS: dict  # value = {'UNKNOWN': <KeyboardInput.UNKNOWN: 0>, 'SPACE': <KeyboardInput.SPACE: 1>, 'APOSTROPHE': <KeyboardInput.APOSTROPHE: 2>, 'COMMA': <KeyboardInput.COMMA: 3>, 'MINUS': <KeyboardInput.MINUS: 4>, 'PERIOD': <KeyboardInput.PERIOD: 5>, 'SLASH': <KeyboardInput.SLASH: 6>, 'KEY_0': <KeyboardInput.KEY_0: 7>, 'KEY_1': <KeyboardInput.KEY_1: 8>, 'KEY_2': <KeyboardInput.KEY_2: 9>, 'KEY_3': <KeyboardInput.KEY_3: 10>, 'KEY_4': <KeyboardInput.KEY_4: 11>, 'KEY_5': <KeyboardInput.KEY_5: 12>, 'KEY_6': <KeyboardInput.KEY_6: 13>, 'KEY_7': <KeyboardInput.KEY_7: 14>, 'KEY_8': <KeyboardInput.KEY_8: 15>, 'KEY_9': <KeyboardInput.KEY_9: 16>, 'SEMICOLON': <KeyboardInput.SEMICOLON: 17>, 'EQUAL': <KeyboardInput.EQUAL: 18>, 'A': <KeyboardInput.A: 19>, 'B': <KeyboardInput.B: 20>, 'C': <KeyboardInput.C: 21>, 'D': <KeyboardInput.D: 22>, 'E': <KeyboardInput.E: 23>, 'F': <KeyboardInput.F: 24>, 'G': <KeyboardInput.G: 25>, 'H': <KeyboardInput.H: 26>, 'I': <KeyboardInput.I: 27>, 'J': <KeyboardInput.J: 28>, 'K': <KeyboardInput.K: 29>, 'L': <KeyboardInput.L: 30>, 'M': <KeyboardInput.M: 31>, 'N': <KeyboardInput.N: 32>, 'O': <KeyboardInput.O: 33>, 'P': <KeyboardInput.P: 34>, 'Q': <KeyboardInput.Q: 35>, 'R': <KeyboardInput.R: 36>, 'S': <KeyboardInput.S: 37>, 'T': <KeyboardInput.T: 38>, 'U': <KeyboardInput.U: 39>, 'V': <KeyboardInput.V: 40>, 'W': <KeyboardInput.W: 41>, 'X': <KeyboardInput.X: 42>, 'Y': <KeyboardInput.Y: 43>, 'Z': <KeyboardInput.Z: 44>, 'LEFT_BRACKET': <KeyboardInput.LEFT_BRACKET: 45>, 'BACKSLASH': <KeyboardInput.BACKSLASH: 46>, 'RIGHT_BRACKET': <KeyboardInput.RIGHT_BRACKET: 47>, 'GRAVE_ACCENT': <KeyboardInput.GRAVE_ACCENT: 48>, 'ESCAPE': <KeyboardInput.ESCAPE: 49>, 'TAB': <KeyboardInput.TAB: 50>, 'ENTER': <KeyboardInput.ENTER: 51>, 'BACKSPACE': <KeyboardInput.BACKSPACE: 52>, 'INSERT': <KeyboardInput.INSERT: 53>, 'DEL': <KeyboardInput.DEL: 54>, 'RIGHT': <KeyboardInput.RIGHT: 55>, 'LEFT': <KeyboardInput.LEFT: 56>, 'DOWN': <KeyboardInput.DOWN: 57>, 'UP': <KeyboardInput.UP: 58>, 'PAGE_UP': <KeyboardInput.PAGE_UP: 59>, 'PAGE_DOWN': <KeyboardInput.PAGE_DOWN: 60>, 'HOME': <KeyboardInput.HOME: 61>, 'END': <KeyboardInput.END: 62>, 'CAPS_LOCK': <KeyboardInput.CAPS_LOCK: 63>, 'SCROLL_LOCK': <KeyboardInput.SCROLL_LOCK: 64>, 'NUM_LOCK': <KeyboardInput.NUM_LOCK: 65>, 'PRINT_SCREEN': <KeyboardInput.PRINT_SCREEN: 66>, 'PAUSE': <KeyboardInput.PAUSE: 67>, 'F1': <KeyboardInput.F1: 68>, 'F2': <KeyboardInput.F2: 69>, 'F3': <KeyboardInput.F3: 70>, 'F4': <KeyboardInput.F4: 71>, 'F5': <KeyboardInput.F5: 72>, 'F6': <KeyboardInput.F6: 73>, 'F7': <KeyboardInput.F7: 74>, 'F8': <KeyboardInput.F8: 75>, 'F9': <KeyboardInput.F9: 76>, 'F10': <KeyboardInput.F10: 77>, 'F11': <KeyboardInput.F11: 78>, 'F12': <KeyboardInput.F12: 79>, 'NUMPAD_0': <KeyboardInput.NUMPAD_0: 80>, 'NUMPAD_1': <KeyboardInput.NUMPAD_1: 81>, 'NUMPAD_2': <KeyboardInput.NUMPAD_2: 82>, 'NUMPAD_3': <KeyboardInput.NUMPAD_3: 83>, 'NUMPAD_4': <KeyboardInput.NUMPAD_4: 84>, 'NUMPAD_5': <KeyboardInput.NUMPAD_5: 85>, 'NUMPAD_6': <KeyboardInput.NUMPAD_6: 86>, 'NUMPAD_7': <KeyboardInput.NUMPAD_7: 87>, 'NUMPAD_8': <KeyboardInput.NUMPAD_8: 88>, 'NUMPAD_9': <KeyboardInput.NUMPAD_9: 89>, 'NUMPAD_DEL': <KeyboardInput.NUMPAD_DEL: 90>, 'NUMPAD_DIVIDE': <KeyboardInput.NUMPAD_DIVIDE: 91>, 'NUMPAD_MULTIPLY': <KeyboardInput.NUMPAD_MULTIPLY: 92>, 'NUMPAD_SUBTRACT': <KeyboardInput.NUMPAD_SUBTRACT: 93>, 'NUMPAD_ADD': <KeyboardInput.NUMPAD_ADD: 94>, 'NUMPAD_ENTER': <KeyboardInput.NUMPAD_ENTER: 95>, 'NUMPAD_EQUAL': <KeyboardInput.NUMPAD_EQUAL: 96>, 'LEFT_SHIFT': <KeyboardInput.LEFT_SHIFT: 97>, 'LEFT_CONTROL': <KeyboardInput.LEFT_CONTROL: 98>, 'LEFT_ALT': <KeyboardInput.LEFT_ALT: 99>, 'LEFT_SUPER': <KeyboardInput.LEFT_SUPER: 100>, 'RIGHT_SHIFT': <KeyboardInput.RIGHT_SHIFT: 101>, 'RIGHT_CONTROL': <KeyboardInput.RIGHT_CONTROL: 102>, 'RIGHT_ALT': <KeyboardInput.RIGHT_ALT: 103>, 'RIGHT_SUPER': <KeyboardInput.RIGHT_SUPER: 104>, 'MENU': <KeyboardInput.MENU: 105>, 'COUNT': <KeyboardInput.COUNT: 106>}
