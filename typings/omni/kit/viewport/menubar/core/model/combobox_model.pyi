from __future__ import annotations
import carb as carb
import collections as collections
from omni import ui
import omni.ui._ui
import weakref as weakref
__all__: list = ['ComboBoxItem', 'ComboBoxModel', 'SettingComboBoxModel']
class ComboBoxItem(omni.ui._ui.AbstractItem):
    """
    A data item for a single item in combobox drop list.
    """
    def __init__(self, text: str, value: typing.Any) -> None:
        """
        
                Constructor.
        
                Args:
                    text (str): Item text.
                    value (Any): Item value.
                
        """
class ComboBoxModel(omni.ui._ui.AbstractItemModel):
    """
    A data model for items in combobox drop list.
    """
    def __init__(self, texts: typing.List[str], values: typing.Optional[typing.List[typing.Any]] = None, current_value: typing.Any = None):
        """
        
                Constructor.
        
                Args:
                    texts (List[str]): Texts displayed in combobox
        
                Keyword Args:
                    values (Optional[List[Any]]): Values for combobox list, default to None to use text as value
                    current_value (Any): Current value displayed in combobox, defaults to None to use first one.
                
        """
    def _get_current_index_by_value(self, value: typing.Any, default: int = 0) -> int:
        ...
    def _on_current_item_changed(self, item: ComboBoxItem) -> None:
        ...
    def destroy(self) -> None:
        """
        Release resources
        """
    def get_item_children(self, item: typing.Optional[omni.kit.viewport.menubar.core.model.combobox_model.ComboBoxItem]) -> typing.List[omni.kit.viewport.menubar.core.model.combobox_model.ComboBoxItem]:
        """
        
                Returns all the children when the widget asks it.
        
                Args:
                    item (Optional[ComboBoxItem]): Parent itemd, defaults to None means to retrieve root items.
                
        """
    def get_item_value_model(self, item: typing.Optional[omni.kit.viewport.menubar.core.model.combobox_model.ComboBoxItem], column_id: int):
        """
        
                Retrieve item value model.
        
                Args:
                    item (Optional[ComboBoxItem]): Combobox item.
                    column_id (int): Column index.
                
        """
    def on_current_changed(self):
        """
        Callback when current selection in combobox changed
        """
class SettingComboBoxModel(ComboBoxModel):
    """
    A data model for items in combobox drop list and get/set value from/to a setting path.
    """
    def _SettingComboBoxModel__on_seq_change(self, tree_item, changed_item, event_type) -> None:
        ...
    def __init__(self, setting_path: str, texts: typing.List[str], values: typing.Optional[typing.List[typing.Any]] = None, current_value: typing.Any = None):
        """
        
                Constructor.
        
                Args:
                    setting_path (str): Setting path
                    texts (List[str]): Texts displayed in combobox
        
                keyword Args:
                    values (Optional[List[Any]]): Values for combobox list, defaults to None to use text as value.
                
        """
    def _on_change(self, tree_item, event_type) -> None:
        ...
    def _on_current_item_changed(self, item: ComboBoxItem) -> None:
        ...
    def destroy(self) -> None:
        """
        Release resources.
        """
