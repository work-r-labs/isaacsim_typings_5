from __future__ import annotations
import carb as carb
from collections.abc import Iterable
from isaacsim.gui.components.callbacks import on_copy_to_clipboard
import isaacsim.gui.components.element_wrappers.base_ui_element_wrappers
from isaacsim.gui.components.element_wrappers.base_ui_element_wrappers import UIWidgetWrapper
from isaacsim.gui.components.style import get_style
from isaacsim.gui.components.ui_utils import add_line_rect_flourish
from isaacsim.gui.components.ui_utils import add_separator
from isaacsim.gui.components.ui_utils import format_tt
from isaacsim.gui.components.widgets import DynamicComboBoxModel
import numpy as np
import omni as omni
from omni.kit.window.filepicker.dialog import FilePickerDialog
from omni import physx as _physx
from omni import ui
from omni.usd._usd import get_context
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdPhysics
import sys as sys
import typing as typing
__all__: list[str] = ['BUTTON_WIDTH', 'Button', 'CheckBox', 'CollapsableFrame', 'ColorPicker', 'DropDown', 'DynamicComboBoxModel', 'FilePickerDialog', 'FloatField', 'Frame', 'IntField', 'Iterable', 'LABEL_HEIGHT', 'LABEL_WIDTH', 'ScrollingFrame', 'ScrollingWindow', 'StateButton', 'StringField', 'TextBlock', 'UIWidgetWrapper', 'Usd', 'UsdGeom', 'UsdPhysics', 'XYPlot', 'add_line_rect_flourish', 'add_separator', 'carb', 'format_tt', 'get_context', 'get_prim_object_type', 'get_style', 'inf', 'np', 'omni', 'on_copy_to_clipboard', 'sys', 'typing', 'ui']
class Button(isaacsim.gui.components.element_wrappers.base_ui_element_wrappers.UIWidgetWrapper):
    """
    Create a Button UI Element
    
        Args:
            label (str): Short descriptive text to the left of the Button
            text (str): Text on the Button
            tooltip (str, optional): Text to appear when the mouse hovers over the Button. Defaults to "".
            on_click_fn (Callable, optional): Callback function that will be called when the button is pressed.
                Function should take no arguments.  The return value will not be used.  Defaults to None.
        
    """
    def __init__(self, label: str, text: str, tooltip = '', on_click_fn = None):
        ...
    def _create_ui_widget(self, label: str, text: str, tooltip: str):
        ...
    def _on_clicked_fn_wrapper(self):
        ...
    def set_on_click_fn(self, on_click_fn: typing.Callable):
        """
        Set the callback function for when the Button is clicked.
        
                Args:
                    on_click_fn (Callable): Callback function for when Button is clicked.
                        The function should take a single bool argument.  The return value will not be used.
                
        """
    def trigger_click(self):
        """
        Trigger identical behavior as if the user pressed the Button through the UI.
        """
    @property
    def button(self) -> omni.ui._ui.Button:
        """
        
                Returns:
                    omni.ui.Button: UI Button element
                
        """
    @property
    def label(self) -> omni.ui._ui.Label:
        """
        
                Returns:
                    omni.ui.Label: UI Label element that contains the descriptive text
                
        """
class CheckBox(isaacsim.gui.components.element_wrappers.base_ui_element_wrappers.UIWidgetWrapper):
    """
    Create a CheckBox UI Element
    
        Args:
            label (str): Short descriptive text to the left of the CheckBox
            default_value (bool, optional): If True, CheckBox will be checked. Defaults to False.
            tooltip (str, optional): Text to appear when the mouse hovers over the CheckBox.  Defaults to "".
            on_click_fn (_type_, optional): Callback function that will be called when the CheckBox is pressed.
                Function should take a single bool argument.  The return value will not be used.  Defaults to None.
        
    """
    def __init__(self, label: str, default_value: bool = False, tooltip = '', on_click_fn = None):
        ...
    def _create_ui_widget(self, label: str, default_value: bool, tooltip: str):
        ...
    def _on_click_fn_wrapper(self, model):
        ...
    def get_value(self) -> bool:
        """
        
                Returns:
                    bool: Check box is checked
                
        """
    def set_on_click_fn(self, on_click_fn: typing.Callable):
        """
        Set the function that will be called when the CheckBox is clicked.
        
                Args:
                    on_click_fn (Callable): Callback function for when CheckBox is clicked.
                        The function should take a single bool argument.  The return value will not be used.
                
        """
    def set_value(self, val: bool):
        """
        
                Args:
                    val (bool): If True, set CheckBox to checked state
                
        """
    @property
    def checkbox(self) -> omni.ui._ui.CheckBox:
        """
        
                Returns:
                    omni.ui.CheckBox: UI CheckBox element
                
        """
    @property
    def label(self) -> omni.ui._ui.Label:
        """
        
                Returns:
                    omni.ui.Label: UI Label element that contains the descriptive text
                
        """
