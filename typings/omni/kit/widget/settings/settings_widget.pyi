"""

Source for SettingType, SettingWidgetType, SettingsSearchableCombo, create_setting_widget, create_setting_widget_combo.
"""
from __future__ import annotations
import carb as carb
import enum
from enum import Enum
import omni as omni
from omni.kit.widget.settings.settings_model import AssetPathSettingsModel
from omni.kit.widget.settings.settings_model import RadioButtonSettingModel
from omni.kit.widget.settings.settings_model import SettingModel
from omni.kit.widget.settings.settings_model import SettingsComboItemModel
from omni.kit.widget.settings.settings_model import VectorFloatSettingsModel
from omni.kit.widget.settings.settings_model import VectorIntSettingsModel
from omni.kit.widget.settings.settings_widget_builder import SettingsWidgetBuilder
from omni import ui
import typing
__all__: list = ['SettingType', 'SettingWidgetType', 'create_setting_widget', 'create_setting_widget_combo', 'SettingsSearchableCombo']
class SettingType(enum.Enum):
    """
    
        Supported setting types for create_setting_widget.
        
    """
    ASSET: typing.ClassVar[SettingType]  # value = <SettingType.ASSET: 8>
    BOOL: typing.ClassVar[SettingType]  # value = <SettingType.BOOL: 3>
    COLOR3: typing.ClassVar[SettingType]  # value = <SettingType.COLOR3: 2>
    DOUBLE2: typing.ClassVar[SettingType]  # value = <SettingType.DOUBLE2: 7>
    DOUBLE3: typing.ClassVar[SettingType]  # value = <SettingType.DOUBLE3: 5>
    FLOAT: typing.ClassVar[SettingType]  # value = <SettingType.FLOAT: 0>
    INT: typing.ClassVar[SettingType]  # value = <SettingType.INT: 1>
    INT2: typing.ClassVar[SettingType]  # value = <SettingType.INT2: 6>
    STRING: typing.ClassVar[SettingType]  # value = <SettingType.STRING: 4>
class SettingWidgetType(enum.Enum):
    """
    
        Supported setting UI widget types
        
    """
    ASSET: typing.ClassVar[SettingWidgetType]  # value = <SettingWidgetType.ASSET: 8>
    BOOL: typing.ClassVar[SettingWidgetType]  # value = <SettingWidgetType.BOOL: 3>
    COLOR3: typing.ClassVar[SettingWidgetType]  # value = <SettingWidgetType.COLOR3: 2>
    COMBOBOX: typing.ClassVar[SettingWidgetType]  # value = <SettingWidgetType.COMBOBOX: 9>
    DOUBLE2: typing.ClassVar[SettingWidgetType]  # value = <SettingWidgetType.DOUBLE2: 7>
    DOUBLE3: typing.ClassVar[SettingWidgetType]  # value = <SettingWidgetType.DOUBLE3: 5>
    FLOAT: typing.ClassVar[SettingWidgetType]  # value = <SettingWidgetType.FLOAT: 0>
    INT: typing.ClassVar[SettingWidgetType]  # value = <SettingWidgetType.INT: 1>
    INT2: typing.ClassVar[SettingWidgetType]  # value = <SettingWidgetType.INT2: 6>
    RADIOBUTTON: typing.ClassVar[SettingWidgetType]  # value = <SettingWidgetType.RADIOBUTTON: 10>
    STRING: typing.ClassVar[SettingWidgetType]  # value = <SettingWidgetType.STRING: 4>
    VECTOR3: typing.ClassVar[SettingWidgetType]  # value = <SettingWidgetType.VECTOR3: 11>
class SettingsSearchableCombo:
    """
    
        Searchable combo box, needs omni.kit.widget.searchable_combobox extensions
        
    """
    @staticmethod
    def _on_setting_change(owner, item: carb.dictionary._dictionary.Item, event_type):
        ...
    def __init__(self, setting_path: str, key_value_pairs: dict, default_key: str):
        ...
    def _register_searchwidget(self):
        ...
    def _unregister_searchwidget(self):
        ...
    def destroy(self):
        """
        
                Destroy class and cleanup.
                
        """
    def get_current_key(self):
        """
        
                Gets current key selected in combo box.
                
        """
    def get_key_from_value(self, value):
        """
        
                Gets key from value.
                
        """
def create_setting_widget(setting_path: str, setting_type: SettingType, range_from = 0, range_to = 0, speed = 1, **kwargs) -> typing.Tuple[omni.ui._ui.Widget, omni.ui._ui.AbstractValueModel]:
    """
    
        Create a UI widget connected with a setting.
    
        If ``range_from`` >= ``range_to`` there is no limit. Undo/redo operations are also supported, because changing setting
        goes through the :mod:`omni.kit.commands` module, using :class:`.ChangeSettingCommand`.
    
        Args:
            setting_path: Path to the setting to show and edit.
            setting_type: Type of the setting to expect.
            range_from: Limit setting value lower bound.
            range_to: Limit setting value upper bound.
            speed: Range speed
    
        Returns:
            :class:`ui.Widget` and :class:`ui.AbstractValueModel` connected with the setting on the path specified.
        
    """
def create_setting_widget_combo(setting_path: str, items: typing.Union[list, dict], setting_is_index: typing.Optional[bool] = None, **kwargs) -> typing.Tuple[omni.kit.widget.settings.settings_model.SettingsComboItemModel, omni.ui._ui.ComboBox]:
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
            **kwargs: Additional keyword arguments to omni.ui Widget constructor
        
    """
