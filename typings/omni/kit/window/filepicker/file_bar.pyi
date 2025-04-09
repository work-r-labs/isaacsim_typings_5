from __future__ import annotations
from functools import partial
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
from omni.kit.window.filepicker.style import get_style
from omni import ui
import pathlib
__all__: list = ['ComboBoxMenu', 'ComboBox', 'FileBar']
class ComboBox:
    def __init__(self, options: typing.List, **kwargs):
        """
        
                Initialize the menu.
        
                Args:
                    options(List): List of options to show in combo box
                
        """
    def _build_ui(self, menu_options: typing.List):
        ...
    def _on_selection_changed(self, option: int):
        ...
    def get_selection_as_string(self, selection: int) -> str:
        """
        
                Returns the string corresponding to the selection.
        
                Args:
                    selection(int): Index of the currently selected menu option
        
                Returns:
                    str: String representation of the selected menu option or none
                
        """
    def show_menu(self):
        """
         Show the menu for the combobox. 
        """
    @property
    def selection(self) -> int:
        """
        
                Gets the selection of this combobox.
        
                Returns:
                    int: Index of the currently selected menu option
                
        """
class ComboBoxMenu:
    def __init__(self, menu_options: typing.List, **kwargs):
        """
        
                 Initialize the menu.
        
                 Args:
                      menu_options(List): List of menu options to be used
                
        """
    def _build_ui(self, menu_options: typing.List):
        ...
    def _frame_build_fn(self, menu_options: typing.List):
        ...
    def hide(self):
        """
        
                Hides the window.
                
        """
    def show(self, offset_x: int = 0, offset_y: int = 0):
        """
        
                Show the window. It will be positioned relative to the parent window.
        
                Keyword Args:
                    offset_x(int): Offset in x direction. Default is 0.
                    offset_y(int): Offset in y direction. Default is 0
                
        """
class FileBar:
    def __init__(self, **kwargs):
        """
        
                Initialize the FileBar.
                
        """
    def _build_filter_combo_box(self) -> omni.ui._ui.ComboBox:
        ...
    def _build_ui(self):
        ...
    def _on_apply(self):
        ...
    def _on_cancel(self):
        ...
    def _on_filename_changed(self, search_words) -> bool:
        ...
    def _on_menu_selection_changed(self, model: typing.Optional[omni.ui._ui.AbstractItemModel] = None):
        ...
    def destroy(self):
        """
         Destroy the widget. 
        """
    def enable_apply_button(self, enable: bool = True):
        """
        
                Enable/disable the apply button for FileBar.
        
                Args:
                    enable (bool): enable or disable the apply button.
                
        """
    def focus_filename_input(self):
        """
        Utility to help focusing the filename input field.
        """
    def set_click_apply_handler(self, click_apply_handler: typing.Callable[[str, str], NoneType]):
        """
        
                Sets the function to execute upon clicking apply.
        
                Args:
                    click_apply_handler (Callable): Callback with filename being the name of the file, and dirname being the containing directory path with an ending slash.
                        Signature is fn(filename: str, dirname: str) -> None
        
                
        """
    def set_extension(self, extension: str):
        """
        
                Set the extension to be used for the file selection.
        
                Args:
                    extension(str): extension of the file to be select.
                
        """
    def set_postfix(self, postfix: str):
        """
        
                Set the postfix to be used for the menu.
        
                Args:
                    postfix(str): postfix of the file to be select.
                
        """
    @property
    def current_filter_option(self) -> int:
        """
        
                Get the current filter option.
        
                Returns:
                    int: The current filter option ( - 1 if none )
                
        """
    @property
    def directory(self) -> str:
        """
        
                Directory to store files in.
        
                Returns:
                    str: Directory to store files in.
                
        """
    @property
    def extension_options(self) -> typing.List[typing.Tuple[str, str]]:
        """
        
                Gets the extension_options.
        
                Returns:
                    List[Tuple[str, str]]: Pair value of file extension and options
                
        """
    @property
    def filename(self) -> str:
        """
        
                Returns the filename to use for the file.
        
                Returns:
                    str: The filename to use for the file.
                
        """
    @filename.setter
    def filename(self, filename):
        """
          Set the filename to use for this file. 
        """
    @property
    def label_name(self) -> str:
        """
        
                Get the label name.
        
                Returns:
                    str: The field label text.
                
        """
    @label_name.setter
    def label_name(self, name: str):
        """
        
                Label the field with the name.
        
                Args:
                    name (str): value set to the field.
                
        """
    @property
    def postfix_options(self) -> typing.List[str]:
        """
        
                Gets all the postfix_options.
        
                Returns:
                    List[str]: All postfix options.
                
        """
    @property
    def selected_extension(self) -> str:
        """
        
                Return the currently selected file extension.
        
                Returns:
                    str: File extension.
                
        """
    @property
    def selected_postfix(self) -> str:
        """
        
                Return the selected postfix.
        
                Returns:
                    str: Selected postfix.
                
        """
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.filepicker-2.11.7+d02c707b/icons/NvidiaDark')
