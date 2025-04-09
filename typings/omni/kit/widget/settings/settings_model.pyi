"""

Source for SettingModel, RadioButtonSettingModel, AssetPathSettingsModel, VectorFloatComponentModel, VectorIntComponentModel, VectorSettingsModel, VectorFloatSettingsModel, VectorIntSettingsModel, SettingsComboValueModel, SettingsComboNameValueItem, SettingsComboItemModel.
"""
from __future__ import annotations
import carb as carb
import omni as omni
from omni import ui
__all__: list = ['update_reset_button', 'SettingModel', 'RadioButtonSettingModel', 'AssetPathSettingsModel', 'VectorFloatComponentModel', 'VectorIntComponentModel', 'VectorSettingsModel', 'VectorFloatSettingsModel', 'VectorIntSettingsModel', 'SettingsComboValueModel', 'SettingsComboNameValueItem', 'SettingsComboItemModel']
class AssetPathSettingsModel(SettingModel):
    def get_resolved_path(self):
        """
        
                Get full path.
                
        """
class RadioButtonSettingModel(omni.ui._ui.SimpleStringModel):
    """
    Model for simple RadioButton widget. The setting value and options are strings.
    """
    def __init__(self, setting_path: str):
        """
        
                RadioButtonSettingModel init function.
        
                Args:
                    setting_path: Carb setting path to create a model for.
                                  RadioButton items are specified in carb.settings "{setting_path}/items"
                
        """
    def _execute_kit_change_setting_command(self, value, previous_value = None):
        ...
    def _get_items(self) -> tuple:
        """
        Return radiobutton items from carb.settings.
        """
    def _on_setting_change(self, _: carb.dictionary._dictionary.Item, event_type):
        """
        
                This gets called this if:
                + Something else changes the setting (e.g an undo command)
                + We also use as a debugging tool to make sure things were changed..
        
                Args:
                    _ (carb.dictionary.Item): Not used here.
                    event_type: use to filter
                
        """
    def _update_reset_button(self):
        ...
    def _value_changed(self, model):
        ...
    def get_value(self) -> str:
        """
        Return current selected item string/label.
        """
    def get_value_as_int(self) -> int:
        """
        Return current selected item idx.
        """
    def set_reset_button(self, button: omni.ui._ui.Rectangle):
        """
        
                Set reset button from ui.Rectangle.
                
        """
    def set_value(self, value: typing.Union[int, str], update_setting: bool = True):
        """
        Set given value as current selected
        
                Args:
                    value (int|str): Value to set. It can be either an int (index) or a string (label)
        
                Kwargs:
                    update_setting (bool): Update corresponding carb.setting. Default True.
                
        """
    @property
    def items(self) -> tuple:
        ...
    @property
    def setting_path(self):
        ...
class SettingModel(omni.ui._ui.AbstractValueModel):
    """
    
        Model for simple scalar/POD carb.settings
        
    """
    @staticmethod
    def _on_change(owner, value, event_type) -> None:
        ...
    def __init__(self, setting_path: str, draggable: bool = False):
        """
        
                SettingModel init function.
        
                Args:
                    setting_path: setting_path carb setting to create a model for
                    draggable: is it a numeric value you will drag in the UI?
                
        """
    def _get_value(self):
        ...
    def _on_dirty(self):
        ...
    def _update_reset_button(self):
        ...
    def begin_edit(self) -> None:
        ...
    def destroy(self):
        """
        
                Destroy class and cleanup.
                
        """
    def end_edit(self) -> None:
        ...
    def get_value(self):
        """
        
                Get current value
                
        """
    def get_value_as_bool(self) -> bool:
        """
        
                Get current value as bool
                
        """
    def get_value_as_float(self) -> float:
        """
        
                Get current value as float
                
        """
    def get_value_as_int(self) -> int:
        """
        
                Get current value as integer
                
        """
    def get_value_as_string(self) -> str:
        """
        
                Get current value as string
                
        """
    def set_range(self, min_val, max_val):
        """
        
                set the allowable range for the setting. This is more restrictive than the UI min/max setting
                which still lets you set out of range values using the keyboard (e.g click and type in slider)
                
        """
    def set_reset_button(self, button: omni.ui._ui.Rectangle):
        """
        
                Set reset button from ui.Rectangle.
                
        """
    def set_value(self, value: typing.Any):
        ...