class CollapsableFrame(Frame):
    """
    Create a CollapsableFrame UI element
    
        Args:
            title (str): Title of Collapsable Frame
            collapsed (bool, optional): Frame is collapsed. Defaults to True.
            enabled (bool, optional): Frame is enabled. Defaults to True.
            visible (bool, optional): Frame is visible. Defaults to True.
            build_fn (Callable, optional): A function that can be called to specify what should fill the Frame.
                Function should take no arguments.  Return values will not be used. Defaults to None.
        
    """
    def __init__(self, title: str, collapsed: bool = True, enabled: bool = True, visible: bool = True, build_fn: typing.Callable = None):
        ...
    def _create_frame(self, title: str, collapsed: bool, enabled: bool, visible: bool, build_fn: typing.Callable) -> omni.ui._ui.CollapsableFrame:
        ...
    @property
    def collapsed(self) -> bool:
        """
        
                Returns:
                    bool: CollapsableFrame is collapsed
                
        """
    @collapsed.setter
    def collapsed(self, value: bool):
        ...
    @property
    def title(self) -> str:
        """
        
                Returns:
                    str: Title text of CollapsableFrame
                
        """
    @title.setter
    def title(self, value: str):
        ...
class ColorPicker(isaacsim.gui.components.element_wrappers.base_ui_element_wrappers.UIWidgetWrapper):
    """
    Create a ColorPicker UI element to allow user-selection of an RGBA color
    
        Args:
            label (str): Short descriptive text to the left of the ColorPicker
            default_value (List[float], optional): RGBA color values between 0 and 1. Defaults to [1.0, 1.0, 1.0, 1.0].
            tooltip (str, optional): Text to appear when the mouse hovers over the ColorPicker. Defaults to "".
            on_color_picked_fn (Callable, optional): Function that will be called if the user picks a new color.
                Function should expect a List[float] as an argument with four RGBA color values between 0 and 1.
                The return value will not be used.
        
    """
    def __init__(self, label: str, default_value: typing.List[float] = [1.0, 1.0, 1.0, 1.0], tooltip: str = '', on_color_picked_fn: typing.Callable = None):
        ...
    def _create_ui_widget(self, label: str, default_value: typing.List[float], tooltip: str):
        ...
    def _on_color_picked_fn_wrapper(self, *worthless_args):
        ...
    def get_color(self) -> typing.List[float]:
        """
        Get the RGBA value of the selected color
        
                Returns:
                    List[float]: RGBA color value with four values between 0 and 1
                
        """
    def set_color(self, color: typing.List[float]):
        """
        Set the RGBA color value of the selected color
        
                Args:
                    color (List[float]): RGBA color value with four values between 0 and 1
                
        """
    def set_on_color_picked_fn(self, on_color_picked_fn: typing.Callable):
        """
        Set the function that should be called if the user picks a new color
        
                Args:
                    on_color_picked_fn (Callable): Function that will be called if the user picks a new color.
                        Function should expect a List[float] as an argument with four RGBA color values between 0 and 1.
                        The return value will not be used.
                
        """
    @property
    def color_picker(self) -> omni.ui._ui.ColorWidget:
        """
        
                Returns:
                    omni.ui.ColorWidget: UI ColorWidget element
                
        """
    @property
    def label(self) -> omni.ui._ui.Label:
        """
        
                Returns:
                    omni.ui.Label: UI Label element that contains the descriptive text
                
        """
