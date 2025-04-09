from __future__ import annotations
import carb as carb
from collections import namedtuple
from isaacsim.gui.components.style import get_style
import omni as omni
from omni.kit.property.usd.relationship import RelationshipTargetPicker
from omni.kit.window.popup_dialog.dialog import get_field_value
from omni import ui
__all__ = ['BUTTON_WIDTH', 'DynamicComboBoxItem', 'DynamicComboBoxModel', 'LABEL_WIDTH', 'ParamWidget', 'RelationshipTargetPicker', 'SelectPrimWidget', 'carb', 'get_field_value', 'get_style', 'namedtuple', 'omni', 'ui']
class DynamicComboBoxItem(omni.ui._ui.AbstractItem):
    def __init__(self, text):
        ...
class DynamicComboBoxModel(omni.ui._ui.AbstractItemModel):
    def __init__(self, args):
        ...
    def get_item_children(self, item):
        ...
    def get_item_value_model(self, item: omni.ui._ui.AbstractItem = None, column_id: int = 0):
        ...
    def set_item_value_model(self, item: omni.ui._ui.AbstractItem = None, column_id: int = 0):
        ...
class ParamWidget:
    """
    
            modified FormWidget (from omni.kit.window.popup_dialog.form_dialog) to better format for parameter collection use
    
        Note:
            ParamWidget.FieldDef:
                A namedtuple of (name, label, type, default value) for describing the input field,
                e.g. FormDialog.FieldDef("name", "Name:  ", omni.ui.StringField, "Bob").
    
        
    """
    FieldDef = FormDialogFieldDef
    def __init__(self, field_def: FormDialogFieldDef):
        ...
    def _build_ui(self, field_def):
        ...
    def destroy(self):
        ...
    def get_value(self):
        ...
class SelectPrimWidget:
    """
    
        modeled after FormWidget (from omni.kit.window.popup_dialog.form_dialog) to add a widget that opens relationship selector
        
    """
    def __init__(self, label: str = None, default: str = None, tooltip: str = ''):
        ...
    def _build_ui(self):
        ...
    def _on_select_prim(self):
        ...
    def _on_target_selected(self, paths):
        ...
    def destroy(self):
        ...
    def get_value(self):
        ...
BUTTON_WIDTH: int = 120
LABEL_WIDTH: int = 160
