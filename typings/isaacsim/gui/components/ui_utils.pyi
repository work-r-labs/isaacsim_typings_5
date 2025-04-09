from __future__ import annotations
import asyncio as asyncio
import carb as carb
from isaacsim.gui.components.callbacks import on_copy_to_clipboard
from isaacsim.gui.components.callbacks import on_docs_link_clicked
from isaacsim.gui.components.callbacks import on_open_IDE_clicked
from isaacsim.gui.components.callbacks import on_open_folder_clicked
from isaacsim.gui.components.style import get_style
import omni as omni
from omni.kit.window.extensions.ext_components import SimpleCheckBox
from omni.kit.window.filepicker.dialog import FilePickerDialog
from omni import ui
import os as os
import subprocess as subprocess
import sys as sys
__all__ = ['BUTTON_WIDTH', 'COLOR_W', 'COLOR_X', 'COLOR_Y', 'COLOR_Z', 'FilePickerDialog', 'LABEL_HEIGHT', 'LABEL_WIDTH', 'SearchListItem', 'SearchListItemDelegate', 'SearchListItemModel', 'SimpleCheckBox', 'add_folder_picker_btn', 'add_folder_picker_icon', 'add_line_rect_flourish', 'add_separator', 'asyncio', 'btn_builder', 'build_header', 'build_info_frame', 'build_simple_search', 'carb', 'cb_builder', 'color_picker_builder', 'combo_cb_dropdown_builder', 'combo_cb_plot_builder', 'combo_cb_scrolling_frame_builder', 'combo_cb_str_builder', 'combo_cb_xyz_plot_builder', 'combo_floatfield_slider_builder', 'combo_intfield_slider_builder', 'dropdown_builder', 'float_builder', 'format_tt', 'get_style', 'inf', 'int_builder', 'multi_btn_builder', 'multi_cb_builder', 'multi_dropdown_builder', 'omni', 'on_copy_to_clipboard', 'on_docs_link_clicked', 'on_open_IDE_clicked', 'on_open_folder_clicked', 'os', 'plot_builder', 'progress_bar_builder', 'scrolling_frame_builder', 'setup_ui_headers', 'state_btn_builder', 'str_builder', 'subprocess', 'sys', 'ui', 'xyz_builder', 'xyz_plot_builder']
class SearchListItem(omni.ui._ui.AbstractItem):
    def __init__(self, text):
        ...
    def __repr__(self):
        ...
    def name(self):
        ...
class SearchListItemDelegate(omni.ui._ui.AbstractItemDelegate):
    """
    
        Delegate is the representation layer. TreeView calls the methods
        of the delegate to create custom widgets for each item.
        
    """
    def __init__(self, on_double_click_fn = None):
        ...
    def build_branch(self, model, item, column_id, level, expanded):
        """
        Create a branch widget that opens or closes subtree
        """
    def build_widget(self, model, item, column_id, level, expanded):
        """
        Create a widget per column per item
        """
    def on_double_click(self, button, model, label):
        """
        Called when the user double-clicked the item in TreeView
        """
class SearchListItemModel(omni.ui._ui.AbstractItemModel):
    """
    
        Represents the model for lists. It's very easy to initialize it
        with any string list:
            string_list = ["Hello", "World"]
            model = ListModel(*string_list)
            ui.TreeView(model)
        
    """
    def __init__(self, *args):
        ...
    def filter_text(self, text):
        ...
    def get_item_children(self, item):
        """
        Returns all the children when the widget asks it.
        """
    def get_item_value_model(self, item, column_id):
        """
        
                Return value model.
                It's the object that tracks the specific value.
                In our case we use ui.SimpleStringModel.
                
        """
    def get_item_value_model_count(self, item):
        """
        The number of columns
        """
def add_folder_picker_btn(on_click_fn):
    ...
def add_folder_picker_icon(on_click_fn, item_filter_fn = None, bookmark_label = None, bookmark_path = None, dialog_title = 'Select Output Folder', button_title = 'Select Folder'):
    ...
def add_line_rect_flourish(draw_line = True):
    """
    Aesthetic element that adds a Line + Rectangle after all UI elements in the row.
    
        Args:
            draw_line (bool, optional): Set false to only draw rectangle. Defaults to True.
        
    """
def add_separator():
    """
    Aesthetic element to adds a Line Separator.
    """
def btn_builder(label = '', type = 'button', text = 'button', tooltip = '', on_clicked_fn = None):
    """
    Creates a stylized button.
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            type (str, optional): Type of UI element. Defaults to "button".
            text (str, optional): Text rendered on the button. Defaults to "button".
            tooltip (str, optional): Tooltip to display over the Label. Defaults to "".
            on_clicked_fn (Callable, optional): Call-back function when clicked. Defaults to None.
    
        Returns:
            ui.Button: Button
        
    """