class DropDown(isaacsim.gui.components.element_wrappers.base_ui_element_wrappers.UIWidgetWrapper):
    """
    
        Create a DropDown UI element.
        A DropDown menu can be populated by the user, with a callback function specified
        for when an item is selected.
    
        Args:
            label (str): Short descriptive text to the left of the DropDown
            tooltip (str, optional): Text to appear when the mouse hovers over the DropDown. Defaults to "".
            populate_fn (Callable, optional): A user-defined function that returns a list[str] of items
                that should populate the drop-down menu.  This Function should have 0 arguments. Defaults to None.
            on_selection_fn (Callable, optional): A user-defined callback function for when an element is selected
                from the DropDown.  The function should take in a string argument of the selection.
                The return value will not be used.  Defaults to None.
            keep_old_selections (bool, optional): When the DropDown is repopulated with the user-defined populate_fn,
                the default behavior is to reset the selection in the DropDown to be at index 0.  If the user
                sets keep_old_selections=True, when the DropDown is repopulated and the old selection is still one of
                the options, the new selection will match the old selection.  Defaults to False.
        
    """
    def __init__(self, label: str, tooltip: str = '', populate_fn: typing.Callable = None, on_selection_fn: typing.Callable = None, keep_old_selections: bool = False, add_flourish: bool = True):
        ...
    def _create_ui_widget(self, label, tooltip):
        ...
    def _find_all_usd_objects_of_type(self, obj_type: str):
        ...
    def _item_changed_fn_wrapper(self, model, val):
        ...
    def get_items(self) -> typing.List[str]:
        """
        Get the items in the DropDown
        
                Returns:
                    List[str]: A list of the options in the DropDown
                
        """
    def get_selection(self) -> str:
        """
        Get current selection in DropDown
        
                Returns:
                    str: Current selection in DropDown
                
        """
    def get_selection_index(self) -> int:
        """
        Get index of selection in DropDown menu
        
                Returns:
                    int: Index of selection in DropDown menu
                
        """
    def repopulate(self):
        """
        A function that the user can call to make the DropDown menu repopulate.
                This will call the populate_fn set by the user.
                
        """
    def set_items(self, items: typing.List[str], select_index: int = None):
        """
        Set the items in the DropDown explicitly.
        
                Args:
                    items (List[str]): New set of items in the DropDown
                    select_index (int, optional): Index of item to select.  If left as None, behavior is determined by the
                        keep_old_selections flag.  Defaults to None.
                
        """
    def set_keep_old_selection(self, val: bool):
        """
        Set keep_old_selection flag to determine behavior when repopulating the DropDown
        
                Args:
                    val (bool): When the DropDown is repopulated with the user-defined populate_fn,
                        the default behavior is to reset the selection in the DropDown to be at index 0.  If the user
                        sets keep_old_selections=True, when the DropDown is repopulated and the old selection is still one of
                        the options, the new selection will match the old selection, and the on_selection_fn() will not be called.
                
        """
    def set_on_selection_fn(self, on_selection_fn: typing.Callable):
        """
        Set the function that gets called when a new item is selected from the DropDown
        
                Args:
                    on_selection_fn (Callable): A function that is called when a new item is selected from the DropDown.
                        he function should take in a string argument of the selection.  Its return value is not used.
                
        """
    def set_populate_fn(self, populate_fn: typing.Callable, repopulate: bool = True):
        """
        Set the populate_fn for this DropDown
        
                Args:
                    populate_fn (Callable): Function used to specify the options that fill the DropDown.
                        Function should take no arguments and return a list[str].
                    repopulate (bool, optional): If true, repopulate the DropDown using the new populate_fn. Defaults to True.
                
        """
    def set_populate_fn_to_find_all_usd_objects_of_type(self, object_type: str, repopulate = True):
        """
        
                Set the populate_fn to find all objects of a specified type on the USD stage.  This is
                included as a convenience function to fulfill one common use-case for a DropDown menu.
                This overrides the populate_fn set by the user.
        
                Args:
                    object_type (str): A string name of the type of USD object matching the output of
                        get_prim_object_type(prim_path)
                    repopulate (bool, optional): Repopulate the DropDown immediately. Defaults to True.
                
        """
    def set_selection(self, selection: str):
        """
        Set the selected item in the DropDown.
                If the specifified selection is not in the DropDown, nothing will happen.
        
                Args:
                    selection (str): Item to select in the DropDown
                
        """
    def set_selection_by_index(self, select_index: int):
        """
        Set the selected item in the DropDown by index.
                If the provided index is out of bounds, nothing will happen.
        
                Args:
                    select_index (int): Index of item to select from DropDown
                
        """
    def trigger_on_selection_fn_with_current_selection(self):
        """
        Call the user on_selection_fn() with whatever item is currently selected in the DropDown.
        """
    @property
    def combobox(self) -> omni.ui._ui.ComboBox:
        """
        
                Returns:
                    omni.ui.ComboBox: UI ComboBox element.
                
        """
    @property
    def label(self) -> omni.ui._ui.Label:
        """
        
                Returns:
                    omni.ui.Label: UI Label element that contains the descriptive text
                
        """
class FloatField(isaacsim.gui.components.element_wrappers.base_ui_element_wrappers.UIWidgetWrapper):
    """
    
        Creates a FloatField UI element.
    
        Args:
            label (str): Short descriptive text to the left of the FloatField.
            tooltip (str, optional): Text to appear when the mouse hovers over the FloatField. Defaults to "".
            default_value (float, optional): Default value of the Float Field. Defaults to 0.0.
            step (float, optional): Smallest increment that the user can change the float by when dragging mouse. Defaults to 0.01.
            format (str, optional): Formatting string for float. Defaults to "%.2f".
            lower_limit (float, optional): Lower limit of float. Defaults to None.
            upper_limit (float, optional): Upper limit of float. Defaults to None.
            on_value_changed_fn (Callable, optional): Function to be called when the value of the float is changed.
                The function should take a float as an argument.  The return value will not be used. Defaults to None.
        
    """
    def __init__(self, label: str, tooltip: str = '', default_value: float = 0.0, step: float = 0.01, format: str = '%.2f', lower_limit: float = None, upper_limit: float = None, on_value_changed_fn: typing.Callable = None, on_end_edit_fn: typing.Callable = None):
        ...
    def _create_ui_widget(self, label, tooltip, default_value, step, format):
        ...
    def _on_value_changed_fn_wrapper(self, model):
        ...
    def get_lower_limit(self) -> float:
        """
        Get the lower limit on the FloatField
        
                Returns:
                    float: Lower limit on FloatField
                
        """
    def get_upper_limit(self) -> float:
        """
        Get the upper limit on the FloatField
        
                Returns:
                    float: Upper limit on FloatField
                
        """
    def get_value(self) -> float:
        """
        Return the current value of the FloatField
        
                Returns:
                    float: Current value of the FloatField
                
        """
    def set_lower_limit(self, lower_limit: float):
        """
        Set lower limit of FloatField.
                If current value is lower than lower_limit, the current value will be clipped to lower_limit
        
                Args:
                    lower_limit (float): lower limit of FloatField
                
        """
    def set_on_end_edit_fn(self, on_end_edit_fn: typing.Callable):
        """
        Set function that is called when the user finishes editing the FloatField
        
                Args:
                    on_end_edit_fn (Callable): Function that is called when the user finishes editing the FloatField.
                        Function should take a float as the argument. The return value will not be used.
                
        """
    def set_on_value_changed_fn(self, on_value_changed_fn: typing.Callable):
        """
        Set function that is called when the value of the FloatField is modified
        
                Args:
                    on_value_changed_fn (Callable): Function that is called when the value of the FloatField is modified.
                        Function should take a float as the argument. The return value will not be used.
                
        """
    def set_upper_limit(self, upper_limit: float):
        """
        Set upper limit of FloatField.
                If current value is higher than upper_limit, the current value will be clipped to upper_limit
        
                Args:
                    upper_limit (float): Upper limit of FloatField
                
        """
    def set_value(self, val: float):
        """
        Set the value in the FloatField
        
                Args:
                    val (float): Value to fill FloatField
                
        """
    @property
    def float_field(self) -> omni.ui._ui.FloatField:
        """
        
                Returns:
                    omni.ui.FloatField: UI FloatField element
                
        """
    @property
    def label(self) -> omni.ui._ui.Label:
        """
        
                Returns:
                    omni.ui.Label: UI Label element that contains the descriptive text
                
        """
