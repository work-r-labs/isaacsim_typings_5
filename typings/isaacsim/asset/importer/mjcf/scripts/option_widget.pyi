from __future__ import annotations
from isaacsim.asset.importer.mjcf.scripts.style import get_option_style
from isaacsim.asset.importer.mjcf.scripts.ui_utils import add_folder_picker_icon
from isaacsim.asset.importer.mjcf.scripts.ui_utils import format_tt
from omni import ui
__all__ = ['OptionWidget', 'add_folder_picker_icon', 'checkbox_builder', 'float_field_builder', 'format_tt', 'get_option_style', 'option_frame', 'option_header', 'string_filed_builder', 'ui']
class OptionWidget:
    def __init__(self, models, config):
        ...
    def _build_colliders_frame(self):
        ...
    def _build_links_frame(self):
        ...
    def _build_model_frame(self):
        ...
    def _update_fix_base(self, model):
        ...
    def _update_import_option(self, model):
        ...
    def build_options(self):
        ...
    @property
    def config(self):
        ...
    @property
    def models(self):
        ...
def checkbox_builder(label = '', type = 'checkbox', default_val = False, tooltip = '', on_clicked_fn = None):
    """
    Creates a Stylized Checkbox
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            type (str, optional): Type of UI element. Defaults to "checkbox".
            default_val (bool, optional): Checked is True, Unchecked is False. Defaults to False.
            tooltip (str, optional): Tooltip to display over the Label. Defaults to "".
            on_clicked_fn (Callable, optional): Call-back function when clicked. Defaults to None.
    
        Returns:
            ui.SimpleBoolModel: model
        
    """
def float_field_builder(label = '', default_val = 0, tooltip = '', format = '%.2f'):
    """
    Creates a Stylized Floatfield Widget
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            default_val (int, optional): Default Value of UI element. Defaults to 0.
            tooltip (str, optional): Tooltip to display over the UI elements. Defaults to "".
    
        Returns:
            AbstractValueModel: model
        
    """
def option_frame(title, build_content_fn, collapse_fn = None):
    ...
def option_header(collapsed, title):
    ...
def string_filed_builder(default_val = ' ', tooltip = '', read_only = False, item_filter_fn = None, folder_dialog_title = 'Select Output Folder', folder_button_title = 'Select Folder'):
    """
    Creates a Stylized Stringfield Widget
    
        Args:
            default_val (str, optional): Text to initialize in Stringfield. Defaults to " ".
            tooltip (str, optional): Tooltip to display over the UI elements. Defaults to "".
            read_only (bool, optional): Prevents editing. Defaults to False.
            item_filter_fn (Callable, optional): filter function to pass to the FilePicker
            bookmark_label (str, optional): bookmark label to pass to the FilePicker
            bookmark_path (str, optional): bookmark path to pass to the FilePicker
        Returns:
            AbstractValueModel: model of Stringfield
        
    """
