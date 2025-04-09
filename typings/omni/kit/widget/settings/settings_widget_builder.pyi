"""

Source for SettingsWidgetBuilder, AssetPicker.
"""
from __future__ import annotations
import carb as carb
import collections as collections
from functools import partial
import omni as omni
from omni.kit.widget.settings.settings_model import RadioButtonSettingModel
from omni.kit.widget.settings.settings_model import SettingsComboItemModel
from omni import ui
from pathlib import Path
import typing
__all__: list = ['LABEL_HEIGHT', 'HORIZONTAL_SPACING', 'LABEL_WIDTH', 'SettingsWidgetBuilder', 'AssetPicker']
class AssetPicker:
    """
    
        AssetPicker class.
        
    """
    @classmethod
    def get_icon_path(cls):
        """
        
                Get icon path for extension
                
        """
    def __init__(self, model):
        """
        
                AssetPicker init function.
                
        """
    def _on_file_pick(self, dialog, filename: str, dirname: str):
        """
        
                When a file or folder is selected in the dialog.
                
        """
    def build_ui(self, additional_widget_kwargs: typing.Optional[dict] = None):
        """
        
                Build UI for asset picker.
                
        """
    def on_show_dialog(self, model, item_filter_options):
        """
        
                Browse button clicked function.
                
        """
class SettingsWidgetBuilder:
    """
    
        Widget builder functions.
        
    """
    _checkbox_alignment: typing.ClassVar[str] = 'left'
    _checkbox_alignment_set: typing.ClassVar[bool] = True
    _label_alignment: typing.ClassVar[str] = 'left'
    _label_alignment_set: typing.ClassVar[bool] = True
    @staticmethod
    def _create_drag_or_slider(drag_widget, slider_widget, **kwargs):
        """
        
                A drag_widget lets you click and drag (you can drag as far left or right on the screen as you like)
                You can double-click to manually enter a value
        
                A slider_widget lets you click and sets the value to where you clicked.
                You don't drag outside the screen space occupied by the widget.
                No double click support.
                You press Ctrl-Click to manually enter a value
        
                This method will use a slider_widget when the range is <100 and a slider otherwise
                
        """
    @staticmethod
    def _create_multi_float_drag_with_labels(model, labels, comp_count, **kwargs) -> None:
        ...
    @staticmethod
    def _create_multi_int_drag_with_labels(model, labels, comp_count, **kwargs) -> None:
        ...
    @staticmethod
    def _get_setting(setting_path: str, setting_name: str = '', default: typing.Any = None) -> typing.Any:
        """
        Get the configuration of an UI widget carb.settings. This method assumes the given "setting_path" points
                to a value that has the given "setting_name" setting lives aside with it as a sibling.
        
                Args:
                    setting_path (str): The base setting path.
                    setting_name (str): The setting name the query.
                Kwargs:
                    default (Any): The value to return if the setting doesn't exist or is None.
        
                Return:
                    (Any): Setting value.
                
        """
    @classmethod
    def _build_reset_button(cls, path) -> omni.ui._ui.Rectangle:
        ...
    @classmethod
    def _create_label(cls, attr_name, path, tooltip = '', additional_label_kwargs = None):
        ...
    @classmethod
    def _restore_defaults(cls, path: str, button = None) -> None:
        ...
    @classmethod
    def createAssetWidget(cls, model, additional_widget_kwargs: typing.Optional[dict] = None):
        """
        
                Create widget for file asset with filepicker.
                
        """
    @classmethod
    def createBoolWidget(cls, model, additional_widget_kwargs: typing.Optional[dict] = None):
        """
        
                Create a boolean widget.
                
        """
    @classmethod
    def createColorWidget(cls, model, comp_count = 3, additional_widget_kwargs: typing.Optional[dict] = None) -> omni.ui._ui.HStack:
        """
        
                Create a three color floating-point widget.
                
        """
    @classmethod
    def createComboboxWidget(cls, setting_path: str, items: typing.Union[list, dict, NoneType] = None, setting_is_index: typing.Optional[bool] = None, additional_widget_kwargs: typing.Optional[dict] = None) -> typing.Tuple[omni.kit.widget.settings.settings_model.SettingsComboItemModel, omni.ui._ui.ComboBox]:
        """
        
                Create a Combo Setting widget.
        
                This function creates a combo box that shows a provided list of names and it is connected with setting by path
                specified. Underlying setting values are used from values of `items` dict.
        
                Args:
                    setting_path: Path to the setting to show and edit.
                    items: Can be either :py:obj:`dict` or :py:obj:`list`. For :py:obj:`dict` keys are UI displayed names, values are
                        actual values set into settings. If it is a :py:obj:`list` UI displayed names are equal to setting values.
                    setting_is_index:
                        None - Detect type from setting_path value. If the type is int, set to True.
                        True - setting_path value is index into items list (default)
                        False - setting_path value is string in items list
                
        """
    @classmethod
    def createDoubleArrayWidget(cls, model, range_min, range_max, comp_count = 3, additional_widget_kwargs: typing.Optional[dict] = None):
        """
        
                Create a widget for multiple double-precision floating-point numbers.
                
        """
    @classmethod
    def createFloatWidget(cls, model, range_min, range_max, additional_widget_kwargs: typing.Optional[dict] = None):
        """
        
                Create a floating point widget.
                
        """
    @classmethod
    def createIntArrayWidget(cls, model, range_min, range_max, comp_count = 3, additional_widget_kwargs: typing.Optional[dict] = None):
        """
        
                Create a widget for multiple integer numbers.
                
        """
    @classmethod
    def createIntWidget(cls, model, range_min, range_max, additional_widget_kwargs: typing.Optional[dict] = None):
        """
        
                Create a integer widget.
                
        """
    @classmethod
    def createRadiobuttonWidget(cls, model: omni.kit.widget.settings.settings_model.RadioButtonSettingModel, setting_path: str = '', additional_widget_kwargs: typing.Optional[dict] = None) -> omni.ui._ui.RadioCollection:
        """
        
                Create a RadioButtons Setting widget.
        
                This function creates a Radio Buttons that shows a list of names that are connected with setting by path
                specified - "{setting_path}/items".
        
                Args:
                    model: A RadioButtonSettingModel instance.
                    setting_path: Path to the setting to show and edit.
        
                Return:
                    (omni.ui.RadioCollection): A omni.ui.RadioCollection instance.
                
        """
    @classmethod
    def createVecWidget(cls, model, range_min, range_max, comp_count = 3, additional_widget_kwargs: typing.Optional[dict] = None):
        """
        
                Create a widget for multiple XYZW float values.
                
        """
    @classmethod
    def get_checkbox_alignment(cls):
        """
        
                Get checkbox alignment from setting "/ext/omni.kit.window.property/checkboxAlignment" and return True/False
                
        """
    @classmethod
    def get_label_alignment(cls):
        """
        
                Get label alignment from setting "/ext/omni.kit.window.property/labelAlignment" and return True/False
                
        """
HORIZONTAL_SPACING: int = 4
LABEL_HEIGHT: int = 18
LABEL_WIDTH: int = 200