class Frame(isaacsim.gui.components.element_wrappers.base_ui_element_wrappers.UIWidgetWrapper):
    """
    Create a Frame UI element
    
        Args:
            enabled (bool, optional): Frame is enabled. Defaults to True.
            visible (bool, optional): Frame is visible. Defaults to True.
            build_fn (Callable, optional): A function that can be called to specify what should fill the Frame.
                Function should take no arguments.  Return values will not be used. Defaults to None.
        
    """
    def __enter__(self):
        ...
    def __exit__(self, *args):
        ...
    def __init__(self, enabled: bool = True, visible: bool = True, build_fn: typing.Callable = None):
        ...
    def _create_frame(self, enabled: bool, visible: bool, build_fn: typing.Callable) -> omni.ui._ui.CollapsableFrame:
        ...
    def rebuild(self):
        """
        
                Rebuild the Frame using the specified build_fn
                
        """
    def set_build_fn(self, build_fn: typing.Callable):
        """
        Set the build_fn to use when rebuilding the frame.
        
                Args:
                    build_fn (Callable): Build function to use when rebuilding the frame.  Function should take
                        no arguments.  Return values will not be used.
                
        """
    @property
    def frame(self) -> omni.ui._ui.Frame:
        """
        
                Returns:
                    omni.ui.Frame: A UI Frame
                
        """
class IntField(isaacsim.gui.components.element_wrappers.base_ui_element_wrappers.UIWidgetWrapper):
    """
    
        Creates a IntField UI element.
    
        Args:
            label (str): Short descriptive text to the left of the IntField.
            tooltip (str, optional): Text to appear when the mouse hovers over the IntField. Defaults to "".
            default_value (int, optional): Default value of the IntField. Defaults to 0.
            lower_limit (int, optional): Lower limit of float. Defaults to None.
            upper_limit (int, optional): Upper limit of float. Defaults to None.
            on_value_changed_fn (Callable, optional): Function to be called when the value of the int is changed.
                The function should take an int as an argument.  The return value will not be used. Defaults to None.
        
    """
    def __init__(self, label: str, tooltip: str = '', default_value: int = 0, lower_limit: int = None, upper_limit: int = None, on_value_changed_fn: typing.Callable = None):
        ...
    def _create_ui_widget(self, label, tooltip, default_value):
        ...
    def _on_value_changed_fn_wrapper(self, model):
        ...
    def get_lower_limit(self) -> int:
        """
        Get the lower limit on the IntField.
        
                Returns:
                    int: Lower Limit on IntField
                
        """
    def get_upper_limit(self) -> int:
        """
        Get the upper limit on the IntField.
        
                Returns:
                    int: Upper Limit on IntField
                
        """
    def get_value(self) -> int:
        """
        Get the current value of the int field
        
                Returns:
                    int: Current value of the int field
                
        """
    def set_lower_limit(self, lower_limit: int):
        """
        Set lower limit of IntField.
                If current value is lower than lower_limit, the current value will be clipped to lower_limit
        
                Args:
                    lower_limit (int): lower limit of IntField
                
        """
    def set_on_value_changed_fn(self, on_value_changed_fn: typing.Callable):
        """
        Set function that is called when the value of the IntField is modified
        
                Args:
                    on_value_changed_fn (Callable): Function that is called when the value of the IntField is modified.
                        Function should take a int as the argument. The return value will not be used.
                
        """
    def set_upper_limit(self, upper_limit: int):
        """
        Set upper limit of IntField.
                If current value is higher than upper_limit, the current value will be clipped to upper_limit
        
                Args:
                    upper_limit (int): Upper limit of IntField
                
        """
    def set_value(self, val: int):
        """
        Set the value in the IntField
        
                Args:
                    val (int): Value to fill IntField
                
        """
    @property
    def int_field(self) -> omni.ui._ui.IntField:
        """
        
                Returns:
                    omni.ui.IntField: UI IntField elements
                
        """
    @property
    def label(self) -> omni.ui._ui.Label:
        """
        
                Returns:
                    omni.ui.Label: UI Label element that contains the descriptive text
                
        """