def build_header(ext_path, file_path, title = 'My Custom Extension', doc_link = 'https://docs.isaacsim.omniverse.nvidia.com/latest/index.html'):
    """
    Title Header with Quick Access Utility Buttons.
    """
def build_info_frame(overview = '', info_collapse = True):
    """
    Info Frame with Overview, Instructions, and Metadata for an Extension
    """
def build_simple_search(label = '', type = 'search', model = None, delegate = None, tooltip = ''):
    """
    A Simple Search Bar + TreeView Widget.
    
            Pass a list of items through the model, and a custom on_click_fn through the delegate.
    
            Returns the SearchWidget so user can destroy it on_shutdown.
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            type (str, optional): Type of UI element. Defaults to "search".
            model (ui.AbstractItemModel, optional): Item Model for Search. Defaults to None.
            delegate (ui.AbstractItemDelegate, optional): Item Delegate for Search. Defaults to None.
            tooltip (str, optional): Tooltip to display over the Label. Defaults to "".
    
        Returns:
            Tuple(Search Widget, Treeview):
        
    """
def cb_builder(label = '', type = 'checkbox', default_val = False, tooltip = '', on_clicked_fn = None):
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
def color_picker_builder(label = '', type = 'color_picker', default_val = [1.0, 1.0, 1.0, 1.0], tooltip = 'Color Picker'):
    """
    Creates a Color Picker Widget
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            type (str, optional): Type of UI element. Defaults to "color_picker".
            default_val (list, optional): List of (R,G,B,A) default values. Defaults to [1.0, 1.0, 1.0, 1.0].
            tooltip (str, optional): Tooltip to display over the Label. Defaults to "Color Picker".
    
        Returns:
            AbstractItemModel: ui.ColorWidget.model
        
    """
def combo_cb_dropdown_builder(label = '', type = 'checkbox_dropdown', default_val = [False, 0], items = ['Option 1', 'Option 2', 'Option 3'], tooltip = '', on_clicked_fn = ...):
    """
    Creates a Stylized Dropdown Combobox with an Enable Checkbox
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            type (str, optional): Type of UI element. Defaults to "checkbox_dropdown".
            default_val (list, optional): list(cb_default, dropdown_default). Defaults to [False, 0].
            items (list, optional): List of items for dropdown box. Defaults to ["Option 1", "Option 2", "Option 3"].
            tooltip (str, optional): Tooltip to display over the Label. Defaults to "".
            on_clicked_fn (list, optional): List of callback functions. Defaults to [lambda x: None, None].
    
        Returns:
            Tuple(ui.SimpleBoolModel, ui.ComboBox): (cb_model, combobox)
        
    """
def combo_cb_plot_builder(label = '', default_val = False, on_clicked_fn = ..., data = None, min = -1, max = 1, type = ..., value_stride = 1, color = None, tooltip = ''):
    """
    Creates a Checkbox-Enabled dyanamic plot
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            default_val (bool, optional): Checkbox default. Defaults to False.
            on_clicked_fn (Callable, optional): Checkbox Callback function. Defaults to lambda x: None.
            data (list(), optional): Data to plat. Defaults to None.
            min (int, optional): Min Y Value. Defaults to -1.
            max (int, optional): Max Y Value. Defaults to 1.
            type (ui.Type, optional): Plot Type. Defaults to ui.Type.LINE.
            value_stride (int, optional): Width of plot stride. Defaults to 1.
            color (int, optional): Plot color. Defaults to None.
            tooltip (str, optional): Tooltip to display over the Label. Defaults to "".
    
    
        Returns:
            list(SimpleBoolModel, ui.Plot): (cb_model, plot)
        
    """
def combo_cb_scrolling_frame_builder(label = '', type = 'cb_scrolling_frame', default_val = [False, 'No Data'], tooltip = '', on_clicked_fn = ...):
    """
    Creates a Labeled, Checkbox-enabled Scrolling Frame with CopyToClipboard button
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            type (str, optional): Type of UI element. Defaults to "cb_scrolling_frame".
            default_val (list, optional): List of Checkbox and Frame Defaults. Defaults to [False, "No Data"].
            tooltip (str, optional): Tooltip to display over the Label. Defaults to "".
            on_clicked_fn (Callable, optional): Callback function when clicked. Defaults to lambda x : None.
    
        Returns:
            list(SimpleBoolModel, ui.Label): (model, label)
        
    """
