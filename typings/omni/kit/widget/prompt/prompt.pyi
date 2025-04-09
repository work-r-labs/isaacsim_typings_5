from __future__ import annotations
import carb as carb
import omni as omni
import typing
import uuid as uuid
__all__ = ['Prompt', 'PromptButtonInfo', 'PromptManager', 'carb', 'omni', 'uuid']
class Prompt:
    """
    Pop up a prompt window that asks the user a simple question with up to four buttons for answers.
    
        Callbacks are executed for each button press, as well as when the window is closed manually.
        
    """
    def __del__(self):
        ...
    def __enter__(self):
        """
        Called on entering a 'with' loop
        """
    def __exit__(self, type, value, trace):
        """
        Called on exiting a 'with' loop
        """
    def __init__(self, title, text, ok_button_text = 'OK', cancel_button_text = None, middle_button_text = None, middle_2_button_text = None, ok_button_fn = None, cancel_button_fn = None, middle_button_fn = None, middle_2_button_fn = None, modal = False, on_closed_fn = None, shortcut_keys = True, no_title_bar = False, width = None, height = None, callback_addons: typing.List = list()):
        """
        Initialize the callbacks and window information
        
                Args:
                    title (str): Text appearing in the titlebar of the window.
                    text (str): Text of the question being posed to the user.
                    ok_button_text (str): Text for the first button.
                    cancel_button_text (str): Text for the last button.
                    middle_button_text (str): Text for the middle button.
                    middle_button_2_text (str): Text for the second middle button.
                    ok_button_fn (Callable[[], None]): Function executed when the first button is pressed.The function signature is:
                        void on_button_clicked_fn(). Defaults to None.
                    cancel_button_fn (Callable[[], None]):: Function executed when the last button is pressed.The function signature is:
                        void on_button_clicked_fn(). Defaults to None.
                    middle_button_fn (Callable[[], None]):: Function executed when the middle button is pressed.The function signature is:
                        void on_button_clicked_fn(). Defaults to None.
                    middle_2_button_fn (Callable[[], None]):: Function executed when the second middle button is pressed.The function signature is:
                        void on_button_clicked_fn(). Defaults to None.
                    modal (bool): True if the window is modal, shutting down other UI until an answer is received
                    on_closed_fn (Callable[[], None]):: Function executed when the window is closed without hitting a button.The function signature is:
                        void on_button_clicked_fn(). Defaults to None.
                    shortcut_keys (bool): If it can be confirmed or hidden with shortcut keys like Enter or ESC. Defaults to True.
                    no_title_bar (bool): If it needs to show title bar. Defaults to True.
                    width (int): The specified width. By default, it will use the computed width.
                    height (int): The specified height. By default, it will use the computed height.
                    callback_addons (List): Addon widgets which is appended in the prompt window. By default, it is empty.
                
        """
    def _build_ui(self):
        """
        Construct the window based on the current parameters
        """
    def _on_cancel_button_fn(self):
        """
        Callback executed when the third (cancel) button is pressed
        """
    def _on_closed_fn(self):
        """
        Callback executed when the window is closed without pressing a button
        """
    def _on_key_pressed_fn(self, key, mod, pressed):
        ...
    def _on_middle_2_button_fn(self):
        ...
    def _on_middle_button_fn(self):
        """
        Callback executed when the second (middle) button is pressed
        """
    def _on_ok_button_fn(self):
        """
        Callback executed when the first (okay) button is pressed
        """
    def _on_visibility_changed(self, new_visibility: bool):
        """
        Callback executed when visibility of the window closes
        """
    def destroy(self):
        """
         Destructor. 
        """
    def hide(self):
        """
        Make the prompt window invisible
        """
    def is_visible(self) -> bool:
        """
        
                Returns True if the prompt is currently visible.
                
                Returns:
                    bool
                
        """
    def set_cancel_fn(self, on_cancel_button_clicked):
        """
        Define a new callback for when the third (cancel) button is clicked
        """
    def set_confirm_fn(self, on_ok_button_clicked):
        """
        Define a new callback for when the first (okay) button is clicked
        """
    def set_middle_2_button_fn(self, on_middle_2_button_clicked):
        """
        Define a new callback for when the second (middle) button is clicked
        """
    def set_middle_button_fn(self, on_middle_button_clicked):
        """
        Define a new callback for when the second (middle) button is clicked
        """
    def set_on_closed_fn(self, on_on_closed):
        """
        Define a new callback for when the window is closed without pressing a button
        """
    def set_text(self, text):
        """
        Set a new question label
        """
    def show(self):
        """
        Make the prompt window visible
        """
    @property
    def visible(self):
        """
        
                Get the prompt's visible stat.
        
                Returns:
                    bool: True is prompt is visible else False.
                
        """
    @visible.setter
    def visible(self, value: bool):
        """
        
                Get the prompt's visible stat.
        
                Args:
                    value (bool): True to show prompt, False to hide.
                
        """