class SettingsComboItemModel(omni.ui._ui.AbstractItemModel):
    """
    
        Model for a combo box - for each setting we have a dictionary of key, values
        
    """
    class ComboboxIndexModel(omni.ui._ui.SimpleIntModel):
        """
        
                A custom ui.SimpleIntModel that can handle value <-> index conversion when setting values.
                
        """
        def __init__(self, combobox_model, *args, **kwargs):
            ...
        def set_value(self, value, as_index = True):
            """
            Set the given index value to the model.
                        If the given value is not int type, it will try to find the index from the given value.
                        If the given value is int but as_index is False, it will still try to find the index
                        from the given value.
                        
            """
    @staticmethod
    def _on_setting_change(owner, item: carb.dictionary._dictionary.Item, event_type):
        """
        
                This gets called this if:
                + Something else changes the setting (e.g an undo command)
                + We also use as a debugging tool to make sure things were changed..
        
                Args:
                    owner: will be an instance of SettingsComboItemModel
                    item: ?
                    event_type: use to filter
                
        """
    def __init__(self, setting_path, key_value_pairs: typing.Dict[str, typing.Any], setting_is_index: bool = True):
        ...
    def _current_index_changed(self, model):
        ...
    def _update_reset_button(self):
        ...
    def destroy(self):
        """
        
                Destroy class and cleanup.
                
        """
    def get_item_children(self, item: omni.ui._ui.AbstractItem = None):
        """
        
                this is called by the widget when it needs the submodel items
                
        """
    def get_item_index(self, value: typing.Any) -> typing.Optional[int]:
        """
        Get the item index to the given value.
        
                Arg:
                    value (int|str|float): The value to set.
        
                Return:
                    (int|None) Item index. None if no item found.
                
        """
    def get_item_value_model(self, item: omni.ui._ui.AbstractItem = None, column_id: int = 0):
        ...
    def get_value(self) -> typing.Any:
        """
        Get current selected item value or index value if setting_is_index is True.
        
                Return:
                    (int|str|float) Current selected item value or index value depends
                              on the self._setting_is_index attribute.
                
        """
    def get_value_as_int(self) -> int:
        """
        Get current selected item index
                Return:
                    (int) Current selected item index
                
        """
    def get_value_as_string(self) -> str:
        """
        Get current selected item label string.
        
                Return:
                    (str) Current selected item label string.
                
        """
    def set_items(self, key_value_pairs: typing.Dict[str, typing.Any]):
        """
        
                Set items and refresh UI.
                
        """
    def set_reset_button(self, button: omni.ui._ui.Rectangle):
        """
        
                Set reset button from ui.Rectangle.
                
        """
    def set_value(self, value: typing.Any) -> typing.Optional[int]:
        """
        Set current selected to the given value
        
                Arg:
                    value (int|str|float): The value to set.
        
                Return:
                    (int|None) Item index set. None if no item found.
                
        """
    @property
    def setting_is_index(self):
        ...
class SettingsComboNameValueItem(omni.ui._ui.AbstractItem):
    """
    
        SettingsComboNameValueItem for combo boxes
        
    """
    def __init__(self, label: str, value: str):
        """
        
                SettingsComboNameValueItem init function.
                
        """
    def __repr__(self):
        ...
