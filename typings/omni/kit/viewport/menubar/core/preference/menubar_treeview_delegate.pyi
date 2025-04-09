from __future__ import annotations
import omni.kit.viewport.menubar.core.menu_item.viewport_menu_item
from omni.kit.viewport.menubar.core.menu_item.viewport_menu_item import ViewportMenuItem
from omni.kit.viewport.menubar.core.model.combobox_model import SettingComboBoxModel
from omni.kit.viewport.menubar.core.model.reset_button import ResetButton
from omni import ui
import omni.ui._ui
__all__: list = ['AlignmentImages', 'MenubarTreeViewDelegate']
class AlignmentImages:
    def __init__(self, left: bool, on_alignment_changed: typing.Callable[[bool], NoneType], icon_size: int = 20):
        ...
class MenubarTreeViewDelegate(omni.ui._ui.AbstractItemDelegate):
    """
    
        Delegate is the representation layer.
        TreeView calls the methods of the delegate to create custom widgets for each item.
        
    """
    def __init__(self):
        ...
    def _on_alignment_changed(self, model: <function singleton.<locals>.getinstance at 0x709ef21dcca0>, item: omni.kit.viewport.menubar.core.menu_item.viewport_menu_item.ViewportMenuItem, left: bool):
        ...
    def _on_reset(self, model: <function singleton.<locals>.getinstance at 0x709ef21dcca0>, item: omni.kit.viewport.menubar.core.menu_item.viewport_menu_item.ViewportMenuItem):
        ...
    def build_branch(self, model, item, column_id, level, expanded):
        """
        Create a branch widget that opens or closes subtree
        """
    def build_widget(self, model: <function singleton.<locals>.getinstance at 0x709ef21dcca0>, item: omni.kit.viewport.menubar.core.menu_item.viewport_menu_item.ViewportMenuItem, column_id, level, expanded):
        """
        Create a widget per column per item
        """
    def destroy(self):
        ...
