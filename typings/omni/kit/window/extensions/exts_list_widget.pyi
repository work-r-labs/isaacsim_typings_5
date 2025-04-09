"""
This module provides a UI for managing and interacting with extensions, allowing users to search, filter, sort, and perform actions on extensions within a list view.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import collections
from collections import OrderedDict
from collections import defaultdict
import contextlib as contextlib
import enum
from enum import IntFlag
import fnmatch as fnmatch
from functools import lru_cache
import omni as omni
from omni.kit.widget.filter.filter import FilterButton
from omni.kit.widget.options_menu.option_item import OptionItem
from omni.kit.widget.options_menu.option_separator import OptionSeparator
from omni.kit.window.extensions.common import ExtAuthorGroup
from omni.kit.window.extensions.common import ExtSource
from omni.kit.window.extensions.common import ExtensionCommonInfo
from omni.kit.window.extensions.common import PageBase
from omni.kit.window.extensions.common import get_categories
from omni.kit.window.extensions.common import is_community_tab_enabled
from omni.kit.window.extensions.common import is_version_locked_exts
from omni.kit.window.extensions.ext_components import ExtSourceSelector
from omni.kit.window.extensions.ext_components import ExtensionToggle
from omni.kit.window.extensions.ext_components import SearchWidget
from omni.kit.window.extensions.ext_controller import are_featured_exts_enabled
from omni.kit.window.extensions.ext_controller import get_default_search_words
from omni.kit.window.extensions.utils import get_ext_info_dict
from omni.kit.window.extensions.utils import get_extpath_git_ext
from omni import ui
import typing
__all__: list = list()
class ExtAuthorGroupItem(ExtGroupItem):
    def __init__(self, name, author_group: ExtAuthorGroup):
        ...
    def contains(self, ext_summary):
        ...
    def is_expanded_by_default(self):
        ...
class ExtCoreGroupItem(ExtGroupItem):
    def contains(self, ext_summary: ExtSummaryItem):
        ...
class ExtDeprecatedGroupItem(ExtGroupItem):
    def contains(self, ext_summary: ExtSummaryItem):
        ...
    def is_expanded_by_default(self):
        ...
class ExtGroupItem(omni.ui._ui.AbstractItem):
    """
    A class representing a group of extensions in a UI list.
    
        This class holds information about an extension group, including its name, total item count, and
        associated items, in the context of a UI application that manages extensions.
    
        Args:
            name (str): The display name for the extension group.
    """
    def __init__(self, name):
        """
        Initializes a new instance of the ExtGroupItem with a given name.
        """
    def contains(self, ext_summary):
        """
        Checks if the given extension summary is contained within the group.
        
                ext_summary (:obj:`ExtensionCommonInfo`): The extension summary to be checked against the group.
        """
    def is_expanded_by_default(self):
        """
        Determines if the group should be expanded by default when displayed.
        """
class ExtInternalGroupItem(ExtGroupItem):
    def contains(self, ext_summary: ExtSummaryItem):
        ...
class ExtNonToggleableGroupItem(ExtGroupItem):
    def contains(self, ext_summary):
        ...
    def is_expanded_by_default(self):
        ...
class ExtSampleGroupItem(ExtGroupItem):
    def contains(self, ext_summary: ExtSummaryItem):
        ...
class ExtSummariesModel(omni.ui._ui.AbstractItemModel):
    """
    Extension summary model that watches the changes in ext manager.
    
        This model provides an organized view of extensions, including filtering,
        sorting, and categorization features. It keeps track of extension states and
        updates the view accordingly when changes are detected.
    
        Args:
            flat (Optional[bool]): If set to True, the model will flatten the hierarchy of extension groups.
    """
    class SortDirection(enum.IntFlag):
        """
        An enumeration to define sorting directions.
        
                This enumeration provides flags to specify the sorting order for items, such as ascending or descending.
        
                Members:
                NONE: No sorting direction.
                Ascending: Items should be sorted in ascending order.
                Descending: Items should be sorted in descending order.
        """
        Ascending: typing.ClassVar[ExtSummariesModel.SortDirection]  # value = <SortDirection.Ascending: 1>
        Descending: typing.ClassVar[ExtSummariesModel.SortDirection]  # value = <SortDirection.Descending: 2>
        NONE: typing.ClassVar[ExtSummariesModel.SortDirection]  # value = <SortDirection.NONE: 0>
    def __init__(self, flat = None):
        """
        Initializes a new instance of ExtSummariesModel.
        """
    def _delayed_expand(self):
        ...
    def _make_sure_sorted(self):
        ...
    def _refresh_item_group_lists(self):
        ...
    def _refresh_once_with_delay(self, delay: float):
        """
        Call refresh once after `delay` seconds. If called again before `delay` is passed the timer gets reset.
        """
    def _resync_exts(self):
        ...
    def delayed_expand(self):
        ...
    def destroy(self):
        """
        Cleans up resources and references held by the ExtSummariesModel.
        """
    def filter_by_text(self, filters):
        """
        Specify the filter string that is used to reduce the model
        
                Args:
                    filter_name_text (str): The text to filter by.
                    filters (list): Additional filters to apply.
        """
    def get_item_children(self, item):
        """
        Reimplemented from AbstractItemModel
        
                Args:
                    item: The parent item whose children are to be retrieved.
        
                Returns:
                    A list of child items.
        """
    def get_item_value_model(self, item, column_id):
        """
        Gets the value model for a given item and column.
        
                Args:
                    item: The item for which the value model is requested.
                    column_id (int): The column identifier.
        
                Returns:
                    The requested value model.
        """
    def get_item_value_model_count(self, item):
        """
        Gets the count of value models for a given item.
        
                Args:
                    item: The item for which the value model count is requested.
        
                Returns:
                    The count of value models for the item.
        """
    def refresh_all(self):
        ...
    def resync_registry(self):
        ...
    def select_category(self, filter_category):
        """
        Selects a specific category to filter the extensions by.
        
                Args:
                    filter_category (str): The category to filter by.
        """
    def select_ext_source(self, ext_source):
        """
        Selects a specific extension source to filter the extensions by.
        
                Args:
                    ext_source (ExtSource): The extension source to filter by.
        """
    def sort_by_attr(self, attr: str):
        """
        Sorts the model by a specified attribute.
        
                Args:
                    attr (str): The attribute to sort by.
        """
    def sort_direction(self, direction: SortDirection):
        """
        Sets the sort direction for the model.
        
                Args:
                    direction (SortDirection): The direction to sort by.
        """
class ExtSummaryItem(omni.ui._ui.AbstractItem):
    """
    An abstract item that represents an extension summary
    """
    def __init__(self, ext_summary: dict):
        ...
class ExtToggleableGroupItem(ExtGroupItem):
    def contains(self, ext_summary):
        ...
class ExtensionCardWidget:
    """
    A UI widget for displaying extension cards in a list.
    
        This widget is responsible for creating the visual representation of an extension summary item.
        It includes methods for building different parts of an extension card, such as the body,
        footer, and the list item itself. The widget is used in the context of a larger UI structure
        that displays a list of extensions, allowing users to view and interact with extensions
        available in the system.
    """
    @staticmethod
    def build_ext_card_body(item: ExtSummaryItem):
        """
        Builds the extension card body UI for a given extension item.
        
                Args:
                    item (:obj:`ExtSummaryItem`): The extension summary item to build the UI for.
        """
    @staticmethod
    def build_ext_card_footer(item: ExtSummaryItem, height = 0, full_width = False):
        """
        Builds the extension card footer UI for a given extension item.
        
                Args:
                    item (:obj:`ExtSummaryItem`): The extension summary item to build the UI for.
                    height (int): The height of the footer area.
                    full_width (bool): Whether the footer should span the full width of the card.
        """
    @staticmethod
    def build_ext_list_item(item: ExtSummaryItem):
        """
        Builds the UI list item for a given extension item.
        
                Args:
                    item (:obj:`ExtSummaryItem`): The extension summary item to build the UI for.
        """
class ExtsDelegate(omni.ui._ui.AbstractItemDelegate):
    """
    A delegate class used within the omni.kit.window.extensions-1.2.7 extension UI.
    
        This class is responsible for rendering the items within the extensions list. It handles the creation of widgets for each extension item and their groups, as well as the visuals for expanded or collapsed state of groups in the list.
    
        The class works in conjunction with the ExtSummariesModel, which provides the data for the extensions, and the ExtensionCardWidget, which provides the layout for each extension item.
    
        The delegate utilizes the ui.AbstractItemDelegate interface to manage the widgets displayed in the UI. It overrides the build_branch, build_widget, and build_header methods to provide the necessary functionality for the extensions list UI.
        
    """
    def _build_group_widget(self, item, expanded):
        ...
    def build_branch(self, model, item, column_id, level, expanded):
        """
        ui.AbstractItemDelegate API: Create a branch widget that opens or closes subtree
        
                Args:
                    model: The model associated with the tree view.
                    item: The item for which to build the branch.
                    column_id: The column identifier.
                    level: The indentation level of the branch.
                    expanded: Whether the branch is expanded or not.
        """
    def build_header(self, column_id):
        """
        Builds the header for a given column.
        
                Args:
                    column_id: The column identifier.
        """
    def build_widget(self, model, item, column_id, level, expanded):
        """
        ui.AbstractItemDelegate API: Create a widget per column
        
                Args:
                    model: The model associated with the tree view.
                    item: The item for which to build the widget.
                    column_id: The column identifier.
                    level: The indentation level of the widget.
                    expanded: Whether the branch is expanded or not.
        """
class ExtsListWidget:
    """
    A widget for listing and interacting with extensions.
    
        This widget provides functionalities to create, search, filter, sort, and
        interact with extensions in a list view. It supports operations such as
        refreshing the list, resyncing the registry, importing extensions, and
        accessing extension settings. Additional features include displaying
        extension cards with detailed information, categorization of extensions, and
        a search field with advanced filtering capabilities.
    """
    menu_style: typing.ClassVar[dict] = {'padding': 2, 'Menu.Item.CheckMark': {'color': 'shade:4294952756'}, 'Titlebar.Background': {'background_color': 'shade:4280492319'}, 'Titlebar.Title': {'color': 'shade:4286874756'}, 'Titlebar.Reset': {'background_color': 0}, 'Titlebar.Reset.Label': {'color': 'shade:4289300014'}, 'Titlebar.Reset.Label:hovered': {'color': 'shade:4294952756'}}
    menus: typing.ClassVar[list] = [SearchMenuPage, SortMenuPage, OptionsMenuPage]
    searches: typing.ClassVar[collections.OrderedDict]  # value = OrderedDict([('@startup', ('Startup', <function ExtsListWidget.<lambda> at 0x709ef2da8820>, None)), ('@update', ('Update Available', <function ExtsListWidget.<lambda> at 0x709ef2da88b0>, None)), ('_1', (None, None, None)), ('@enabled', ('Enabled', <function ExtsListWidget.<lambda> at 0x709ef2da8940>, None)), ('@nontoggleable', ('Non-Toggleable', <function ExtsListWidget.<lambda> at 0x709ef2da89d0>, None)), ('_3', (None, None, None)), ('@feature', ('Featured', <function ExtsListWidget.<lambda> at 0x709ef2da8a60>, None)), ('@bundled', ('Bundled', <function ExtsListWidget.<lambda> at 0x709ef2da8af0>, None)), ('@app', ('App', <function ExtsListWidget.<lambda> at 0x709ef2da8b80>, None)), ('_4', (None, None, None)), ('@installed', ('Installed', <function ExtsListWidget.<lambda> at 0x709ef2da8c10>, None)), ('@remote', ('Remote', <function ExtsListWidget.<lambda> at 0x709ef2da8ca0>, None))])
    @classmethod
    def build_menu_header(cls, title, clicked_fn):
        ...
    def __init__(self):
        """
        Initializes the ExtsListWidget with default settings.
        """
    def _on_ext_list_refresh(self):
        ...
    def _on_key_pressed(self, key, mod, pressed):
        """
        Allow up/down arrow to be used to select prev/next extension
        """
    def _on_selection_changed(self, selection):
        ...
    def _resync_registry(self):
        ...
    def _select_category(self, category: str):
        """
        Set the category to show
        """
    def _select_ext_source(self, ext_source):
        ...
    def _show_dependencies(self):
        ...
    def _show_properties(self):
        ...
    def build(self):
        """
        Builds the main UI elements of the ExtsListWidget.
        """
    def close_filter_menu(self):
        """
        Closes the filter menu.
        """
    def destroy(self):
        """
        Cleans up the ExtsListWidget and releases any associated resources.
        """
    def get_model(self):
        ...
    def rebuild_filter_menu(self):
        """
        Rebuilds the filter menu based on current filter settings.
        """
    def select_extension_by_name(self, name: str):
        """
        {'Args': {'name (str)': 'The name of the extension to select in the list.'}}
        """
    def set_ext_selected_fn(self, fn: typing.Callable):
        """
        {'Args': {'fn (Callable)': 'The function to be called when an extension is selected from the list.'}}
        """
    def set_show_dependencies_fn(self, fn: typing.Callable):
        """
        {'Args': {'fn (Callable)': "The function to be called when the 'Show Extension Dependencies' option is selected."}}
        """
    def set_show_properties_fn(self, fn: typing.Callable):
        """
        {'Args': {'fn (Callable)': "The function to be called when the 'Settings' option is selected."}}
        """
class OptionsMenuPage(omni.kit.window.extensions.common.PageBase):
    @staticmethod
    def get_tab_name():
        ...
    def __init__(self, owner_cls = None):
        ...
    def build_tab(self, ext_info, ext_item: bool):
        ...
    def destroy(self):
        ...
    def rebuild_options_menu(self):
        """
        Rebuilds the options menu for the extension list.
        """
    def sort_index(self):
        ...
class SearchMenuPage(omni.kit.window.extensions.common.PageBase):
    @staticmethod
    def get_tab_name():
        ...
    def _SearchMenuPage__update_filter(self, search_key: str) -> None:
        ...
    def __init__(self, owner_cls = None):
        ...
    def _build_filter_button(self):
        ...
    def _build_filter_items(self) -> list[OptionItem]:
        ...
    def _filter_by_text(self, search_words: list[str] | None):
        """
        Set the search filter string to the models and widgets
        """
    def build_tab(self, ext_info, ext_item: bool):
        ...
    def close_menu(self):
        """
        Closes the filter menu.
        """
    def destroy(self):
        ...
    def rebuild_filter_menu(self):
        """
        Rebuilds the filter menu based on current filter settings.
        """
    def sort_index(self):
        ...
class SortMenuPage(omni.kit.window.extensions.common.PageBase):
    @staticmethod
    def get_tab_name():
        ...
    def __init__(self, owner_cls = None):
        ...
    def build_tab(self, ext_info, ext_item: bool):
        ...
    def destroy(self):
        ...
    def rebuild_sortby_menu(self):
        """
        Rebuilds the 'Sort By' menu with sort options for the extension list.
        """
    def sort_index(self):
        ...
def _sync_registry(*args, **kwargs):
    ...
EXTENSION_PULL_STARTED_EVENT: int = 8509126198065146478
REGISTRIES_CHANGED_EVENT: int = 17790543992418514273
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
ext_manager = None
