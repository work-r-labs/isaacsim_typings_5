"""
This module provides the ComboListBoxWidget class, which integrates a search field with a list box for item selection, and a function to create a searchable combo box widget.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.widget.searchable_combobox.combo_model import ComboBoxListDelegate
from omni.kit.widget.searchable_combobox.combo_model import ComboBoxListModel
from omni.kit.widget.searchable_combobox.search_widget import SearchWidget
from omni import ui
__all__: list = ['ComboListBoxWidget']
class ComboListBoxWidget:
    """
    A widget that combines a search field with a list box for item selection.
    
        This widget facilitates the selection of items from a list that can be filtered
        through a search interface. Users can type in the search widget to filter the
        items displayed in the list box below it. It supports customization through themes
        and delegates for item display.
    
        Args:
            search_widget: SearchWidget
                An instance of SearchWidget to handle search input.
            item_list: list
                A list of items to be displayed and filtered in the list box.
            theme: str
                The visual theme for the widget's appearance.
            window_id: str
                The identifier for the window; default is 'SearchableComboBoxWindow'.
            delegate: ui.AbstractItemDelegate
                Delegate for custom item rendering; defaults to ComboBoxListDelegate.
    """
    def __init__(self, search_widget: omni.kit.widget.searchable_combobox.search_widget.SearchWidget, item_list: list, theme: str, window_id: str = 'SearchableComboBoxWindow', delegate: omni.ui._ui.AbstractItemDelegate = ...):
        """
        A widget that combines a search field with a list box for item selection.
        
                This widget facilitates the selection of items from a list that can be filtered
                through a search interface. Users can type in the search widget to filter the
                items displayed in the list box below it. It supports customization through themes
                and delegates for item display.
        
                Args:
                    search_widget: SearchWidget
                        An instance of SearchWidget to handle search input.
                    item_list: list
                        A list of items to be displayed and filtered in the list box.
                    theme: str
                        The visual theme for the widget's appearance.
                    window_id: str
                        The identifier for the window; default is 'SearchableComboBoxWindow'.
                    delegate: ui.AbstractItemDelegate
                        Delegate for custom item rendering; defaults to ComboBoxListDelegate.
        """
    def _get_view_height(self):
        ...
    def _search_updated(self, string):
        ...
    def _select_index(self, comboview: omni.ui._ui.TreeView, model: omni.ui._ui.AbstractItemModel, index: int):
        ...
    def _select_next(self, comboview: omni.ui._ui.TreeView, model: omni.ui._ui.AbstractItemModel, after = True):
        ...
    def build_ui(self):
        """
        builds UI for the ComboListBoxWidget UI.
        """
    def clean(self):
        """
        Cleans up the ComboListBoxWidget and destroys models.
        """
    def destroy(self):
        """
        Destroys the ComboListBoxWidget widget.
        """
    def destroy_ui(self, visible):
        """
        destroys the ComboListBoxWidget UI.
        """
    def set_parent(self, parent):
        """
        Set the parent widget
        
                Args:
                    parent: prent widget.
        """
def build_searchable_combo_widget(combo_list: typing.List[str], combo_index: int, combo_click_fn: callable, widget_height: int, default_value: str, window_id: str = 'SearchableComboBoxWindow', delegate: omni.ui._ui.AbstractItemDelegate = ...) -> omni.kit.widget.searchable_combobox.search_widget.SearchWidget:
    """
    Creates a searchable combo box widget with a specified list of options.
    
        Args:
            combo_list (List[str]): List of string options to be included in the combo box.
            combo_index (int): Index of the currently selected item in the combo list.
            combo_click_fn (callable): Function to be called when an item in the combo box is clicked.
            widget_height (int): The height of the widget.
            default_value (str): The default value to be displayed when no item is selected.
            window_id (str, optional): The identifier for the window; default is 'SearchableComboBoxWindow'.
            delegate (ui.AbstractItemDelegate, optional): Delegate for custom item rendering; defaults to ComboBoxListDelegate().
    
        Returns:
            SearchWidget: An instance of the SearchWidget with an attached searchable combo box.
    """
