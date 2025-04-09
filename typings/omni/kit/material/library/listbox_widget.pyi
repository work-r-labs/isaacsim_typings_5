"""
Simulated combobox widget with drop-down list of materials from stage class.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import copy as copy
import omni as omni
from omni.kit.material.library.search_widget import SearchWidget
from omni.kit.material.library.treeview_model import MaterialListDelegate
from omni.kit.material.library.treeview_model import MaterialListModel
from omni import ui
__all__: list = ['MaterialListBoxWidget']
class MaterialListBoxWidget:
    """
    Simulated combobox widget with drop-down list of materials from stage class.
    """
    def _MaterialListBoxWidget__on_key_pressed(self, key, mod, pressed):
        """
        Called when the user presses a key
        """
    def __init__(self, icon_path: str, index: int, on_click_fn: callable, theme: str, filter_fn: callable = None, get_materials_async_fn: callable = None):
        """
        Initialize class function.
        
                Args:
                    icon_path (str): path to icons, if None then omni.kit.material.library/data/icons will be used.
                    index (int): default item in combobox.
                    on_click_fn (callable): function called when combobox item changed.
                    theme (str): theme name, should be "NvidiaDark" or "NvidiaLight". Not wildly supported.
                    filter_fn (callable): filter function passed to MaterialListModel.
                    get_materials_async_fn (callable): override for default omni.kit.material.library.get_materials_from_stage_async callback.
                
        """
    def _execute(self, treeview):
        ...
    def _get_treeview_height(self):
        ...
    def _search_updated(self, string):
        ...
    def _select_index(self, treeview: omni.ui._ui.TreeView, model: omni.ui._ui.AbstractItemModel, index: int):
        ...
    def _select_next(self, treeview: omni.ui._ui.TreeView, model: omni.ui._ui.AbstractItemModel, after = True):
        ...
    def _update_list_model(self, new_list, percent, state):
        ...
    def build_ui(self):
        """
        
                Build UI for list box widget.
                
        """
    def clean(self):
        """
        Clean up widget.
        """
    def destroy(self):
        """
        Destroy class and cleanup.
        """
    def set_parent(self, parent: omni.ui._ui.Widget):
        """
        Set widget parent
        
                Args:
                    parent (ui.Widget): parent widget to pin widget to.
                
        """
    def set_selection_on_loading_complete(self, selection: str):
        """
        
                When loading material list is complete, select these materials in the list.
                
        """