def combo_cb_str_builder(label = '', type = 'checkbox_stringfield', default_val = [False, ' '], tooltip = '', on_clicked_fn = ..., use_folder_picker = False, read_only = False, folder_dialog_title = 'Select Output Folder', folder_button_title = 'Select Folder'):
    """
    Creates a Stylized Checkbox + Stringfield Widget
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            type (str, optional): Type of UI element. Defaults to "checkbox_stringfield".
            default_val (str, optional): Text to initialize in Stringfield. Defaults to [False, " "].
            tooltip (str, optional): Tooltip to display over the UI elements. Defaults to "".
            use_folder_picker (bool, optional): Add a folder picker button to the right. Defaults to False.
            read_only (bool, optional): Prevents editing. Defaults to False.
    
        Returns:
            Tuple(ui.SimpleBoolModel, AbstractValueModel): (cb_model, str_field_model)
        
    """
def combo_cb_xyz_plot_builder(label = '', default_val = False, on_clicked_fn = ..., data = list(), min = -1, max = 1, type = ..., value_stride = 1, tooltip = ''):
    """
    [summary]
    
        Args:
            label (str, optional):  Label to the left of the UI element. Defaults to "".
            default_val (bool, optional): Checkbox default. Defaults to False.
            on_clicked_fn (Callable, optional): Checkbox Callback function. Defaults to lambda x: None.
            data list(), optional): Data to plat. Defaults to None.
            min (int, optional): Min Y Value. Defaults to -1.
            max (int, optional): Max Y Value. Defaults to 1.
            type (ui.Type, optional): Plot Type. Defaults to ui.Type.LINE.
            value_stride (int, optional): Width of plot stride. Defaults to 1.
            tooltip (str, optional): Tooltip to display over the Label. Defaults to "".
    
        Returns:
            Tuple(list(ui.Plot), list(AbstractValueModel)): ([plot_0, plot_1, plot_2], [val_model_x, val_model_y, val_model_z])
        
    """
def combo_floatfield_slider_builder(label = '', type = 'floatfield_stringfield', default_val = 0.5, min = 0, max = 1, step = 0.01, tooltip = ['', '']):
    """
    Creates a Stylized FloatField + FloatSlider Widget
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            type (str, optional): Type of UI element. Defaults to "floatfield_stringfield".
            default_val (float, optional): Default Value. Defaults to 0.5.
            min (int, optional): Minimum Value. Defaults to 0.
            max (int, optional): Maximum Value. Defaults to 1.
            step (float, optional): Step. Defaults to 0.01.
            tooltip (list, optional): List of tooltips. Defaults to ["", ""].
    
        Returns:
            Tuple(AbstractValueModel, IntSlider): (flt_field_model, flt_slider_model)
        
    """
def combo_intfield_slider_builder(label = '', type = 'intfield_stringfield', default_val = 0.5, min = 0, max = 1, step = 0.01, tooltip = ['', '']):
    """
    Creates a Stylized IntField + Stringfield Widget
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            type (str, optional): Type of UI element. Defaults to "intfield_stringfield".
            default_val (float, optional): Default Value. Defaults to 0.5.
            min (int, optional): Minimum Value. Defaults to 0.
            max (int, optional): Maximum Value. Defaults to 1.
            step (float, optional): Step. Defaults to 0.01.
            tooltip (list, optional): List of tooltips. Defaults to ["", ""].
    
        Returns:
            Tuple(AbstractValueModel, IntSlider): (flt_field_model, flt_slider_model)
        
    """
def dropdown_builder(label = '', type = 'dropdown', default_val = 0, items = ['Option 1', 'Option 2', 'Option 3'], tooltip = '', on_clicked_fn = None):
    """
    Creates a Stylized Dropdown Combobox
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            type (str, optional): Type of UI element. Defaults to "dropdown".
            default_val (int, optional): Default index of dropdown items. Defaults to 0.
            items (list, optional): List of items for dropdown box. Defaults to ["Option 1", "Option 2", "Option 3"].
            tooltip (str, optional): Tooltip to display over the Label. Defaults to "".
            on_clicked_fn (Callable, optional): Call-back function when clicked. Defaults to None.
    
        Returns:
            AbstractItemModel: model
        
    """
def float_builder(label = '', type = 'floatfield', default_val = 0, tooltip = '', min = ..., max = ..., step = 0.1, format = '%.2f'):
    """
    Creates a Stylized Floatfield Widget
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            type (str, optional): Type of UI element. Defaults to "floatfield".
            default_val (int, optional): Default Value of UI element. Defaults to 0.
            tooltip (str, optional): Tooltip to display over the UI elements. Defaults to "".
    
        Returns:
            AbstractValueModel: model
        
    """