class ScrollingFrame(Frame):
    """
    Create a ScrollingFrame UI element with a specified size.
    
        Args:
            num_lines (int, optional): Determines height of ScrollingFrame element in terms of the
                typical line height of UI elements. If not specified, the ScrollingFrame will fill the space it can in the UI Window.
            enabled (bool, optional): Frame is enabled. Defaults to True.
            visible (bool, optional): Frame is visible. Defaults to True.
            build_fn (Callable, optional): A function that can be called to specify what should fill the Frame.
                Function should take no arguments.  Return values will not be used. Defaults to None.
        
    """
    def __init__(self, num_lines = None, enabled: bool = True, visible: bool = True, build_fn: typing.Callable = None):
        ...
    def _create_frame(self, num_lines: typing.Optional[int], enabled: bool, visible: bool, build_fn: typing.Callable) -> omni.ui._ui.ScrollingFrame:
        ...
    def set_num_lines(self, num_lines: int):
        """
        Set the height of the ScrollingFrame element in terms of the typical line height of
                other UI elements.
        
                Args:
                    num_lines (int): Number of lines that should be shown in a ScrollingFrame.
                
        """
class ScrollingWindow(omni.ui._ui.Window):
    def __init__(self, **kwargs):
        ...
    @property
    def frame(self) -> omni.ui._ui.ScrollingFrame:
        """
        
                Returns:
                    omni.ui.Frame: A UI Frame
                
        """
class StateButton(isaacsim.gui.components.element_wrappers.base_ui_element_wrappers.UIWidgetWrapper):
    """
    
        Creates a State Button UI element.
        A StateButton is a button that changes between two states A and B when clicked.
        In state A, the StateButton has a_text written on it, and
        in state B, the StateButton has b_text written on it.
    
        Args:
            label (str): Short descriptive text to the left of the StateButton
            a_text (str): Text on the StateButton in one of its two states
            b_text (str): Text on the StateButton in the other of its two states
            tooltip (str, optional): Text that appears when the mouse hovers over the button. Defaults to "".
            on_a_click_fn (Callable, optional): A function that should be called when the button is clicked while in
                state A. Function should have 0 arguments.  The return value will not be used.  Defaults to None.
            on_b_click_fn (Callable, optional): A function that should be called when the button is clicked while in
                state B. Function should have 0 arguments.  The return value will not be used.  Defaults to None.
            physics_callback_fn (Callable, optional): A function that will be called on every physics step while the
                button is in state B (a_text was pressed). The function should have one argument for physics step size (float).
                The return value will not be used. Defaults to None.
        
    """
    def __init__(self, label: str, a_text: str, b_text: str, tooltip = '', on_a_click_fn: typing.Callable = None, on_b_click_fn: typing.Callable = None, physics_callback_fn: typing.Callable = None):
        ...
    def _creat_ui_widget(self, label: str, a_text: str, b_text: str, tooltip: str):
        ...
    def _create_physics_callback(self):
        ...
    def _on_clicked_fn_wrapper(self, value):
        ...
    def _remove_physics_callback(self):
        ...
    def cleanup(self):
        """
        Remove physics callback created by the StateButton if exists.
        """
    def get_current_text(self) -> str:
        """
        Get the current text on the button.
        """
    def is_in_a_state(self) -> bool:
        """
        Return True if the StateButton is in the a state.  False implies that it is in the b state.
        
                Returns:
                    bool: True when the StateButton is in the b state.
                
        """
    def reset(self):
        """
        Reset StateButton to state A.
        """
    def set_on_a_click_fn(self, on_a_click_fn: typing.Callable):
        """
        Set a function that is called when the button is clicked in state A.
        
                Args:
                    on_a_click_fn (Callable): A function that is called when the button is clicked in state A.
                        Function should take no arguments.  The return value will not be used.
                
        """
    def set_on_b_click_fn(self, on_b_click_fn: typing.Callable):
        """
        Set a function that is called when the button is clicked in state B.
        
                Args:
                    on_b_click_fn (Callable): A function that is called when the button is clicked in state B.
                        Function should take no arguments.  The return value will not be used.
                
        """
    def set_physics_callback_fn(self, physics_callback_fn: typing.Callable):
        """
        Set a physics callback function that will be called on every physics step while the StateButton is
                in state B.
        
                Args:
                    physics_callback_fn (Callable): A function that will be called on every physics step while the
                        button is in state B (a_text was pressed). The function should have one argument for physics step size (float).
                        The return value will not be used.
                
        """
    def trigger_click_if_a_state(self):
        """
        
                If in the A state, trigger button to execute the same behavior as if it were clicked by the
                user.  If the button is in the B state, nothing will happen.
                
        """
    def trigger_click_if_b_state(self):
        """
        
                If in the B state, trigger button to execute the same behavior as if it were clicked by the
                user.  If the button is in the A state, nothing will happen.  This is distinct from calling
                reset() because the user on_b_click_fn() will be triggered.
                
        """
    @property
    def label(self) -> omni.ui._ui.Label:
        """
        
                Returns:
                    omni.ui.Label: UI Label element that contains the descriptive text
                
        """
    @property
    def state_button(self) -> omni.ui._ui.Button:
        """
        
                Returns:
                    omni.ui.Button: UI Button element
                
        """