class SettingsComboValueModel(omni.ui._ui.AbstractValueModel):
    """
    
        Model to store a pair (label, value of arbitrary type) for use in a ComboBox
        
    """
    def __init__(self, label: str, value: typing.Any):
        """
        
                SettingsComboValueModel init function.
        
                Args:
                    label: what appears in the UI widget
                    value: the value corresponding to that label
                
        """
    def __repr__(self):
        ...
    def get_setting_value(self) -> typing.Union[str, int, float]:
        """
        
                we call this to get the value of the combo box item
                
        """
    def get_value_as_string(self) -> str:
        """
        
                this is called to get the label of the combo box item
                
        """
class VectorFloatComponentModel(omni.ui._ui.SimpleFloatModel):
    """
    
        VectorFloatComponentModel
        
    """
    def __init__(self, parent, vec_index, immediate_mode):
        """
        
                VectorFloatComponentModel init function.
                
        """
    def get_value_as_float(self):
        ...
    def set_range(self, min_val = None, max_val = None):
        """
        
                set the allowable range for the setting. This is more restrictive than the UI min/max setting
                which still lets you set out of range values using the keyboard (e.g click and type in slider)
                
        """
    def set_value(self, val):
        ...
class VectorFloatSettingsModel(VectorSettingsModel):
    def __init__(self, setting_path: str, component_count: int, immediate_mode: bool = True):
        ...
    def end_edit(self, item):
        ...
    def get_value(self) -> tuple:
        """
        Return current float values tuple.
        """
class VectorIntComponentModel(omni.ui._ui.SimpleIntModel):
    def __init__(self, parent, vec_index, immediate_mode):
        """
        
                VectorIntComponentModel init function.
                
        """
    def get_value_as_int(self):
        ...
    def set_value(self, val):
        ...
class VectorIntSettingsModel(VectorSettingsModel):
    def __init__(self, setting_path: str, component_count: int, immediate_mode: bool = True):
        ...
    def end_edit(self, item):
        ...
    def get_value(self) -> tuple:
        """
        Return current int values tuple.
        """
class VectorSettingsModel(omni.ui._ui.AbstractItemModel):
    """
    
        Model For Color, Vec3 and other multi-component settings
        Assumption is the items are draggable, so we only store a command when the dragging has completed.
    
        TODO: Needs testing with component_count = 2,4
        
    """
    @staticmethod
    def _on_change(owner, item: carb.dictionary._dictionary.Item, event_type: carb.settings._settings.ChangeEventType):
        """
        
                when an undo, reset_to_default or other change to the setting happens outside this model
                update the component child models
                
        """
    def __init__(self, setting_path: str, component_count: int, item_class: omni.ui._ui.AbstractItemModel, immediate_mode: bool):
        """
        
                VectorSettingsModel init function.
        
                Args:
                    setting_path: setting_path carb setting to create a model for
                    component_count: how many elements does the setting have?
                    immediate_mode: do we update the underlying setting immediately, or wait for endEdit
                
        """
    def _update_reset_button(self):
        ...
    def begin_edit(self, item: omni.ui._ui.AbstractItem):
        """
        
                Stub: need implementation to prevent crashes.
                
        """
    def destroy(self):
        """
        
                Destroy class and cleanup.
                
        """
    def end_edit(self, item):
        ...
    def get_item_children(self, item: omni.ui._ui.AbstractItem = None):
        """
        
                this is called by the widget when it needs the submodel items
                
        """
    def get_item_value_model(self, sub_model_item: omni.ui._ui.AbstractItem = None, column_id: int = 0):
        """
        
                This is called by the widget when it needs the submodel item models.
                (to then get or set them)
                
        """
    def set_reset_button(self, button: omni.ui._ui.Rectangle):
        """
        
                Set reset button from ui.Rectangle.
                
        """
    def set_value(self, values: typing.Union[tuple, list]):
        """
        Set list of values to the model.
        """
def update_reset_button(settingModel):
    """
    
        work out whether to show the reset button highlighted or not depending on whether the setting
        is set to it's default value
        
    """