def format_tt(tt):
    ...
def int_builder(label = '', type = 'intfield', default_val = 0, tooltip = '', min = -9223372036854775807, max = 9223372036854775807):
    """
    Creates a Stylized Intfield Widget
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            type (str, optional): Type of UI element. Defaults to "intfield".
            default_val (int, optional): Default Value of UI element. Defaults to 0.
            tooltip (str, optional): Tooltip to display over the UI elements. Defaults to "".
            min (int, optional): Minimum limit for int field. Defaults to sys.maxsize * -1
            max (int, optional): Maximum limit for int field. Defaults to sys.maxsize * 1
    
        Returns:
            AbstractValueModel: model
        
    """
def multi_btn_builder(label = '', type = 'multi_button', count = 2, text = ['button', 'button'], tooltip = ['', '', ''], on_clicked_fn = [None, None]):
    """
    Creates a Row of Stylized Buttons
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            type (str, optional): Type of UI element. Defaults to "multi_button".
            count (int, optional): Number of UI elements to create. Defaults to 2.
            text (list, optional): List of text rendered on the UI elements. Defaults to ["button", "button"].
            tooltip (list, optional): List of tooltips to display over the UI elements. Defaults to ["", "", ""].
            on_clicked_fn (list, optional): List of call-backs function when clicked. Defaults to [None, None].
    
        Returns:
            list(ui.Button): List of Buttons
        
    """
def multi_cb_builder(label = '', type = 'multi_checkbox', count = 2, text = [' ', ' '], default_val = [False, False], tooltip = ['', '', ''], on_clicked_fn = [None, None]):
    """
    Creates a Row of Stylized Checkboxes.
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            type (str, optional): Type of UI element. Defaults to "multi_checkbox".
            count (int, optional): Number of UI elements to create. Defaults to 2.
            text (list, optional): List of text rendered on the UI elements. Defaults to [" ", " "].
            default_val (list, optional): List of default values. Checked is True, Unchecked is False. Defaults to [False, False].
            tooltip (list, optional): List of tooltips to display over the UI elements. Defaults to ["", "", ""].
            on_clicked_fn (list, optional): List of call-backs function when clicked. Defaults to [None, None].
    
        Returns:
            list(ui.SimpleBoolModel): List of models
        
    """
def multi_dropdown_builder(label = '', type = 'multi_dropdown', count = 2, default_val = [0, 0], items = [['Option 1', 'Option 2', 'Option 3'], ['Option A', 'Option B', 'Option C']], tooltip = '', on_clicked_fn = [None, None]):
    """
    Creates a Stylized Multi-Dropdown Combobox
    
        Returns:
            AbstractItemModel: model
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            type (str, optional): Type of UI element. Defaults to "multi_dropdown".
            count (int, optional): Number of UI elements. Defaults to 2.
            default_val (list(int), optional): List of default indices of dropdown items. Defaults to 0.. Defaults to [0, 0].
            items (list(list), optional): List of list of items for dropdown boxes. Defaults to [["Option 1", "Option 2", "Option 3"], ["Option A", "Option B", "Option C"]].
            tooltip (str, optional): Tooltip to display over the Label. Defaults to "".
            on_clicked_fn (list(Callable), optional): List of call-back function when clicked. Defaults to [None, None].
    
        Returns:
            list(AbstractItemModel): list(models)
        
    """
def plot_builder(label = '', data = None, min = -1, max = 1, type = ..., value_stride = 1, color = None, tooltip = ''):
    """
    Creates a stylized static plot
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            data (list(float), optional): Data to plot. Defaults to None.
            min (int, optional): Minimum Y Value. Defaults to -1.
            max (int, optional): Maximum Y Value. Defaults to 1.
            type (ui.Type, optional): Plot Type. Defaults to ui.Type.LINE.
            value_stride (int, optional): Width of plot stride. Defaults to 1.
            color (int, optional): Plot color. Defaults to None.
            tooltip (str, optional): Tooltip to display over the Label. Defaults to "".
    
        Returns:
            ui.Plot: plot
        
    """
def progress_bar_builder(label = '', type = 'progress_bar', default_val = 0, tooltip = 'Progress'):
    """
    Creates a Progress Bar Widget
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            type (str, optional): Type of UI element. Defaults to "progress_bar".
            default_val (int, optional): Starting Value. Defaults to 0.
            tooltip (str, optional): Tooltip to display over the Label. Defaults to "Progress".
    
        Returns:
            AbstractValueModel: ui.ProgressBar().model
        
    """