class StringField(isaacsim.gui.components.element_wrappers.base_ui_element_wrappers.UIWidgetWrapper):
    """
    Create StringField UI Element.
    
        Starting at use_folder_picker, the arguments to the StringField all pertain to the folder_picker.
        If the folder_picker is not used, these arguments may all be ignored.
    
    
        Args:
            label (str, optional): Label to the left of the UI element. Defaults to "".
            tooltip (str, optional): Tooltip to display over the UI elements. Defaults to "".
            default_val (str, optional): Text to initialize in Stringfield. Defaults to " ".
            read_only (bool, optional): Prevents editing. Defaults to False.
            multiline_okay (bool, optional): If True, allow newline character in input strings. Defaults to False.
            on_value_changed_fn (Callable, optional) Function called when value of StringField is changed.
                The function should take a string as an argument.  The return value will not be used. Defaults to None.
            use_folder_picker (bool, optional): Add a folder picker button to the right. Defaults to False.
            item_filter_fn (Callable, optional): Filter function to pass to the FilePicker.  This function should take a string
                as an argument and return a boolean.  When the user opens the file picker, every file in the directory they are
                viewing will be passed to item_filter_fn, and when True is returned, the file will be shown.  When False is
                returned, the file will not be shown.  This can be used to ensure that the user may only select valid file types.
            bookmark_label (str, optional): Bookmark label to pass to the FilePicker.  This will create a bookmark when the
                file picker is used with the label specified here.
            bookmark_path (str, optional): Bookmark path to pass to the FilePicker.  This will create a bookmark when the file
                picker is used with the path specified here.
        
    """
    def __init__(self, label: str, tooltip: str = '', default_value: str = '', read_only = False, multiline_okay = False, on_value_changed_fn: typing.Callable = None, use_folder_picker = False, item_filter_fn = None, bookmark_label = None, bookmark_path = None, folder_dialog_title = 'Select Output Folder', folder_button_title = 'Select Folder'):
        ...
    def _create_ui_widget(self, label = '', default_val = ' ', tooltip = '', use_folder_picker = False, read_only = False, multiline_okay = True, bookmark_label = None, bookmark_path = None, folder_dialog_title = 'Select Output Folder', folder_button_title = 'Select Folder'):
        ...
    def _item_filter_fn_wrapper(self, file):
        ...
    def _on_value_changed_fn_wrapper(self, model):
        ...
    def add_folder_picker_icon(self, on_click_fn, item_filter_fn = None, bookmark_label = None, bookmark_path = None, dialog_title = 'Select Output Folder', button_title = 'Select Folder'):
        ...
    def get_value(self) -> str:
        """
        Return the current value of the StringField
        
                Returns:
                    str: Current value of the StringField
                
        """
    def set_item_filter_fn(self, item_filter_fn: typing.Callable):
        """
        Set the filter function that will be used with the file picker
        
                Args:
                    item_filter_fn (Callable): Filter function that will be called to filter the files shown in the
                        picker.  This function should take a string file_path as the argument. The return value
                        should be a bool, with True indicating the the file should be shown to the user in the file picker.
                
        """
    def set_multiline_okay(self, multiline_okay: bool):
        """
        Set the StringFiled to allow the newline character
        
                Args:
                    multiline_okay (bool): If True, allow newline character in strings.
                
        """
    def set_on_value_changed_fn(self, on_value_changed_fn: typing.Callable):
        """
        Set function that is called when the value of the StringField is modified
        
                Args:
                    on_value_changed_fn (Callable): Function that is called when the value of the StringField is modified.
                        Function should take a string as the argument. The return value will not be used.
                
        """
    def set_read_only(self, read_only: bool):
        """
        Set this StringField to be read only
        
                Args:
                    read_only (bool): If True, StringField cannot be modified through the UI; it can still be
                        modified programmatically with set_value()
                
        """
    def set_value(self, val: str):
        """
        Set the value of the StringField
        
                Args:
                    val (str): Value to fill StringField
                
        """
    @property
    def file_picker_btn(self) -> omni.ui._ui.Button:
        """
        
                Returns:
                    omni.ui.Button: Button to activate file picker
                
        """
    @property
    def file_picker_frame(self) -> omni.ui._ui.Frame:
        """
        
                Returns:
                    omni.ui.Frame: UI Frame containing FilePicker
                
        """
    @property
    def label(self) -> omni.ui._ui.Label:
        """
        
                Returns:
                    omni.ui.Label: UI Label element that contains the descriptive text
                
        """
    @property
    def string_field(self) -> omni.ui._ui.StringField:
        """
        
                Returns:
                    omni.ui.StringField: UI StringField element
                
        """
class TextBlock(isaacsim.gui.components.element_wrappers.base_ui_element_wrappers.UIWidgetWrapper):
    """
    Create a text block that is only modifiable through code. The user may not set
        the value of the text in the UI.
    
        Args:
            label (str): Short description of the contents of the TextBlock
            text (str, optional): Text to put in the TextBlock. Defaults to "".
            tooltip (str, optional): Text to appear when the mouse hovers over the TextBlock. Defaults to "".
            num_lines (int, optional): Number of lines that should be visible in the TextBlock at one time. Defaults to 5.
            include_copy_button (bool, optional): Include a copy_to_clipboard button. Defaults to True.
        
    """
    def __init__(self, label: str, text: str = '', tooltip: str = '', num_lines = 5, include_copy_button: bool = True):
        ...
    def _create_ui_widget(self, num_lines, label, text, tooltip, include_copy_btn):
        ...
    def get_text(self) -> str:
        """
        
                Returns:
                    str: Text in the text block
                
        """
    def set_num_lines(self, num_lines: int):
        """
        Set the number of lines that should be visible in the TextBlock at one time.
        
                Args:
                    num_lines (int): Number of lines that should be visible in the TextBlock at one time.
                
        """
    def set_text(self, text: str):
        """
        
                Args:
                    text (str): Set the text in the text block.
                
        """
    @property
    def copy_btn(self) -> omni.ui._ui.Button:
        """
        
                Returns:
                    omni.ui.Button: Copy Button.  If the TextBlock was built without a copy button, this will return None.
                
        """
    @property
    def label(self) -> omni.ui._ui.Label:
        """
        
                Returns:
                    omni.ui.Label: UI Label element that contains the descriptive text
                
        """
    @property
    def scrolling_frame(self) -> omni.ui._ui.ScrollingFrame:
        """
        
                Returns:
                    omni.ui.ScrollingFrame: Scrolling Frame that contains the TextBlock text
                
        """
    @property
    def text_block(self) -> omni.ui._ui.Label:
        """
        
                Returns:
                    omni.ui.Label: UI element that contains the text in the text block
                
        """