class PromptButtonInfo:
    """
     Prompt button's information
    """
    def __init__(self, name: str, on_button_clicked_fn: typing.Callable[[], NoneType] = None):
        """
        
                Construtor.
        
                Args:
                    name (str): The button's name.
                    on_button_clicked_fn (Callable[[], None], optional): Function executed when this button clicked. The function signature is:
                        void on_button_clicked_fn(). Defaults to None.
                
        """
    @property
    def name(self) -> str:
        """
        
                Get the button's name.
        
                Returns:
                    str: Name of the button.
                
        """
    @property
    def on_button_clicked_fn(self) -> typing.Callable[[], NoneType]:
        """
        
                Get the button clicked function.
        
                Returns:
                    Callable[[], None]: Function executed when this button clicked. The function signature is:
                        void on_button_clicked_fn()
                
        """
class PromptManager:
    """
     Prompt Manager 
    """
    _prompts: typing.ClassVar[set] = set()
    @staticmethod
    def add_prompt(prompt: Prompt):
        """
        
                Add the prompt to mananger.
        
                Args:
                    prompt (:obj:'Prompt'): Prompt to add.
                
        """
    @staticmethod
    def on_shutdown():
        """
        Remove all the prompts when shut down
        """
    @staticmethod
    def on_startup():
        ...
    @staticmethod
    def post_simple_prompt(title: str, message: str, ok_button_info: PromptButtonInfo = ..., cancel_button_info: PromptButtonInfo = None, middle_button_info: PromptButtonInfo = None, middle_2_button_info: PromptButtonInfo = None, on_window_closed_fn: typing.Callable[[], NoneType] = None, modal = True, shortcut_keys = True, standalone = True, no_title_bar = False, width = None, height = None, callback_addons: typing.List = list()):
        """
        
                Post a simple prompt with given param. 
                Note: When standalone is true, it will hide all other managed prompts in this manager.
        
                Args:
                    title (str): Text appearing in the titlebar of the window.
                    message (str): Message being posed to the user.
                    ok_button_info (:obj:'PromptButtonInfo'): Information for the ok button.
                    cancel_button_info (:obj:'PromptButtonInfo'): Information for the last button.
                    middle_button_info (:obj:'PromptButtonInfo'): Information for the middle button.
                    middle_2_button_info (:obj:'PromptButtonInfo'): Information for the second middle button.
                    on_window_closed_fn (Callable[[], None]): Function executed when the window is closed.The function signature is:
                        void on_button_clicked_fn(). Defaults to None.
                    modal (bool): True if the window is modal, shutting down other UI until an answer is received
                    shortcut_keys (bool): If it can be confirmed or hidden with shortcut keys like Enter or ESC. Defaults to True.
                    no_title_bar (bool): If it needs to show title bar. Defaults to True.
                    width (int): The specified width. By default, it will use the computed width.
                    height (int): The specified height. By default, it will use the computed height.
                    callback_addons (List): Addon widgets which is appended in the prompt window. By default, it is empty.
                
        """
    @staticmethod
    def query_prompt_by_title(title: str):
        """
        
                Query the prompt by tiyle.
        
                Args:
                    title (str): Prompt to query.
                
                Returns:
                    prompt (:obj:'Prompt'): Prompt with the title in manager.
                
        """
    @staticmethod
    def remove_prompt(prompt: Prompt):
        """
        
                Remove the prompt from mananger.
        
                Args:
                    prompt (:obj:'Prompt'): Prompt to be remove.
                
        """