def scrolling_frame_builder(label = '', type = 'scrolling_frame', default_val = 'No Data', tooltip = ''):
    """
    Creates a Labeled Scrolling Frame with CopyToClipboard button
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            type (str, optional): Type of UI element. Defaults to "scrolling_frame".
            default_val (str, optional): Default Text. Defaults to "No Data".
            tooltip (str, optional): Tooltip to display over the Label. Defaults to "".
    
        Returns:
            ui.Label: label
        
    """
def setup_ui_headers(ext_id, file_path, title = 'My Custom Extension', doc_link = 'https://docs.isaacsim.omniverse.nvidia.com/latest/index.html', overview = '', info_collapsed = True):
    """
    Creates the Standard UI Elements at the top of each Isaac Extension.
    
        Args:
            ext_id (str): Extension ID.
            file_path (str): File path to source code.
            title (str, optional): Name of Extension. Defaults to "My Custom Extension".
            doc_link (str, optional): Hyperlink to Documentation. Defaults to "https://docs.isaacsim.omniverse.nvidia.com/latest/index.html".
            overview (str, optional): Overview Text explaining the Extension. Defaults to "".
        
    """
def state_btn_builder(label = '', type = 'state_button', a_text = 'STATE A', b_text = 'STATE B', tooltip = '', on_clicked_fn = None):
    """
    Creates a State Change Button that changes text when pressed.
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            type (str, optional): Type of UI element. Defaults to "button".
            a_text (str, optional): Text rendered on the button for State A. Defaults to "STATE A".
            b_text (str, optional): Text rendered on the button for State B. Defaults to "STATE B".
            tooltip (str, optional): Tooltip to display over the Label. Defaults to "".
            on_clicked_fn (Callable, optional): Call-back function when clicked. Defaults to None.
        
    """
def str_builder(label = '', type = 'stringfield', default_val = ' ', tooltip = '', on_clicked_fn = None, use_folder_picker = False, read_only = False, item_filter_fn = None, bookmark_label = None, bookmark_path = None, folder_dialog_title = 'Select Output Folder', folder_button_title = 'Select Folder'):
    """
    Creates a Stylized Stringfield Widget
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            type (str, optional): Type of UI element. Defaults to "stringfield".
            default_val (str, optional): Text to initialize in Stringfield. Defaults to " ".
            tooltip (str, optional): Tooltip to display over the UI elements. Defaults to "".
            use_folder_picker (bool, optional): Add a folder picker button to the right. Defaults to False.
            read_only (bool, optional): Prevents editing. Defaults to False.
            item_filter_fn (Callable, optional): filter function to pass to the FilePicker
            bookmark_label (str, optional): bookmark label to pass to the FilePicker
            bookmark_path (str, optional): bookmark path to pass to the FilePicker
        Returns:
            AbstractValueModel: model of Stringfield
        
    """
def xyz_builder(label = '', tooltip = '', axis_count = 3, default_val = [0.0, 0.0, 0.0, 0.0], min = ..., max = ..., step = 0.001, on_value_changed_fn = [None, None, None, None]):
    """
    [summary]
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            type (str, optional): Type of UI element. Defaults to "".
            axis_count (int, optional): Number of Axes to Display. Max 4. Defaults to 3.
            default_val (list, optional): List of default values. Defaults to [0.0, 0.0, 0.0, 0.0].
            min (float, optional): Minimum Float Value. Defaults to float("-inf").
            max (float, optional): Maximum Float Value. Defaults to float("inf").
            step (float, optional): Step. Defaults to 0.001.
            on_value_changed_fn (list, optional): List of callback functions for each axes. Defaults to [None, None, None, None].
    
        Returns:
            list(AbstractValueModel): list(model)
        
    """
def xyz_plot_builder(label = '', data = list(), min = -1, max = 1, tooltip = ''):
    """
    Creates a stylized static XYZ plot
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            data (list(float), optional): Data to plot. Defaults to [].
            min (int, optional): Minimum Y Value. Defaults to -1.
            max (int, optional): Maximum Y Value. Defaults to "".
            tooltip (str, optional): Tooltip to display over the Label.. Defaults to "".
    
        Returns:
            list(ui.Plot): list(x_plot, y_plot, z_plot)
        
    """
BUTTON_WIDTH: int = 120
COLOR_W: int = 4289353045
COLOR_X: int = 4283782570
COLOR_Y: int = 4285965169
COLOR_Z: int = 4288707919
LABEL_HEIGHT: int = 18
LABEL_WIDTH: int = 160
inf: float  # value = inf