class XYPlot(isaacsim.gui.components.element_wrappers.base_ui_element_wrappers.UIWidgetWrapper):
    def __init__(self, label: str, tooltip: str = '', x_data: typing.Union[typing.List[typing.List], typing.List] = list(), y_data: typing.Union[typing.List[typing.List], typing.List] = list(), x_min: float = None, x_max: float = None, y_min: float = None, y_max: float = None, x_label: str = 'X', y_label: str = 'Y', plot_height: int = 10, show_legend: bool = False, legends: typing.List[str] = None, plot_colors: typing.List[typing.List[int]] = None):
        """
        Create an XY plot UI Widget with axis scaling, legends, and support for multiple plots.
                Overlapping data is most accurately plotted when centered in the frame with reasonable axis scaling.
                Pressing down the mouse gives the x and y values of each function at an x coordinate.
        
                Args:
                    label (str): Short descriptve text to the left of the plot
                    tooltip (str, optional): Tooltip to appear when hovering the mouse over the plot label. Defaults to "".
                    x_data (Union[List[List],List], optional): A possibly ragged list of lists where each ith inner list is the x coordinates for plot i.
                        For a single plot, the data may be provided as a list of floats.  x_data must have exactly the same shape as y_data.  Defaults to [].
                    y_data (Union[List[List],List], optional): A possibly ragged list of lists where each ith inner list is the y coordinates for plot i.
                        For a single plot, the data may be provided as a list of floats.  y_data must have exactly the same shape as x_data.  Defaults to [].
                    x_min (float, optional): Minimum value of x shown on the plot. If not specified, the minimum value found in x_data will be uesd. Defaults to None.
                    x_max (float, optional): Maximum value of x shown on the plot.  If not specified, the maximum value found in x_data will be used. Defaults to None.
                    y_min (float, optional): Minimum value of y shown on the plot. If not specified, the minimum value found in y_data will be uesd. Defaults to None.
                    y_max (float, optional): Maximum value of y shown on the plot.  If not specified, the maximum value found in y_data will be used. Defaults to None.
                    x_label (str, optional): Label of X axis. Defaults to "X".
                    y_label (str, optional): Label of Y axis. Defaults to "Y".
                    plot_height (int, optional): Height of the plot, proportional to the height of a line of text. Defaults to 10.
                    show_legend (bool, optional): Show a legend on the plot. Defaults to False.
                    legends (List[str], optional): Legend for the plotted data.  If not specified, names 'F_i(x)' will be automatically generated. Defaults to None.
                    plot_colors (List[List], optional): Colors of the plotted data.  The ith entry in plot_colors is considered to be a list of [r,g,b] values in [0,255] for the ith plot color.
                        If not specified, colors will be automatically generated.  Defaults to None.
                
        """
    def _build_widget(self):
        ...
    def _convert_hex_to_rgb(self, hex_color) -> typing.Tuple[int]:
        ...
    def _convert_rgb_to_hex(self, r, g, b) -> int:
        ...
    def _create_ui_widget(self):
        ...
    def _get_data_colors(self, num_colors) -> typing.List[int]:
        ...
    def _get_distinct_colors(self, num_colors) -> typing.List[int]:
        """
        
                This function returns a list of distinct colors for plotting.
        
                Args:
                    num_colors (int): the number of colors to generate
        
                Returns:
                    List[int]: a list of distinct colors in hexadecimal format 0xFFBBGGRR
                
        """
    def _get_fn_y_value(self, idx, x_value, decimals) -> float:
        ...
    def _get_interpolated_data(self, x_min = None, x_max = None):
        """
        Get all data necessary for plotting
        
                Returns:
                    x_fracs (np.array): (N x 2) corresponding to the fraction of x values that are covered by the min and max
                        x values for each plot
                    y_vals (np.array): (N x ?) a list of y values corresponding to each plot.  The shape may be ragged
                    x_min (float): minimum value of x to be shown in the plot
                    x_max (float): maximum value of x to be shown in the plot
                
        """
    def _get_ragged_data_max(self, data) -> float:
        ...
    def _get_ragged_data_min(self, data) -> float:
        ...
    def _mouse_moved_on_plot(self, x, y, *args):
        ...
    def _on_mouse_released(self, *args):
        ...
    def get_legends(self) -> typing.List[str]:
        """
        Get the legends for the plotted data.
        
                Returns:
                    List[str]: Legends for the plotted data
                
        """
    def get_plot_colors(self) -> typing.List[typing.List[int]]:
        """
        Get the colors of the data in the plot
        
                Returns:
                    List[List[int]]: List of lists where each inner list has length 3 corresponding to r,g,b values.
                
        """
    def get_plot_height(self) -> int:
        """
        Get the height of the plot, proportional to the height of a line of text
        
                Returns:
                    int: Height of the plot
                
        """
    def get_x_data(self) -> typing.List[typing.List[float]]:
        """
        x_data in the plot
        
                Returns:
                    List[List[float]]: A possibly ragged list of lists where each ith inner list is the x coordinates for plot i.
                
        """
    def get_x_max(self) -> float:
        """
        Get the maximum value of x shown in the plot.
        
                Returns:
                    float: Maximum value of x shown in the plot.
                
        """
    def get_x_min(self) -> float:
        """
        Get the minimum value of x shown in the plot.
        
                Returns:
                    float: Minimum value of x shown in the plot.
                
        """
    def get_y_data(self) -> typing.List[typing.List[float]]:
        """
        y_data in the plot
        
                Returns:
                    List[List[float]]: A possibly ragged list of lists where each ith inner list is the y coordinates for plot i.
                
        """
    def get_y_max(self) -> float:
        """
        Get the maximum value of y shown in the plot.
        
                Returns:
                    float: Maximum value of y shown in the plot.
                
        """
    def get_y_min(self) -> float:
        """
        Get the minimum value of y shown in the plot.
        
                Returns:
                    float: Minimum value of y shown in the plot.
                
        """
    def set_data(self, x_data: typing.Union[typing.List[typing.List], typing.List], y_data: typing.Union[typing.List[typing.List], typing.List]):
        """
        Set the data to plot
        
                Args:
                    x_data (Union[List[List],List]): A possibly ragged list of lists where each ith inner list is the x coordinates for plot i.
                        For a single plot, the data may be provided as a list of floats.  x_data must have exactly the same shape as y_data.
                    y_data (Union[List[List],List]): A possibly ragged list of lists where each ith inner list is the y coordinates for plot i.
                        For a single plot, the data may be provided as a list of floats.  y_data must have exactly the same shape as x_data.
                
        """
    def set_legend_by_index(self, idx: int, legend: str):
        """
        Set the legend for a specific plot whose index corresponds to the rows of x_data and y_data
        
                Args:
                    idx (int): Index of legend to set.
                    legend (str): Legend
                
        """
    def set_legends(self, legends: typing.List[str]):
        """
        Set legends for each plot.
        
                Args:
                    legends (List[str]): List of legends for each plot.
                
        """
    def set_plot_color_by_index(self, index: int, r: int, g: int, b: int):
        """
        Set the color of a specific plot.
        
                Args:
                    index (int): Index of the plot corresponding to the rows of x_data and y_data.
                    r (int): Value for red in [0,255]
                    g (int): Value for green in [0,255]
                    b (int): Value for blue in [0,255]
                
        """
    def set_plot_colors(self, plot_colors: typing.List[typing.List[int]]):
        """
        Set the colors for every plot
        
                Args:
                    plot_colors (List[List[int]]): A list of lists where each index corresponds to the rows of x_data and y_data.  Each inner list must
                        contain [r,g,b] color values in [0,255]
                
        """
    def set_plot_height(self, plot_height: int):
        """
        Set the height of the plot.
        
                Args:
                    plot_height (int): Height of the plot, proportional to the height of a line of text.
                
        """
    def set_plot_visible_by_index(self, index: int, visible: bool):
        """
        Hide or show a specific plot
        
                Args:
                    index (int): Index of plot to show
                    visible (bool):If True, show the plot, otherwise hide it.
                
        """
    def set_show_legend(self, show_legend: bool):
        """
        Hide or show the legend for this Widget
        
                Args:
                    show_legend (bool): If True, show a legend for the Widget.
                
        """
    def set_x_max(self, x_max: float):
        """
        Set maximum value of x shown on the plot.
                If this value is not greater than x_min, x_min will be updated to x_max - 1.
        
                Args:
                    x_max (float): Maximum value of x shown on the plot.
                
        """
    def set_x_min(self, x_min: float):
        """
        Set the minimum value of x shown on the plot.
                If this value is not less than x_max, x_max will be updated to x_min + 1.
        
                Args:
                    x_min (float): Minimum value of x shown on the plot.
                
        """
    def set_y_max(self, y_max: float):
        """
        Set maximum value of y shown on the plot.
                If this value is not greater than y_min, y_min will be updated to y_max - 1.
        
                Args:
                    y_max (float): Maximum value of y shown on the plot.
                
        """
    def set_y_min(self, y_min: float):
        """
        Set the minimum value of y shown on the plot.
                If this value is not less than y_max, y_max will be updated to y_min + 1.
        
                Args:
                    y_min (float): Minimum value of y shown on the plot.
                
        """
def get_prim_object_type(prim_path: str) -> typing.Optional[str]:
    """
    Get the dynamic control object type of the USD Prim at the given path.
    
        Copied over from isaacsim.core.utils.prims, to avoid a heavy dependency on UI elements.
    
        Example:
        
    """
BUTTON_WIDTH: int = 120
LABEL_HEIGHT: int = 18
LABEL_WIDTH: int = 160
inf: float  # value = inf
